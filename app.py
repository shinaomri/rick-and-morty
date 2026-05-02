
from flask import Flask, jsonify
import requests
import time

app = Flask(__name__)

def fetch_characters():
    results = []
    url = "https://rickandmortyapi.com/api/character"

    while url:
        response = requests.get(url)
        
        if response.status_code != 200:
            break

        data = response.json()

        for character in data["results"]:
            is_human = character["species"] == "Human"
            is_alive = character["status"] == "Alive"
            is_from_earth = "Earth" in character["origin"]["name"]

            if is_human and is_alive and is_from_earth:
                results.append({
                    "Name": character["name"],
                    "Location": character["location"]["name"],
                    "Image": character["image"]
                })

        url = data["info"]["next"]
        time.sleep(0.5)

    return results

# Cache the data when app starts
characters_cache = fetch_characters()

@app.route("/healthcheck")
def healthcheck():
    return jsonify({"status": "ok"})

@app.route("/characters")
def get_characters():
    return jsonify(characters_cache)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)