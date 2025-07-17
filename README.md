# 🧳 Travel Buddy AI Agent

An intelligent travel assistant powered by OpenAI, LangChain, and Streamlit. It uses public APIs to provide conversational answers about weather, tourist attractions, currency exchange, visa requirements, flights, restaurants, and more – all in natural language.

---

## 🚀 Features

- 🧠 Conversational AI interface (Streamlit + LangChain)
- 🌦️ Weather forecast via WeatherAPI
- 🗺️ Top sights using OpenTripMap
- 💱 Live currency conversion via ExchangeRate API
- 📖 Wikipedia-based fact summaries
- ✈️ Flight search via Kiwi Tequila API
- 🛂 Visa information lookup
- 🍽️ Restaurant suggestions using OpenTable or mock data
- 🧱 Easy extension with new tools (Hotel prices, beach finder, etc.)

---

## 🐳 How to Run with Docker

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/travel-ai-agent.git
   cd travel-ai-agent
   ```

2. **Create a `.env` file**

   See the example below under [Environment Variables](#-environment-variables).

3. **Build and run**

   ```bash
   docker-compose up --build
   ```

4. **Visit in your browser**

   ```
   http://localhost:8501
   ```

---

## 🐍 How to Run Locally (Python)

1. **Create virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install requirements**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**

   Create a `.env` file as shown below.

4. **Run the app**

   ```bash
   streamlit run app.py
   ```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=sk-...
WEATHER_API_KEY=...
OPENTRIP_API_KEY=...
EXCHANGE_API_KEY=...
KIWI_API_KEY=...
```

Optional additional keys if you expand further:

```env
YELP_API_KEY=...
BOOKING_API_KEY=...
```

> Note: Some tools will fallback to mock data if the key is missing.

---

## 📁 Project Structure

```
travel-ai-agent/
├── app.py                # Streamlit UI
├── agent.py              # LangChain agent logic
├── tools/                # All external tools
│   ├── weather_tool.py
│   ├── tripmap_tool.py
│   ├── exchange_tool.py
│   ├── wikipedia_tool.py
│   ├── flight_tool.py
│   ├── visa_tool.py
│   └── restaurant_tool.py
├── .env                  # Environment variables (not committed)
├── requirements.txt
└── docker-compose.yml
```

---

## 💬 Example Prompts

- “What’s the weather in Gdańsk tomorrow?”
- “Top 3 attractions in Barcelona”
- “How much is 2 EUR in PLN?”
- “Do I need a visa for the USA?”
- “Find flights from Warsaw to Rome on 2025-08-10”
- “Best Italian restaurants in Prague?”

---

## 🧱 Adding More Tools

To extend the agent:

1. Create a new file in `tools/` with your function
2. Use `@tool(...)` decorator or define a `Tool(...)` in `agent.py`
3. Add to the `tools` list during `initialize_agent(...)`

Ideas for new tools:
- 🏨 HotelPriceTool (Booking, Expedia)
- 🏥 HealthAdvisoryTool
- 🏖️ BeachFinderTool
- 🧭 RoutePlannerTool

---

## ✅ Requirements

- Python 3.9+
- Docker (optional but recommended)
- OpenAI API key (required)
- Additional API keys depending on tools

---

## 📄 License

MIT License © 2025 by Łukasz Sędek
