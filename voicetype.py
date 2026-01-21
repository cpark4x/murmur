#!/usr/bin/env python3
"""voicetype - Speech to text using local Whisper.

Usage:
    voicetype           # Record and print to stdout
    voicetype -c        # Record and copy to clipboard
    voicetype -m medium # Use medium model for better quality
    voicetype --learn   # Learn vocabulary from SuperWhisper recordings

First run:
    The first time you use a model, Whisper will download it (~244MB for 'small').
    This is a one-time download - subsequent runs use the cached model.
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path

import numpy as np
import sounddevice as sd
import whisper

SAMPLE_RATE = 16000
MIN_AUDIO_LENGTH = 0.5  # Minimum seconds of audio required
MODELS = ["tiny", "base", "small", "medium", "large"]
CONFIG_DIR = Path.home() / ".config" / "voicetype"
PROMPT_FILE = CONFIG_DIR / "prompt.txt"
SUPERWHISPER_DIR = Path.home() / "Documents" / "superwhisper" / "recordings"

# Cache for loaded model
_model_cache = {}


def record_until_enter() -> np.ndarray:
    """Record audio until user presses Enter."""
    print("Recording... Press Enter to stop.", file=sys.stderr)

    chunks = []
    recording = True

    def callback(indata, frames, time, status):
        if status:
            print(f"Audio status: {status}", file=sys.stderr)
        if recording:
            chunks.append(indata.copy())

    try:
        with sd.InputStream(samplerate=SAMPLE_RATE, channels=1, dtype=np.float32, callback=callback):
            input()  # Block until Enter
            recording = False
    except sd.PortAudioError as e:
        print(f"\nMicrophone error: {e}", file=sys.stderr)
        print("Make sure microphone permission is granted in System Settings > Privacy & Security > Microphone", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nRecording cancelled.", file=sys.stderr)
        sys.exit(0)

    if not chunks:
        print("No audio recorded.", file=sys.stderr)
        sys.exit(1)

    audio = np.concatenate(chunks).flatten()
    duration = len(audio) / SAMPLE_RATE

    if duration < MIN_AUDIO_LENGTH:
        print(f"Recording too short ({duration:.1f}s). Speak for at least {MIN_AUDIO_LENGTH}s.", file=sys.stderr)
        sys.exit(1)

    return audio


def load_prompt() -> str | None:
    """Load custom prompt from config file if it exists."""
    if PROMPT_FILE.exists():
        return PROMPT_FILE.read_text().strip()
    return None


def transcribe(audio: np.ndarray, model_name: str, prompt: str | None = None) -> str:
    """Transcribe audio array using Whisper."""
    print(f"Transcribing with {model_name}...", file=sys.stderr)

    if model_name not in _model_cache:
        _model_cache[model_name] = whisper.load_model(model_name)

    model = _model_cache[model_name]

    # Use prompt to bias toward your vocabulary
    result = model.transcribe(
        audio,
        fp16=False,
        language="en",
        initial_prompt=prompt,
    )
    return result["text"].strip()


def to_clipboard(text: str):
    """Copy text to macOS clipboard."""
    subprocess.run(["pbcopy"], input=text.encode(), check=True)


def learn_from_superwhisper() -> str:
    """Extract vocabulary and style from SuperWhisper recordings."""
    if not SUPERWHISPER_DIR.exists():
        print(f"SuperWhisper recordings not found at {SUPERWHISPER_DIR}", file=sys.stderr)
        sys.exit(1)

    print(f"Learning from SuperWhisper recordings...", file=sys.stderr)

    transcripts = []
    for folder in SUPERWHISPER_DIR.iterdir():
        meta_path = folder / "meta.json"
        if meta_path.exists():
            try:
                data = json.loads(meta_path.read_text())
                text = data.get("result", "") or data.get("rawResult", "")
                if text:
                    transcripts.append(text.strip())
            except (json.JSONDecodeError, KeyError):
                pass

    if not transcripts:
        print("No transcriptions found in SuperWhisper recordings.", file=sys.stderr)
        sys.exit(1)

    print(f"Found {len(transcripts)} recordings", file=sys.stderr)

    # Build a prompt from recent transcripts (Whisper uses this for style/vocab)
    # Take samples from your transcripts to teach Whisper your speaking style
    samples = transcripts[-10:]  # Last 10 recordings
    prompt_text = " ".join(samples)

    # Truncate to ~500 chars (Whisper prompt limit is ~224 tokens)
    if len(prompt_text) > 500:
        prompt_text = prompt_text[:500]

    # Save to config
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    PROMPT_FILE.write_text(prompt_text)

    print(f"\nLearned vocabulary saved to {PROMPT_FILE}", file=sys.stderr)
    print(f"Preview: {prompt_text[:100]}...", file=sys.stderr)

    return prompt_text


def main():
    parser = argparse.ArgumentParser(
        description="Speech to text using local Whisper",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  voicetype              Record and print transcription
  voicetype -c           Record and copy to clipboard
  voicetype -c -m medium Use medium model, copy to clipboard
  voicetype --learn      Learn your vocabulary from SuperWhisper

Models (quality/speed tradeoff):
  tiny   - Fastest, lowest quality
  base   - Fast, decent quality
  small  - Good balance (default)
  medium - High quality, slower
  large  - Best quality, slowest

Learning from SuperWhisper:
  Run 'voicetype --learn' to extract your vocabulary and speaking
  style from SuperWhisper recordings. This creates a prompt that
  helps Whisper recognize your common words and phrases.
        """,
    )
    parser.add_argument(
        "-m", "--model",
        default="small",
        choices=MODELS,
        help="Whisper model to use (default: small)"
    )
    parser.add_argument(
        "-c", "--clipboard",
        action="store_true",
        help="Copy result to clipboard instead of stdout"
    )
    parser.add_argument(
        "-o", "--output",
        type=str,
        metavar="FILE",
        help="Save result to file"
    )
    parser.add_argument(
        "-p", "--prompt",
        type=str,
        help="Custom prompt to bias vocabulary (e.g., 'Claude, Amplifier, Canvas')"
    )
    parser.add_argument(
        "--learn",
        action="store_true",
        help="Learn vocabulary from SuperWhisper recordings"
    )
    parser.add_argument(
        "--list-models",
        action="store_true",
        help="List available models and exit"
    )
    parser.add_argument(
        "--no-prompt",
        action="store_true",
        help="Don't use saved prompt (ignore learned vocabulary)"
    )
    args = parser.parse_args()

    if args.list_models:
        print("Available models:", ", ".join(MODELS))
        print("\nRecommended: 'small' for M3 Pro (best quality/speed balance)")
        return

    if args.learn:
        learn_from_superwhisper()
        return

    # Determine prompt to use
    prompt = None
    if args.prompt:
        prompt = args.prompt
    elif not args.no_prompt:
        prompt = load_prompt()
        if prompt:
            print("Using learned vocabulary.", file=sys.stderr)

    # Record audio
    audio = record_until_enter()

    # Transcribe
    text = transcribe(audio, args.model, prompt)

    # Output
    if args.clipboard:
        to_clipboard(text)
        print("Copied to clipboard.", file=sys.stderr)
        print(text, file=sys.stderr)
    elif args.output:
        with open(args.output, "w") as f:
            f.write(text + "\n")
        print(f"Saved to {args.output}", file=sys.stderr)
    else:
        print(text)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nCancelled.", file=sys.stderr)
        sys.exit(0)
