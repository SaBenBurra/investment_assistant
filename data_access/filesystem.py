import json


def get_stock_data_from_json(stock_code):
    with open("datas/pair_all_data.json", "r") as file:
        all_data = json.load(file)

    for data in all_data:
        if data["symbol"] == stock_code:
            return data
