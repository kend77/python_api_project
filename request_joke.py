import requests


def request_joke(term):
    url = "https://icanhazdadjoke.com/search"
    response = requests.get(
        url,
        headers={"accept": "application/json"},
        params={"term": term}
    )
    return response
