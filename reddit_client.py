import requests as http
from datetime import datetime, timezone

REDDIT_SEARCH_URL = "https://www.reddit.com/search.json"
USER_AGENT = "monte-intel-bot/0.1 (market intelligence platform)"

def fetch(query: str, time_filter: str = "week", limit: int = 25) -> list:
    response = http.get(
        REDDIT_SEARCH_URL,
        headers={"User-Agent": USER_AGENT},
        params={
            "q": query,
            "sort": "relevance",
            "t": time_filter,
            "limit": limit,
            "type": "link",
        },
        timeout=15,
    )
    response.raise_for_status()
    return response.json().get("data", {}).get("children", [])
