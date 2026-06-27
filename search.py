from datetime import datetime, timedelta
import yaml


def load_config():
    with open("config.yaml", "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def create_date_list(start_date, end_date):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")

    dates = []

    while start <= end:
        dates.append(start.strftime("%Y-%m-%d"))
        start += timedelta(days=1)

    return dates


def build_search_list():

    config = load_config()

    searches = []

    dates = create_date_list(
        config["search"]["start_date"],
        config["search"]["end_date"]
    )

    for origin in config["origins"]:

        for destination in config["destinations"]:

            for flight_date in dates:

                searches.append({

                    "origin": origin,

                    "destination": destination["airport"],

                    "city": destination["city"],

                    "date": flight_date,

                    "max_price": destination["max_price"]

                })

    return searches
