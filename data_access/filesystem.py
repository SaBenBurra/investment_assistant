import json
import os
from datetime import datetime, timedelta


def get_stock_data_from_json(stock_code):
    with open("datas/pair_all_data.json", "r") as file:
        all_data = json.load(file)

    for data in all_data:
        if data["symbol"] == stock_code:
            return data


def cache_stock(stock):
    path = "datas/stock_cache.json"
    with open(path, "a+") as file:
        file.seek(0)
        content = file.read()
        if len(content) == 0:
            file.close()

    file = open(path, "r")
    if os.path.getsize(path) == 0:
        cached_data = []
    else:
        cached_data = json.load(file)
    file.close()

    i = 0
    for data in cached_data:
        if data["data"]["symbol"] == stock.symbol:
            del cached_data[i]
        i = i + 1

    cached_data.append({"time": str(datetime.now()), "data": stock.__dict__})
    json_data = json.dumps(cached_data)
    file = open(path, "w")
    file.write(json_data)
    file.close()


def get_stock_from_cache_if_exists(symbol):
    path = "datas/stock_cache.json"
    if not os.path.exists(path):
        return False
    with open(path, "r") as file:
        all_data = json.load(file)

    for data in all_data:
        if data["data"]["symbol"] == symbol.upper():
            cache_time = datetime.strptime(data["time"], "%Y-%m-%d %H:%M:%S.%f")
            if (datetime.now() - cache_time) > timedelta(minutes=30):
                return False
            return data["data"]
    return False


def get_all_stock_data():
    file = open("datas/pair_all_data.json", "r")
    all_data = json.load(file)
    return all_data
