import requests
import os
from dotenv import load_dotenv


load_dotenv(dotenv_path=".env", override=True)
OPENTRIP_API_KEY = os.getenv("OPENTRIP_API_KEY")

def get_attractions(city):
    geo_url = f"https://api.opentripmap.com/0.1/en/places/geoname?name={city}&apikey={OPENTRIP_API_KEY}"
    geo_resp = requests.get(geo_url).json()
    lat, lon = geo_resp.get("lat"), geo_resp.get("lon")
    if not lat or not lon:
        return "Couldn't find the city."
    
    places_url = f"https://api.opentripmap.com/0.1/en/places/radius?radius=1000&lon={lon}&lat={lat}&format=json&limit=3&apikey={OPENTRIP_API_KEY}"
    places_resp = requests.get(places_url).json()
    attractions = [f"- {place['name']} ({place['kinds']})" for place in places_resp if place.get("name")]
    return "Top attractions:\n" + "\n".join(attractions)
