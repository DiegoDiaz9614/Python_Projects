import requests

STOCK_ENDPOINT = "https://www.alphavantage.co/query"

def get_closing_prices(symbol, api_key):
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": api_key
    }

    response = requests.get(STOCK_ENDPOINT, params=params)
    data = response.json()

    if "Time Series (Daily)" not in data:
        raise ValueError(f"Unexpected API response: {data}")

    time_series = data["Time Series (Daily)"]
    dates = list(time_series.keys())

    def get_close_price(data_index):
        date = dates[data_index]
        close_price = time_series[date]["4. close"]
        return date, close_price

    yesterday_date, yesterday_close = get_close_price(1)
    before_yesterday_date, before_yesterday_close = get_close_price(2)

    yesterday_close = float(yesterday_close)
    before_yesterday_close = float(before_yesterday_close)
    close_diff = ((yesterday_close - before_yesterday_close) / before_yesterday_close * 100)

    return {
        "yesterday_date": yesterday_date,
        "yesterday_close": yesterday_close,
        "before_yesterday_date": before_yesterday_date,
        "before_yesterday_close": before_yesterday_close,
        "close_diff": close_diff
    }
