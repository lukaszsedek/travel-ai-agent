import requests
import os
from dotenv import load_dotenv


load_dotenv(dotenv_path=".env", override=True)

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
print(f"DEBUG: WEATHER_API_KEY = {WEATHER_API_KEY}")

def get_weather(query):
    try:
        city, date = query.split(",")
        city = city.strip()
        date = date.strip()
        url = f"http://api.weatherapi.com/v1/forecast.json?key={WEATHER_API_KEY}&q={city}&days=3"
        resp = requests.get(url)
        data = resp.json()

        if "error" in data:
            return f"❌ Weather API error: {data['error'].get('message', 'Unknown error')}"

        forecast = data.get("forecast", {}).get("forecastday", [])
        for day in forecast:
            if day["date"] == date:
                condition = day["day"]["condition"]["text"]
                temp = day["day"]["avgtemp_c"]
                return f"🌤️ Weather in {city} on {date}: {condition}, {temp}°C"

        return f"⚠️ No forecast available for {city} on {date}."

    except Exception as e:
        return f"❌ get_weather failed: {str(e)}"
