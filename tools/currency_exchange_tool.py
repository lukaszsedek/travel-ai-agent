import requests

def get_exchange_rate(query):
    try:
        parts = query.upper().split("TO")
        if len(parts) != 2:
            return "❌ Format should be like 'USD to EUR' or 'PLN to NOK'"

        from_currency = parts[0].strip()
        to_currency = parts[1].strip()
        url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}"

        response = requests.get(url)
        data = response.json()

        if data.get("success"):
            rate = data["result"]
            return f"💱 1 {from_currency} = {rate:.4f} {to_currency}"
        else:
            return "❌ Failed to retrieve exchange rate."
    except Exception as e:
        return f"❌ Error: {str(e)}"
