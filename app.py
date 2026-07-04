from flask import Flask, render_template, request, session
import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "dev-secret-key-change-this")

API_KEY = os.getenv('WEATHER_API_KEY')
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'
FORECAST_URL = 'https://api.openweathermap.org/data/2.5/forecast'

@app.route('/', methods=['GET', 'POST'])
def home():
    weather_data = None
    forecast_data = None
    error = None

    if request.method == 'POST':
        city = request.form.get('city', '').strip()

        if not city:
            error = 'Please enter a city name.'
        else:
            response = None
            try:
                params = {'q': city, 'appid': API_KEY, 'units': 'metric'}
                response = requests.get(BASE_URL, params=params, timeout=5)
            except requests.exceptions.RequestException:
                error = 'Could not connect. Check your internet connection and try again.'

            if response and response.status_code == 200:
                data = response.json()
                weather_data = {
                    'city': data['name'],
                    'country': data['sys']['country'],
                    'temperature': data['main']['temp'],
                    'feels_like': data['main']['feels_like'],
                    'humidity': data['main']['humidity'],
                    'pressure': data['main']['pressure'],
                    'visibility': round(data.get('visibility', 0) / 1000, 1),
                    'description': data['weather'][0]['description'].title(),
                    'icon': data['weather'][0]['icon'],
                    'wind_speed': data['wind']['speed'],
                    'sunrise': datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M'),
                    'sunset': datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M'),
                }
                session['weather_data'] = weather_data

                try:
                    forecast_response = requests.get(FORECAST_URL, params=params, timeout=5)
                    if forecast_response.status_code == 200:
                        raw_forecast = forecast_response.json()['list']
                        forecast_data = []
                        seen_days = set()
                        for entry in raw_forecast:
                            day = entry['dt_txt'].split(' ')[0]
                            if day not in seen_days and len(seen_days) < 5:
                                seen_days.add(day)
                                forecast_data.append({
                                    'day': datetime.fromtimestamp(entry['dt']).strftime('%a'),
                                    'temp': round(entry['main']['temp']),
                                    'icon': entry['weather'][0]['icon'],
                                    'description': entry['weather'][0]['description'].title(),
                                })
                        session['forecast_data'] = forecast_data
                except requests.exceptions.RequestException:
                    forecast_data = None

            elif response is not None:
                error = 'City not found. Please check the spelling and try again.'

    return render_template('index.html', weather=weather_data, forecast=forecast_data, error=error)


@app.route('/send-summary', methods=['POST'])
def send_summary():
    email = request.form.get('email', '').strip()
    weather = session.get('weather_data')
    forecast = session.get('forecast_data')

    if not weather:
        return render_template('index.html', weather=None, forecast=None,
                                error="Please search for a city first.")

    if not email:
        return render_template('index.html', weather=weather, forecast=forecast,
                                error="Please enter an email address.")

    from crew_setup import send_weather_summary
    try:
        send_weather_summary(weather, email)
        email_sent = True
    except Exception:
        email_sent = False

    return render_template('index.html', weather=weather, forecast=forecast, email_sent=email_sent)


if __name__ == '__main__':
    app.run(debug=True)

