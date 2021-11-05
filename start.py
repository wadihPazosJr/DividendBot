import requests
import json
import datetime

#What about holidays?


def get_right_end_date(date):
    #Make date object based off date string
    init_date = datetime.datetime.strptime(date, "%Y-%m-%d")
    weekday = init_date.weekday()
    print(weekday)
    result_date = ""

    if weekday <=2:
        result_date = init_date + datetime.timedelta(days=2)
    else:
        result_date = init_date + datetime.timedelta(days=4)

    return str(result_date)[:10]

def get_right_start_date(date):
    init_date = datetime.datetime.strptime(date, "%Y-%m-%d")
    weekday = init_date.weekday()
    print(weekday)
    result_date = ""

    if weekday >= 2:
        result_date = init_date - datetime.timedelta(days=2)
    else:
        result_date = init_date - datetime.timedelta(days=4)

    return str(result_date)[:10]

def get_start_date(dividends, year):
    counter = 0
    while int(dividends[counter]["exDate"][:4]) != year:
        counter+=1
    return dividends[counter - 1]["exDate"]

stock_ticker = input("Enter Stock Ticker Symbol: \n")

stock_dividends = requests.get("https://api.polygon.io/v2/reference/dividends/" + stock_ticker, headers={"Authorization": "Bearer YSB3smcV7460ocSpES4mSWvV0c7JovD1"}).json()

end_date = get_right_end_date(stock_dividends["results"][0]["exDate"])

start_date = get_right_start_date(get_start_date(stock_dividends["results"], int(end_date[:4]) - 5))

aggregate_params = {
    "stocksTicker": stock_ticker,
    "multiplier": "30",
    "timespan": "minute",
    "from": start_date,
    "to": end_date,
    "sort": "desc",
    "limit": "30000"
}
print(start_date)
print(end_date)

prices = requests.get(f"https://api.polygon.io/v2/aggs/ticker/{stock_ticker}/range/30/minute/{start_date}/{end_date}?sort=desc&limit=30000", headers={"Authorization": "Bearer YSB3smcV7460ocSpES4mSWvV0c7JovD1"})
json_price = prices.json()
print(json.dumps(json_price, indent=4))














