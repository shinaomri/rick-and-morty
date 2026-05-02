import requests
import csv
import time  # ADD THIS

def fetch_characters():
    results = []
    url = "https://rickandmortyapi.com/api/character"

    while url:
        response = requests.get(url)
        
        if response.status_code != 200:
            print(f"❌ API call failed with status {response.status_code}")
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
        time.sleep(0.5)  # ADD THIS - wait half a second between pages

    return results

def save_to_csv(characters, filename="characters.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["Name", "Location", "Image"])
        writer.writeheader()
        writer.writerows(characters)

    print(f"✅ Saved {len(characters)} characters to {filename}")

if __name__ == "__main__":
    characters = fetch_characters()
    save_to_csv(characters)
