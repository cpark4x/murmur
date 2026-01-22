# murmur

A CLI speech-to-text tool using local Whisper. Record from your microphone, transcribe locally, and optionally copy to clipboard.

## Installation

```bash
pip install openai-whisper sounddevice numpy
```

## Usage

```bash
# Record and print transcription
murmur

# Record and copy to clipboard
murmur -c

# Use a different model (tiny/base/small/medium/large)
murmur -m medium

# Learn vocabulary from SuperWhisper recordings
murmur --learn
```

## Models

| Model  | Speed   | Quality |
|--------|---------|---------|
| tiny   | Fastest | Lower   |
| base   | Fast    | Decent  |
| small  | Medium  | Good (default) |
| medium | Slower  | High    |
| large  | Slowest | Best    |

The first time you use a model, Whisper downloads it automatically (~244MB for 'small').

## Features

- **Local processing** - All transcription happens on your machine
- **Clipboard support** - Use `-c` to copy directly to clipboard
- **Custom vocabulary** - Learn from your SuperWhisper recordings with `--learn`
- **Multiple models** - Choose speed vs quality tradeoff

## License

MIT
