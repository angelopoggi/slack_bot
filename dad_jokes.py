import requests
from config import DAD_API

def dad_jokes():
    url = "https://dad-jokes.p.rapidapi.com/random/joke"

    headers = {
        'x-rapidapi-host': "dad-jokes.p.rapidapi.com",
        'x-rapidapi-key': DAD_API
        }

    response = requests.request("GET", url, headers=headers)
    dadJokes = response.json()
    return dadJokes

if __name__ == '__main__':
    currentJoke = dad_jokes()
    print(currentJoke['body'][0]['setup'])
    print(currentJoke['body'][0]['punchline'])


