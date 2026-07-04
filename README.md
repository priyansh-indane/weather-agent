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

weather-agent/
├── app.py                 # Flask app — routes, weather/forecast fetching, sessions
├── crew_setup.py          # CrewAI agent + task definition (the LLM logic)
├── email_tool.py          # Custom CrewAI tool — sends email via SMTP
├── requirements.txt       # Python dependencies
├── .gitignore
├── README.md
├── templates/
│   └── index.html         # Main page template (Jinja2)
└── static/
└── style.css          # All styling

---

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/your-username/weather-agent.git
cd weather-agent
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file
In the project root:
WEATHER_API_KEY=your_openweathermap_key
OPENAI_API_KEY=your_openai_key
EMAIL_ADDRESS=your_gmail_address@gmail.com
EMAIL_APP_PASSWORD=your_16_character_app_password
FLASK_SECRET_KEY=any_random_string

**Where to get each key:**
- `WEATHER_API_KEY` → [openweathermap.org](https://openweathermap.org/) → sign up → API keys tab
- `OPENAI_API_KEY` → [platform.openai.com](https://platform.openai.com/api-keys)
- `EMAIL_APP_PASSWORD` → Google Account → Security → 2-Step Verification → App Passwords (requires 2FA)

> ⚠️ Never commit your `.env` file — it's already excluded via `.gitignore`.

### 4. Run the app
```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

---

## How It Works

1. **Search** — enter a city, state, or country and hit **Scan**
2. **Fetch** — Flask calls the OpenWeatherMap API for current conditions and a 5-day forecast
3. **Render** — results populate the dashboard: live stats, forecast strip, all server-rendered via Jinja2
4. **Delegate to the agent** — click **Email Me This Summary**, and the live weather data is handed to a CrewAI agent
5. **Agent reasoning** — the agent (powered by an OpenAI LLM) writes a short, natural-language summary based on the actual data
6. **Autonomous action** — the agent calls its own `send_email` tool to deliver the summary directly to the provided email address

---

## Roadmap / Ideas

- [ ] WhatsApp delivery via Twilio, alongside email
- [ ] Persistent search history (SQLite)
- [ ] "Use my location" via browser geolocation
- [ ] Unit toggle (°C/°F, m/s/mph)
- [ ] Multi-agent workflow (e.g. a separate recommendation agent)
- [ ] Deployment (Render / PythonAnywhere)

---

## License

This project is open for personal and educational use. Feel free to fork and build on it.