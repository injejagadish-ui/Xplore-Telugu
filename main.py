import os
import time
import requests

API_KEY = os.environ.get("GEMINI_API_KEY")


def generate_telugu_fact():

    if not API_KEY:
        raise ValueError("GEMINI_API_KEY is missing")

    model = "gemini-3.8-flash"

    url = (
        "https://generativelanguage.googleapis.com/"
        f"v1beta/models/{model}:generateContent"
    )

    prompt = """
    Write one interesting and scientifically accurate
    fact for a Telugu YouTube Shorts video.

    Language: Telugu.
    Duration: 30 seconds.

    Include:
    1. Powerful opening hook.
    2. Interesting explanation.
    3. Exciting ending.

    Return only the Telugu narration.
    """

    for attempt in range(3):

        try:
            response = requests.post(
                url,
                params={"key": API_KEY},
                json={
                    "contents": [
                        {
                            "parts": [
                                {"text": prompt}
                            ]
                        }
                    ]
                },
                timeout=90
            )

            if response.status_code == 503:
                print("Gemini server busy. Retrying...")
                time.sleep(15 * (attempt + 1))
                continue

            response.raise_for_status()

            data = response.json()

            script = data["candidates"][0]["content"]["parts"][0]["text"]

            with open("script.txt", "w", encoding="utf-8") as file:
                file.write(script)

            print("SUCCESS! Telugu script generated!")
            print(script)
            return

        except requests.exceptions.RequestException as error:
            print("API Error:", error)
            time.sleep(10)

    raise Exception("Gemini failed after 3 attempts.")


if __name__ == "__main__":
    generate_telugu_fact()
