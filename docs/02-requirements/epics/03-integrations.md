# Epic 03: Integrations

**Owner:** Chris Park
**Status:** 🔮 Future (V3)

---

## 1. Summary

Make murmur invisible by integrating directly with the tools where text is needed. Instead of copy-paste, voice input flows directly into Ridecast, Canvas, and other applications.

---

## 2. Problem

Even with great UX (Epic 02), there's still a copy-paste step. For frequent use cases like:
- Dictating podcast scripts into Ridecast
- Adding notes to Canvas workspaces
- Writing documentation

The ideal workflow is: speak → text appears where you need it.

---

## 3. Proposed Solution

Build integrations that connect murmur directly to target applications:
- Ridecast: Direct text input for podcast scripts
- Canvas/Workspaces: Voice notes that become workspace content
- Generic: Streaming output, API mode for other tools

---

## 4. User Stories

### Future

- ⏭️ **Ridecast integration** - Dictate directly into Ridecast text fields
- ⏭️ **Canvas integration** - Voice creates notes/content in workspaces
- ⏭️ **Streaming output** - See words appear as you speak
- ⏭️ **API/server mode** - Other tools can request transcription
- ⏭️ **Menu bar app** - Full GUI for non-terminal users
- ⏭️ **Watch folder** - Transcribe audio files dropped in a folder

---

## 5. Outcomes

**Success Looks Like:**
- Zero friction between voice and destination
- Voice input is the default for long-form text
- murmur is invisible infrastructure

**We'll Measure:**
- Adoption in daily workflow (subjective)
- Time saved vs typing (estimated)

---

## 6. Dependencies

**Requires:**
- Epic 01: Core Dictation (complete)
- Epic 02: UX Improvements (recommended)
- Ridecast API or extension points
- Canvas/Workspaces API or extension points

**Enables:**
- Voice-first workflows across all tools

---

## 7. Risks & Mitigations

| Risk | Impact | Probability | Response |
|------|--------|-------------|----------|
| Ridecast has no API | H | M | Browser extension or clipboard watching |
| Integration maintenance burden | M | M | Keep integrations simple and optional |
| Scope creep into "voice assistant" | M | L | Stay focused on text output only |

---

## 8. Open Questions

- [ ] Does Ridecast have extension points?
- [ ] How does Canvas handle external input?
- [ ] Streaming: word-by-word or sentence-by-sentence?
- [ ] Is a menu bar app worth the complexity?

---

## 9. Change History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| v1.0 | 2026-01-21 | Chris Park | Initial epic |
