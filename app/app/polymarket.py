import requests


POLYMARKET_API = "https://gamma-api.polymarket.com/markets"


def get_markets():
    try:
        response = requests.get(POLYMARKET_API, timeout=10)
        response.raise_for_status()
        return response.json()

    except Exception as e:
        print("Error getting markets:", e)
        return []


def get_active_markets(limit=20):
    markets = get_markets()

    active = []

    for market in markets:
        if market.get("active"):
            active.append({
                "question": market.get("question"),
                "yes_price": market.get("outcomePrices"),
                "volume": market.get("volume"),
                "end_date": market.get("endDate")
            })

    return active[:limit]


if __name__ == "__main__":
    markets = get_active_markets()

    for m in markets:
        print("----------------")
        print(m["question"])
        print("Prices:", m["yes_price"])
