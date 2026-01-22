# Epic 01: Core Dictation

**Owner:** Chris Park
**Status:** ✅ Complete

---

## 1. Summary

Basic speech-to-text functionality using local Whisper. Record from microphone, transcribe locally, output text. This is the foundation that validates local STT is viable for daily use.

---

## 2. Problem

Users need to convert speech to text without cloud costs, privacy concerns, or poor quality. Existing solutions either cost money (SuperWhisper), have poor quality (macOS Dictation), or require complex setup (raw Whisper CLI).

---

## 3. Proposed Solution

A simple CLI tool that:
- Records audio from the default microphone
- Transcribes using OpenAI Whisper locally
- Outputs text to stdout, clipboard, or file
- Learns vocabulary from existing SuperWhisper recordings

---

## 4. User Stories

### Implemented

| # | Story | Status |
|---|-------|--------|
| 01-01 | Record and transcribe | ✅ Done |
| 01-02 | Copy to clipboard | ✅ Done |
| 01-03 | Choose Whisper model | ✅ Done |
| 01-04 | Learn from SuperWhisper | ✅ Done |
| 01-05 | Save to file | ✅ Done |

### Details

**01-01: Record and transcribe**
- User runs `murmur`
- Speaks into microphone
- Presses Enter to stop
- Sees transcribed text in terminal

**01-02: Copy to clipboard**
- User runs `murmur -c`
- Speaks and presses Enter
- Text is copied to clipboard, ready to paste

**01-03: Choose Whisper model**
- User runs `murmur -m medium` for higher quality
- User runs `murmur -m tiny` for faster speed
- Default is `small` (best balance for M-series Macs)

**01-04: Learn from SuperWhisper**
- User runs `murmur --learn`
- Tool extracts vocabulary from SuperWhisper recordings
- Future transcriptions are biased toward user's terms

**01-05: Save to file**
- User runs `murmur -o notes.txt`
- Transcription is saved to specified file

---

## 5. Outcomes

**Success Looks Like:**
- Tool works reliably for daily dictation
- Transcription quality is acceptable (>95% accuracy for clear speech)
- Vocabulary learning improves recognition of user's terms

**We'll Measure:**
- Does it work? (binary - yes)
- Is quality good enough? (subjective - yes)

---

## 6. Dependencies

**Requires:** 
- Python 3.10+
- openai-whisper, sounddevice, numpy
- macOS (for pbcopy clipboard support)

**Enables:**
- Epic 02: UX Improvements
- Epic 03: Integrations

---

## 7. Risks & Mitigations

| Risk | Impact | Probability | Response |
|------|--------|-------------|----------|
| Whisper quality insufficient | H | L | Use larger models, prompt conditioning |
| Model download too slow | M | L | Document first-run experience |
| Microphone permissions | M | M | Added friendly error messages |

---

## 8. Open Questions

- [x] Which model is best for M3 Pro? → `small`
- [x] How to handle vocabulary learning? → Prompt conditioning from SuperWhisper

---

## 9. Change History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| v1.0 | 2026-01-21 | Chris Park | Initial epic, all stories complete |
