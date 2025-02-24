import requests
from tinydb import TinyDB
from datetime import datetime
import time


def extract_btc_data():

    url = "https://api.coinbase.com/v2/prices/spot"
    params = {"currency": "USD"}

    response = requests.get(url, params=params)
    data = response.json()["data"]
    return data


def transform_btc_data(data):
    value = data["amount"]
    cryptocurrency = data["base"]
    currency = data["currency"]
    timestamp = datetime.now().timestamp()

    transformed_data = {
        "value": value,
        "cryptocurrency": cryptocurrency,
        "currency": currency,
        "timestamp": timestamp,
    }
    return transformed_data


def load_btc_data_into_TinyDB(data, db_name="btc.json"):

    db = TinyDB(db_name)
    db.insert(data)
    print("Data Sucesfully Saved!")


if __name__ == "__main__":

    while True:

        json_data = extract_btc_data()
        transformed_data = transform_btc_data(json_data)
        load_btc_data_into_TinyDB(transformed_data)
        time.sleep(15)