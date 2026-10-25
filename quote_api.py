
import json
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

API_URL = "https://jsonplaceholder.typicode.com/todos/1"


def get_data():
    try:
        request = Request(
            API_URL,
            headers={"User-Agent": "Python-API-Project"}
        )

        with urlopen(request, timeout=10) as response:
            data = json.loads(response.read().decode("utf-8"))

        if not isinstance(data, dict) or "title" not in data:
            print("Error: Invalid API response.")
            return

        print("\n--- Python REST API Project ---")
        print("ID:", data.get("id"))
        print("Title:", data.get("title"))
        print("Completed:", data.get("completed"))

    except HTTPError as error:
        print("HTTP Error:", error.code)
    except URLError as error:
        print("Network Error:", error.reason)
    except TimeoutError:
        print("Request timed out. Try again.")
    except (json.JSONDecodeError, UnicodeDecodeError):
        print("Error: Invalid JSON response.")


def main():
    choice = input("Enter Y to fetch API data: ").strip().lower()

    if choice == "y":
        get_data()
    else:
        print("Invalid choice. Enter Y.")


if __name__ == "__main__":
    main()
