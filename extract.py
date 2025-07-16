import json
import requests


def extract():
    url = "https://api.ekraf.go.id/posts"
    response = requests.get(url)
    data = response.json()
    with open("raw.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


print("data nya berhasil diextract ke raw.json")

if __name__ == "__main__":
    extract()
