import os
from os.path import dirname, join


def fetch(day):
    import requests
    from dotenv import load_dotenv

    # Load session cookie from a file
    load_dotenv(join(dirname(__file__), '.env'))
    session_cookie = os.getenv("SESSION")

    url = f"https://adventofcode.com/2025/day/{day}/input"
    headers = {"Cookie": f"session={session_cookie}"}

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    with open(f"inputs/day{day:02d}.txt", "w") as f:
        f.write(response.text)


if __name__ == "__main__":
    # allow running this file directly to fetch a sample input
    fetch(1)