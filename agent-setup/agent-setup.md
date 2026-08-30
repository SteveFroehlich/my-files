# Possible enhancements

## Voice

**Eleven labs** voice and voice cloning
A 30 minute audio clip will give best cloning results 

Local voice with openclaw
[https://izwiai.com/blog/give-openclaw-agents-local-voice](https://izwiai.com/blog/give-openclaw-agents-local-voice)

---

# Four-Machine Hardware Architecture

The architecture separates workloads by **security boundary and operational role**:

1. **Dirty Machine** — isolated machine for highly sensitive transactions.
2. **Driver Machine** — primary personal/interactive workstation.
3. **Build Server** — (TBD if needed) dedicated macOS development and build environment.
4. **Linux Always-On Server** — 24/7 infrastructure for agents, containers, and AI workloads.

---

## 1. Dirty Machine

**Model:** ASUS Chromebook CX1

**Specs**
- 15.6" 1080p display
- Intel Celeron N4500
- 4 GB RAM
- 128 GB storage
- ~$159 reference price

**Main Responsibilities**
- Highly sensitive web transactions
- Financial/account security operations
- Isolated browsing where compromise of the primary workstation is unacceptable
- Minimal software and attack surface

**Role:** Security isolation

---

## 2. Driver Machine

**Model:** macOS laptop

**Specs**
- TBD / existing Mac laptop

**Main Responsibilities**
- Primary daily workstation
- Interactive development
- Web browsing and communications
- SSH/control point for the Build Server and Linux Server
- AI coding assistants and other interactive tools

**Role:** Human interface / command center

---

## 3. Build Server

**Model:** Mac mini M4

**Specs**
- Apple M4
- 24 GB unified memory
- 256 GB SSD

**Main Responsibilities**
- Dedicated development environment
- macOS builds and testing
- Long-running builds or development tasks that shouldn't consume Driver Machine resources
- Remote development target from the Driver Machine

**Role:** Dedicated macOS development compute

---

## 4. Linux Always-On Server

**Model:** MINISFORUM UM870 Slim  
**Micro Center SKU:** 799197

**Specs**
- AMD Ryzen 7 8745H
- 32 GB DDR5-5600 RAM
- 1 TB SSD
- Radeon 780M integrated GPU

**Main Responsibilities**
- 24/7 Docker/container workloads
- Always-on AI agents
- OpenClaw Gateway / agent infrastructure
- Realtime conversational voice stack
- Faster-Whisper / local STT
- Local TTS where appropriate
- Local AI/model workloads
- General self-hosted services
- Potential Nostr relay

**Role:** Always-on infrastructure + AI compute

#### where to buy

We chose the **MINISFORUM UM870 Slim** from the Chicago 

Micro Center
[Web](https://www.microcenter.com/site/stores/chicago.aspx?storeid=151&utm_source=chatgpt.com)
Address: 2645 N Elston Ave, Chicago, IL 60647, United States
Phone: +17732921700

**2645 N Elston Ave, Chicago, IL 60647**

**Machine:** MINISFORUM UM870 Slim
**SKU:** 799197
**Ryzen 7 8745H / 32GB RAM / 1TB SSD / Radeon 780M**
**Current listed price:** $699.99

[Buy / reserve the UM870 Slim at Micro Center](https://www.microcenter.com/product/689898/minisforum-um870-slim-mini-pc-amd-ryzen-7-8745h-38ghz-processor-32gb-ddr5-5600-ram-1tb-solid-state-drive-amd-radeon-780m-microsoft-windows-11-pro?bvstate=pg%3A3%2Fct%3Ar&showfullsite=true&storeid=151&utm_source=chatgpt.com)

Micro Center's current search results show **2 in stock at the Chicago store**, although inventory can change quickly. ([Micro Center][1])

[1]: https://www.microcenter.com/search/search_results.aspx?fq=category%3ADesktop+Computers%7C106%2Cbrand%3AMinisforum+OR+GMKtec&vkw=pc&utm_source=chatgpt.com "Desktop Computers : Minisforum : GMKtec : Micro Center"


# voice

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

# Data setup

AGENTS.md - the team roster ?

Memory.md - the permanent brain 

Dream.md - daily log 

Prompts.md - the human blueprint 