# Who's in space? From Exercises for Programmers.


import urllib.request
import json


API_ENDPOINT = "http://api.open-notify.org/astros.json"


def fetch_astros():
    """ Fetch details of who is in space from the API."""
    response = urllib.request.urlopen(API_ENDPOINT)
    lines = response.readlines()
    decoded_line = bytes.decode(lines[0])
    return json.loads(decoded_line)


def show_people(people):
    """Print out a table on std output of each person in space."""
    longest_name_length = max([len(p["name"]) for p in people])
    print(f"{'Name':<{longest_name_length}} | Craft")
    print("-" * (longest_name_length), end=" | ")
    print("-" * 5)
    for p in people:
        print(f"{p['name']:<{longest_name_length}} | {p['craft']}")


def main():
    data = fetch_astros()
    print(f"There are {data['number']} people in space right now:")
    show_people(data["people"])


if __name__ == "__main__":
    main()
