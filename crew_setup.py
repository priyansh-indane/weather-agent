from crewai import Agent, Task, Crew
from email_tool import SendEmailTool


def send_weather_summary(weather, recipient_email):
    summarizer_agent = Agent(
        role="Weather Summary Assistant",
        goal="Write a short, friendly weather summary and email it to the user",
        backstory=(
            "You are a helpful assistant that turns raw weather data into a short, "
            "friendly summary and sends it to people via email. Your tone is warm "
            "and natural, like a helpful friend, not robotic or overly formal."
        ),
        tools=[SendEmailTool()],
        verbose=True,
    )

    task = Task(
        description=f"""
        Here is the current weather data for {weather['city']}, {weather['country']}:
        - Temperature: {weather['temperature']}°C (feels like {weather['feels_like']}°C)
        - Condition: {weather['description']}
        - Humidity: {weather['humidity']}%
        - Wind speed: {weather['wind_speed']} m/s
        - Pressure: {weather['pressure']} hPa
        - Visibility: {weather['visibility']} km
        - Sunrise: {weather['sunrise']}, Sunset: {weather['sunset']}

        Write the email body with this exact layout (use actual line breaks, not
        run-on text):

        LINE 1 (greeting, on its own line): A short, warm greeting with one emoji,
        e.g. "Hello! 👋" or "Hey there! ☀️"

        [blank line]

        MAIN PARAGRAPH (5-6 sentences): Summarize the weather — temperature and how
        it feels, humidity and wind in plain language, and 1-2 of the other factors
        (visibility, pressure, sunrise/sunset) if worth mentioning. Include one
        practical tip based on staying comfortable — umbrella, clothing choice, or
        staying hydrated. Sprinkle in 2-3 emojis naturally through this paragraph
        where they fit (🌧️ 💧 🌬️ 🌡️ ☁️ ☀️ 🌤️ ❄️), each used only once.

        [blank line]

        CLOSING LINE (on its own line): A short, warm sign-off with one emoji,
        tailored specifically to today's actual conditions rather than a stock phrase.

        The greeting and closing line must be visually separate from the main
        paragraph — do not merge everything into one block of text. Aim for about
        70-90 words total across all parts.

        Then use the send_email tool to send this summary to {recipient_email}.
        Use the subject line: "Your Weather Summary for {weather['city']}".
        """,
        expected_output="Confirmation that the email was sent successfully.",
        agent=summarizer_agent,
    )

    crew = Crew(agents=[summarizer_agent], tasks=[task])
    return crew.kickoff()