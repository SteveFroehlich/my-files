
# Possible enhancements

## Voice
**Eleven labs** voice and voice cloning
A 30 minute audio clip will give best cloning results 

---
# Locked in Architecture

The main Mac laptop my act as a driver. There should be two users
1. standard user - has limited privledges - for running things
2. admin user - has sensitive files but encrypted using FileVault

Server architecture uses a **two-machine split architecture**:

1. **Mac mini** = interactive development / control plane
2. **Linux mini PC** = always-on infrastructure / compute plane

This avoids overpaying for one large machine while improving concurrency, isolation, reliability, and responsiveness.

setup specs:
- **Mac mini M4 / 24GB RAM / 256GB SSD**
- **Fanless Intel N100 Linux mini PC / 32GB RAM / 512GB SSD**

This gives the best balance of:

- Cost
- Responsiveness
- Always-on reliability
- Docker capacity
- Experimentation flexibility
- Long-term extensibility
---

## 1. Mac mini — Primary Dev Machine / Control Plane

### Recommended Spec

- **Model:** Apple Mac mini
- **Chip:** M4
- **Memory:** 24GB unified memory
- **Storage:** 256GB SSD
- **Role:** Interactive development machine

### Primary Responsibilities

- Browser
- IDE / editor
- Terminal workflows
- Primary development environment
- Short-lived Docker containers
- Experimentation with new repos/tools
- Occasional local LLM usage
- Control plane for managing the Linux box

### Rationale

- Strong performance-per-dollar
- Very responsive for interactive work
- Quiet and power-efficient
- Avoids Linux desktop friction
- 24GB RAM is the minimum viable choice for Docker + IDE + browser

---

## 2. Linux Mini PC — Always-On Infra / Compute Plane

### Recommended Spec

- **Model:** Fanless Intel N100 mini PC
- **CPU:** Intel N100
- **Memory:** 32GB RAM
- **Storage:** 512GB SSD
- **Cooling:** Fanless
- **Role:** Always-on local infrastructure box

### Primary Responsibilities

- Long-lived Docker containers
- Postgres
- Redis
- APIs / backend services
- Background workers
- Agents
- Schedulers / cron jobs
- WireGuard VPN
- Persistent services
- Occasional vector DB workloads

### Rationale

- Dedicated always-on compute
- No resource contention with daily dev work
- Low power usage
- Silent operation
- Cheap compared with a single large workstation
- 32GB RAM is the practical minimum for reliable multi-container infra

---
# Agent specific context below

## Rejected Option

### Single Large Machine, e.g. Meerkat 64GB at ~$2,200

Rejected because it:

- Over-consolidates dev and infra workloads
- Creates resource contention
- Costs significantly more
- Reduces separation of concerns
- Limits parallelism
- Makes the system less flexible over time



## voice

```
[ Your Mic / Speaker ] 
       │  ▲
       ▼  │ (Audio Streams)
┌────────────────────────────────────────┐
│      LOCAL AUDIO PIPELINE LAYER        │
│  - STT: Deepgram / Whisper Local       │
│  - TTS: ElevenLabs / OpenAI            │
└────────────────────────────────────────┘
       │  ▲
       ▼  │ (Pure Text Prompts & Outputs)
┌────────────────────────────────────────┐
│     SWAPPABLE AGENT ROUTER SWITCH      │
│  [ ] Cursor CLI                        │
│  [ ] Claude Code                       │
│  [ ] OpenClaw Gateway                  │
└────────────────────────────────────────┘
```

### 🧱 The 100% Local Voice Stack

To avoid dependencies on web browsers or remote cloud WebRTC infrastructure, orchestrate your local machine using three specific open-source tools:

Speech-to-Text (STT): Faster-Whisper. This is a highly optimized CTranslate2 implementation of OpenAI’s Whisper model. It runs locally on your machine's CPU or GPU, delivering sub-100ms transcription latency.

Audio In/Out Pipeline: Pipecat (Local Runner). An open-source Python framework designed for real-time voice orchestration. It handles voice activity detection (VAD), meaning it knows exactly when you stop talking and when to mute your speakers if you interrupt the agent.

Text-to-Speech (TTS): Piper. A blazing-fast local neural text-to-speech system that can easily match the speed of your terminal output.