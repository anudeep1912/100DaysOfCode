import requests
from datetime import date, timedelta
from twilio.rest import Client

STOCK = "MSFT"
COMPANY_NAME = "Tesla inc"
TODAY = date.today()
YESTERDAY = (date.today() - timedelta(1)).isoformat()
DAY_BEFORE = (date.today() - timedelta(2)).isoformat()


def check_stock_deviation():
    """Checks if the given stock price is increases/decreases by 5%."""
    # STEP 1: Use https://www.alphavantage.co
    # When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
    stock_end_point = "https://www.alphavantage.co/query"
    api_key = "LOJ3IISNINEK9WXG"
    stock_parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": api_key,
    }

    stock_response = requests.get(url=stock_end_point, params=stock_parameters)
    stock_data = stock_response.json()["Time Series (Daily)"]
    ltp_yesterday = float(stock_data[YESTERDAY]["4. close"])
    ltp_day_before = float(stock_data[DAY_BEFORE]["4. close"])

    if abs(ltp_day_before - ltp_yesterday) / ltp_day_before > 0.05:
        return True, ltp_day_before < ltp_yesterday, abs(ltp_day_before - ltp_yesterday) / ltp_day_before
    return False


def extract_news():
    """Extracts news of the define COMPANY and returns all the news arcticle's for last 2 days"""
    # STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    news_api_key = "fda770e95b6f41308f3efd182c670f5c"
    news_api_endpoint = "https://newsapi.org/v2/everything"
    news_parameters = {
        "q": COMPANY_NAME,
        "from": DAY_BEFORE,
        "to": TODAY,
        "sortBy": "popularity",
        "apikey": news_api_key
    }

    news_response = requests.get(url=news_api_endpoint, params=news_parameters)
    news_articles = news_response.json()["articles"][:3]
    return news_articles


# STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.
twilio_sid = ""
twilio_auth = ""
is_changed = check_stock_deviation()

if is_changed:
    if is_changed[1]:
        symbol = "🔺"
    else:
        symbol = "🔻"

    extracted_news = extract_news()
    client = Client(twilio_sid, twilio_auth)
    message = client.messages \
        .create(
            body=f"TSLA: {symbol}{is_changed[2]*100}%\nHeadline: {extracted_news[0]['title']}\n"
                 f"Brief: {extracted_news[0]['description']}\n URL: {extracted_news[0]['url']}\n"
                 f"\n"
                 f"Headline: {extracted_news[1]['title']}\nBrief: {extracted_news[1]['description']}\n"
                 f"URL: {extracted_news[1]['url']}",
            from_="+13166616433",
            to=""
        )
    print(message.status)


