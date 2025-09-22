import requests
import json

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

def get_news(company_name, api_key):
    params = {
        "q": company_name,
        "apiKey": api_key,
        "sortBy": "publishedAt",
    }

    response = requests.get(NEWS_ENDPOINT, params=params)

    if response.status_code != 200:
        print(f"Error fetching news: {response.status_code}")
        return []

    data = response.json()
    articles = data.get("articles", [])

    top_articles = []
    for article in articles[:3]:
        title = article.get("title")
        url = article.get("url")
        publishedAt = article.get("publishedAt")

        top_articles.append({
            "title": title,
            "url": url,
            "publishedAt": publishedAt
        })

    return top_articles
