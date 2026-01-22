# murmur: Vision

**Local-first speech-to-text that learns your voice and vocabulary.**

_murmur_

**Owner:** Chris Park
**Last Updated:** 2026-01-21

---

## Summary

murmur solves the problem of quality speech-to-text without cloud costs or privacy concerns. It uses OpenAI's Whisper locally on your machine, learns your vocabulary from existing recordings, and outputs text ready to paste into any application. Built for developers and creators who talk faster than they type.

---

## Table of Contents

1. [The Problems We're Solving](#1-the-problems-were-solving)
2. [Strategic Positioning](#2-strategic-positioning)
3. [Who This Is For](#3-who-this-is-for)
4. [The Sequence](#4-the-sequence)

---

## 1. The Problems We're Solving

### Problem 1: Cloud STT is Expensive and Privacy-Invasive

**Current Reality:**
- Cloud speech-to-text services charge per minute of audio
- Your voice data is sent to third-party servers
- Requires API keys and account management
- Quality varies by provider and pricing tier

**The Impact:**
- Hesitation to use STT for quick tasks (cost adds up)
- Privacy-conscious users avoid STT entirely
- Vendor lock-in to specific cloud providers

**Why This Matters:**
Modern hardware (M-series Macs, GPUs) can run Whisper locally with excellent quality. There's no technical reason to pay for cloud STT for personal use.

**Who this affects:** Developers, writers, anyone doing frequent dictation

---

### Problem 2: Generic STT Doesn't Know Your Vocabulary

**Current Reality:**
- STT systems mishear technical terms, product names, jargon
- "Claude" becomes "cloud", "Amplifier" becomes "amplify"
- No way to teach the system your specific vocabulary
- Each transcription requires manual corrections

**The Impact:**
- Time wasted fixing transcription errors
- Frustration when domain-specific terms are consistently wrong
- Reduced trust in STT output

**Why This Matters:**
Whisper supports prompt conditioning - you can bias it toward your vocabulary. Most tools don't expose this capability.

**Who this affects:** Anyone with domain-specific vocabulary (developers, researchers, specialists)

---

### Problem 3: Existing Tools Have Poor UX for Quick Capture

**Current Reality:**
- SuperWhisper is great but costs money
- Built-in macOS dictation is mediocre quality
- Most CLI tools require complex setup
- No easy way to capture voice and paste immediately

**The Impact:**
- Friction prevents using voice input when it would be faster
- Context switching to voice tools breaks flow
- Voice input reserved for "big" tasks, not quick capture

**Why This Matters:**
Voice input should be as easy as Cmd+V. The less friction, the more it gets used.

**Who this affects:** Power users who want voice as a seamless input method

---

## 2. Strategic Positioning

### The Core Insight

**What others do:**
- SuperWhisper: Excellent UX, subscription model, closed source
- macOS Dictation: Free but mediocre quality, no customization
- Cloud APIs: Pay-per-use, privacy concerns, complex integration

**Why they're incomplete:**
- SuperWhisper solves UX but adds cost
- macOS solves cost but sacrifices quality
- Cloud APIs solve quality but add cost and privacy issues

**Our position:**
murmur is **free, local, high-quality, and learns your vocabulary**. It trades polish for simplicity and ownership.

**The difference:**
- **SuperWhisper**: Polished product, subscription fee
- **murmur**: Simple CLI, free forever, you own it

murmur is built for **developers who value simplicity and ownership**, not users who want a polished product experience.

---

### The 3 Strategic Pillars

#### 1. Local-First

**The old way:** Send audio to cloud, wait for response, pay per minute
**The murmur way:** Process everything on-device, instant, free

- Your voice never leaves your machine
- No API keys, no accounts, no billing
- Works offline

#### 2. Vocabulary Learning

**The old way:** Accept whatever the model outputs, fix errors manually
**The murmur way:** Learn from your SuperWhisper history, bias toward your terms

- `murmur --learn` extracts your vocabulary
- Prompt conditioning improves recognition of your specific terms
- Gets better the more you use SuperWhisper

#### 3. Unix Philosophy

**The old way:** Monolithic app with features you don't need
**The murmur way:** Do one thing well, compose with other tools

- Single Python file, ~200 lines
- Outputs to stdout, clipboard, or file
- Pipe to other tools: `murmur | pbcopy`, `murmur >> notes.txt`

---

### What We're NOT Building

Clear boundaries:

- **NOT a SuperWhisper replacement** (we're a CLI tool, not a menu bar app)
- **NOT a real-time transcription service** (we're batch processing)
- **NOT a voice assistant** (we're text output, not AI conversation)
- **NOT cross-platform initially** (macOS focus, pbcopy dependency)

---

## 3. Who This Is For

### Primary: Developers and Technical Users

People who:
- Live in the terminal
- Value owning their tools
- Have domain-specific vocabulary (code, products, technical terms)
- Use SuperWhisper or similar tools already

**Why they're underserved:**
- SuperWhisper: Great but costs $8/month
- macOS Dictation: Poor quality for technical terms
- Cloud STT: Overkill for quick capture, privacy concerns

### Secondary: Content Creators

People who:
- Dictate drafts, notes, ideas
- Want voice-to-text for Ridecast, blogs, documentation
- Need quick capture without app switching

**What they need:**
- Fast capture to clipboard
- Good quality transcription
- No friction in the workflow

---

## 4. The Sequence

**Sequence: CLI → UX → Integrations**

Start with core functionality, then improve UX, then add integrations.

### V1: Core Dictation (Current - Done)

**Focus:** Basic speech-to-text that works

**Core capabilities:**
- Record from microphone until Enter
- Transcribe with local Whisper
- Output to stdout, clipboard, or file
- Learn vocabulary from SuperWhisper

**V1 validates:** Local Whisper is good enough for daily use

**V1 reality:** Fully functional CLI, vocabulary learning works, ready for daily use

---

### V2: UX Improvements (Next)

**Focus:** Remove friction from daily use

**Core capabilities:**
- Global hotkey trigger (no terminal needed)
- Auto-stop on silence detection
- Visual/audio feedback during recording
- Faster model loading (keep model warm)

**V2 goal:** Voice capture is as fast as Cmd+V

---

### V3: Integrations (Future)

**Focus:** Seamless workflow with other tools

**Core capabilities:**
- Direct integration with Ridecast
- Integration with Canvas/Workspaces
- Menu bar app (optional)
- Streaming output (see words as you speak)

**V3 goal:** murmur is invisible - voice just becomes text wherever you need it

---

## Related Documentation

- [Epic 01: Core Dictation](../02-requirements/epics/01-core-dictation.md) - V1 implementation
- [Epic 02: UX Improvements](../02-requirements/epics/02-ux-improvements.md) - V2 roadmap
- [Epic 03: Integrations](../02-requirements/epics/03-integrations.md) - V3 roadmap

---

## Change History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| v1.0 | 2026-01-21 | Chris Park | Initial vision document |
