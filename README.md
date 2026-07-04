# 🌤️ Weather Agent

A Flask weather dashboard with live conditions, a 5-day forecast, and an AI agent that summarizes the weather and emails it to you on request.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Flask](https://img.shields.io/badge/Flask-2.x-black)
![CrewAI](https://img.shields.io/badge/CrewAI-Agent-orange)
![OpenAI](https://img.shields.io/badge/LLM-OpenAI-green)

## Overview

Search any city for real-time weather and a 5-day forecast. Click one button, and a CrewAI agent reads the live data, writes a natural-language summary, and emails it to you using its own email tool — no manual copy-pasting, the agent decides and acts on its own.

## Tech Stack

- **Backend:** Python, Flask, Jinja2
- **API:** OpenWeatherMap (live weather + forecast)
- **AI/LLM:** CrewAI (agent orchestration) + OpenAI (reasoning) + a custom email tool built on `smtplib`
- **Frontend:** HTML, custom CSS, vanilla JavaScript — no frameworks
- **Config:** python-dotenv for API keys

## Features

- 🌍 Live weather (temp, humidity, wind, pressure, visibility)
- 📅 5-day forecast
- 🤖 AI agent that writes and emails a weather summary autonomously
- 🎨 Custom instrument-panel-style UI
- ⚡ Error handling for bad input, city-not-found, and network failures

## Project Structure

weather-agent/
├── app.py              # Flask routes + weather fetching
├── crew_setup.py       # CrewAI agent + task
├── email_tool.py       # Custom tool: sends email
├── requirements.txt
├── .gitignore
├── README.md
├── templates/
│   └── index.html
└── static/
└── style.css

## Setup

```bash
git clone https://github.com/your-username/weather-agent.git
cd weather-agent
pip install -r requirements.txt
```

Create a `.env` file:
WEATHER_API_KEY=your_openweathermap_key
OPENAI_API_KEY=your_openai_key
EMAIL_ADDRESS=your_gmail_address@gmail.com
EMAIL_APP_PASSWORD=your_16_character_app_password
FLASK_SECRET_KEY=any_random_string

Run it:
```bash
python app.py
```

Visit `http://127.0.0.1:5000`.

## How It Works

1. Search a city → Flask fetches live weather + forecast from OpenWeatherMap
2. Click "Email Me This Summary" → weather data is handed to a CrewAI agent
3. The agent (powered by an OpenAI LLM) writes a short summary and autonomously calls its email tool to send it

## Roadmap

- [ ] WhatsApp delivery via Twilio
- [ ] Persistent search history (SQLite)
- [ ] "Use my location" via geolocation
- [ ] Deploy live (Render / PythonAnywhere)

## License

Open for personal and educational use.