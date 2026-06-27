import yaml
from pathlib import Path


CONFIG_FILE = Path("config.yaml")


def load_config():
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def main():

    config = load_config()

    print("=" * 50)
    print("Flight Tracker Started")
    print("=" * 50)

    print()

    print("Origins:")

    for airport in config["origins"]:
        print("-", airport)

    print()

    print("Destinations")

    for city in config["destinations"]:

        print(
            city["city"],
            city["airport"],
            city["max_price"]
        )


if __name__ == "__main__":
    main()
