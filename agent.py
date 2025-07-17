from dotenv import load_dotenv
from langchain.agents import initialize_agent, Tool
from langchain.chat_models import ChatOpenAI
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from tools.currency_exchange_tool import get_exchange_rate
from tools.weather_tool import get_weather
from tools.tripmap_tool import get_attractions
import datetime
import os
from datetime import datetime, timedelta
import re

load_dotenv(dotenv_path=".env", override=True)

chat_history = []

llm = ChatOpenAI(
    temperature=0,
    model="gpt-4o",
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

tools = [
    Tool(
        name="WeatherTool",
        func=lambda q: get_weather(q),
        description="Get weather forecast for a given city and date. Input format: 'City, YYYY-MM-DD'"
    ),
    Tool(
        name="AttractionsTool",
        func=lambda q: get_attractions(q),
        description="Get top tourist attractions in a given city. Input format: 'City'"
    ),
    Tool(
        name="WikipediaPL",
        func=WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper()),
        description="Useful for answering questions about well-known cities, landmarks, historical facts, and general knowledge."
    ),
    Tool(
       name="ExchangeRateTool",
        func=lambda q: get_exchange_rate(q),
        description="Get currency exchange rates. Input format: 'USD to EUR', 'PLN to GBP'"
    )
]

agent = initialize_agent(
    tools,
    llm,
    agent="chat-conversational-react-description",
    verbose=True,
    agent_kwargs={
        "system_message": "Jesteś pomocnym asystentem podróży. Zawsze odpowiadaj po polsku, używając uprzejmego i rzeczowego języka. Jeśli nie znasz odpowiedzi, powiedz to wprost, ale po polsku."
    }
)

def parse_user_input(user_input: str) -> str:
    # Domyślnie: jutro
    city = user_input
    date = (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d")

    # Spróbuj znaleźć miasto + datę tekstową
    match = re.search(r"(\w+)\s+(dziś|dzisiaj|jutro|\d{4}-\d{2}-\d{2})", user_input.lower())
    if match:
        city_raw, date_raw = match.groups()
        city = city_raw.capitalize()

        if date_raw in ["dziś", "dzisiaj"]:
            date = datetime.today().strftime("%Y-%m-%d")
        elif date_raw == "jutro":
            date = (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d")
        elif re.match(r"\d{4}-\d{2}-\d{2}", date_raw):
            date = date_raw

    return f"{city}, {date}"

def run_agent(user_input, chat_history):
    parsed_query = parse_user_input(user_input)

    try:
        result = agent.invoke({
            "input": parsed_query,
            "chat_history": chat_history
        })

        if isinstance(result, dict) and "output" in result:
            return result["output"]

        return str(result)

    except Exception as e:
        return f"❌ Agent failed: {str(e)}"


