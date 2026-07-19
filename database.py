import json
import os

DATA_FILE = "artists.json"


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

            return {
                int(user_id): artists
                for user_id, artists in data.items()
            }

    return {}


def save_data(users_artists):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(
            users_artists,
            file,
            ensure_ascii=False,
            indent=4
        )