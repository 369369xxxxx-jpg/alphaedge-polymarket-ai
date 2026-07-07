
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def analyze_market(market):
    prompt = f"""
You are a prediction market analyst.

Analyze this Polymarket question:

{market['question']}

Current market data:
Price: {market['yes_price']}
Volume: {market['volume']}
Expiration: {market['end_date']}

Return:
1. Estimated probability of YES (0-100%)
2. Whether the market looks underpriced, overpriced, or fair
3. Confidence score (0-100)
4. Short explanation

Do not guarantee a win. Look for possible statistical edge.
"""

    try:
        response = client.chat.completions.create(
            model="gpt-5-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"AI error: {e}"
