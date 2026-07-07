import time
import schedule

from polymarket import get_active_markets
from ai_engine import analyze_market
from email_alerts import send_alert


MIN_CONFIDENCE = 80


def scan_markets():

    print("Scanning Polymarket...")

    markets = get_active_markets(20)

    for market in markets:

        analysis = analyze_market(market)

        print("----------------")
        print(market["question"])
        print(analysis)

        # Send alerts for high-confidence opportunities
        if "Confidence score: 8" in analysis or "Confidence score: 9" in analysis:

            send_alert(
                "AlphaEdge Polymarket Alert",
                f"""
Market:
{market['question']}

AI Analysis:
{analysis}
"""
            )


schedule.every(30).minutes.do(scan_markets)


if __name__ == "__main__":

    print("AlphaEdge started")

    scan_markets()

    while True:
        schedule.run_pending()
        time.sleep(60)
