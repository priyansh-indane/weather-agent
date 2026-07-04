# 🌤️ Weather Agent

A full-stack weather dashboard that combines live weather data with an AI agent — search any location for real-time conditions and a 5-day forecast, then get an AI-generated summary emailed straight to your inbox with one click.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Flask](https://img.shields.io/badge/Flask-2.x-black)
![CrewAI](https://img.shields.io/badge/CrewAI-Agent-orange)
![OpenAI](https://img.shields.io/badge/LLM-OpenAI-green)

---

## Overview

Weather Agent pairs a real-time weather dashboard with an autonomous AI agent. Instead of just displaying data, it uses an LLM-powered agent (built with CrewAI) that reads the live weather conditions, writes a natural-language summary in its own words, and autonomously calls an email tool to deliver it — all triggered by a single click in the UI.

---

## Tech Stack

### Backend
- **Python** — core application logic
- **Flask** — web framework handling routing, sessions, and server-side rendering
- **Jinja2** — Flask's templating engine, used to dynamically inject weather data into HTML

### API Integration
- **OpenWeatherMap API** — live current weather + 5-day forecast data, fetched via the `requests` library
- **REST calls with error handling** — timeouts, failed lookups, and network errors are caught and surfaced gracefully in the UI

### AI / LLM Integration
- **CrewAI** — an agent-orchestration framework used to define an autonomous "Weather Summary Assistant" agent
- **OpenAI (LLM)** — powers the agent's natural-language reasoning and writing
- **Custom Tool (`email_tool.py`)** — a CrewAI tool built on Python's `smtplib`, giving the agent the ability to actually *send* an email autonomously rather than just generate text

This is the core "agentic" piece of the project: the agent isn't just prompted for text — it's given a **goal**, **context** (the live weather data), and a **tool**, and it decides to call that tool to complete the task.

### Frontend
- **HTML + Jinja2 templating** — server-rendered structure
- **Custom CSS** — a hand-built, meteorology-instrument-panel-inspired design (no UI framework/template), including animated SVG "isobar" lines, a custom typography system (Space Grotesk, Inter, IBM Plex Mono), and a responsive grid dashboard
- **Vanilla JavaScript** — live clock, loading states, and form interactivity — no frontend framework dependencies

### Environment & Config
- **python-dotenv** — loads API keys and secrets from a local `.env` file, kept out of version control

---

## Features

- 🌍 **Live weather data** — temperature, feels-like, humidity, wind, pressure, and visibility
- 📅 **5-day forecast** — daily outlook with condition icons
- 🤖 **AI agent email summaries** — CrewAI agent reads live data, writes a short human-sounding summary, and emails it using its own tool
- 🎨 **Custom-designed UI** — distinctive dark, instrument-panel aesthetic instead of a generic template
- ⚡ **Robust error handling** — empty input, city-not-found, and network failures are all handled explicitly

---

## Project Structure