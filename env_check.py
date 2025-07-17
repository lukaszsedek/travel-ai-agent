import os
from dotenv import load_dotenv

REQUIRED_KEYS = [
    "OPENAI_API_KEY",
    "WEATHER_API_KEY",
    "OPENTRIP_API_KEY"
]

def check_env():
    load_dotenv()  # Wczytaj zmienne z pliku .env

    missing = []
    for key in REQUIRED_KEYS:
        value = os.getenv(key)
        if not value or "your_" in value.lower():
            missing.append(key)

    if missing:
        print("❌ Missing or invalid environment variables:")
        for key in missing:
            print(f"   - {key}")
        print("\n➡️  Please set these variables in your .env file.")
        exit(1)
    else:
        print("✅ All required environment variables are set.")

if __name__ == "__main__":
    check_env()
