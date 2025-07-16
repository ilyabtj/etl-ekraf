import json
import pandas as pd


def transform():
    # baca raw.json
    with open("raw.json", "r", encoding="utf-8") as f:
        raw = json.load(f)
    data = raw["data"]

    df = pd.json_normalize(data)

    # drop kolom content & content_html
    for col in ["content_html", "content"]:
        if col in df.columns:
            df = df.drop(columns=[col])

    # flatten user (user_name, user_email)
    if "user" in df.columns:
        df["user_name"] = df["user"].apply(
            lambda x: x.get("name") if isinstance(x, dict) else None
        )
        df["user_email"] = df["user"].apply(
            lambda x: x.get("email") if isinstance(x, dict) else None
        )
        df = df.drop(columns=["user"])

    # kita gabung categories: ambil "title", gabung pake "|"
    if "categories" in df.columns:
        df["categories"] = df["categories"].apply(
            lambda x: (
                "|".join([cat.get("title", "") for cat in x])
                if isinstance(x, list)
                else ""
            )
        )

    # gabung tags: ambil "name", gabung pake "|"
    if "tags" in df.columns:
        df["tags"] = df["tags"].apply(
            lambda x: (
                "|".join([tag.get("name", "") for tag in x])
                if isinstance(x, list)
                else ""
            )
        )

    # Save ke CSV
    df.to_csv("ekraf_posts.csv", index=False)
    print("transform sukses dan saved as ekraf_posts.csv")


if __name__ == "__main__":
    transform()
