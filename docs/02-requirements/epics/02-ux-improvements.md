# Epic 02: UX Improvements

**Owner:** Chris Park
**Status:** 🔜 Planned (V2)

---

## 1. Summary

Remove friction from daily use. The goal is to make voice capture as fast and seamless as Cmd+V. This includes global hotkeys, silence detection, and feedback during recording.

---

## 2. Problem

The current CLI workflow requires:
1. Opening a terminal
2. Typing `murmur -c`
3. Pressing Enter to stop recording

This friction prevents using voice input for quick captures. Users default to typing because it's "easier" even when speaking would be faster.

---

## 3. Proposed Solution

Reduce the workflow to:
1. Press global hotkey
2. Speak
3. Recording auto-stops on silence (or manual stop)
4. Text appears in clipboard

No terminal, no typing, minimal friction.

---

## 4. User Stories

### Future

- ⏭️ **Global hotkey trigger** - Press a keyboard shortcut from any app to start recording
- ⏭️ **Auto-stop on silence** - Recording ends automatically when user stops speaking
- ⏭️ **Visual feedback** - Menu bar icon or notification shows recording state
- ⏭️ **Audio feedback** - Sound plays when recording starts/stops
- ⏭️ **Warm model loading** - Keep Whisper model in memory for instant transcription
- ⏭️ **Recording indicator** - Show audio levels while recording

---

## 5. Outcomes

**Success Looks Like:**
- Voice capture takes <2 seconds from intent to clipboard
- No context switching required (stay in current app)
- User knows recording state without looking at terminal

**We'll Measure:**
- Time from hotkey to text in clipboard
- Subjective friction score (1-10)

---

## 6. Dependencies

**Requires:**
- Epic 01: Core Dictation (complete)
- Research: macOS hotkey registration (pynput or similar)
- Research: Silence detection algorithms

**Enables:**
- Epic 03: Integrations (better UX makes integrations more valuable)

---

## 7. Risks & Mitigations

| Risk | Impact | Probability | Response |
|------|--------|-------------|----------|
| Hotkey conflicts with other apps | M | M | Make hotkey configurable |
| Silence detection too aggressive | M | M | Configurable threshold, manual override |
| Background process uses too much memory | M | L | Lazy model loading option |

---

## 8. Open Questions

- [ ] Which hotkey library for macOS? (pynput, rumps, native?)
- [ ] Menu bar app or background daemon?
- [ ] How to handle hotkey conflicts?
- [ ] Silence threshold - how many seconds?

---

## 9. Change History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| v1.0 | 2026-01-21 | Chris Park | Initial epic |
