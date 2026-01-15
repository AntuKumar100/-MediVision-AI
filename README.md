MediVision-AI

An AI-Powered Multimodal Medical Assistant (Vision + Voice + Intelligence)

MediVision AI is a multimodal healthcare-focused AI application that simulates an AI Doctor Assistant. It can understand medical images, process patient voice input, and respond with a natural doctor-like voice through an interactive UI.

⚠️ Disclaimer: MediVision AI is for research and educational purposes only and is not a replacement for professional medical advice.

🚀 Features

🧠 Multimodal LLM (Text + Image Understanding)

🎙️ Patient Voice Input (Speech-to-Text)

🗣️ Doctor Voice Output (Text-to-Speech)

🖼️ Medical Image Processing

💬 Interactive VoiceBot UI

⚡ Fast AI inference using Groq

🏗️ System Architecture

Patient Voice / Image
        ↓
Speech-to-Text (Whisper)
        ↓
Multimodal LLM (LLaMA 3 via Groq)
        ↓
Text Response
        ↓
Text-to-Speech (gTTS / ElevenLabs)
        ↓
Doctor Voice Output (UI)

📌 Project Phases
Phase 1: Setup the Brain of the Doctor (Multimodal LLM)

Configure Groq API Key

Convert medical images to supported formats (PNG / JPEG / Base64)

Initialize LLaMA 3 Multimodal LLM

Enable text + image reasoning

Phase 2: Setup Voice of the Patient (Speech-to-Text)

Record patient audio using:

ffmpeg

pyaudio / sounddevice

Transcribe speech using OpenAI Whisper

Send transcribed text to the LLM

Phase 3: Setup Voice of the Doctor (Text-to-Speech)

Convert AI-generated text responses into voice

Supported TTS engines:

gTTS

ElevenLabs

Play doctor voice response in real time

Phase 4: Setup UI for VoiceBot

Build UI using Gradio

Support:

Voice input

Image upload

Real-time AI responses

Audio output playback

🛠️ Tools & Technologies

Groq – AI inference engine

LLaMA 3 – Open-source LLM by Meta

OpenAI Whisper – Speech-to-Text

gTTS / ElevenLabs – Text-to-Speech

Gradio – UI framework

Python

VS Code

🌱 Future Improvements

Medical report generation

Patient history memory

Multi-language support

Medical knowledge grounding

HIPAA-compliant deployment
