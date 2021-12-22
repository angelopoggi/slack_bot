import random

def dad_jokes():
    jokeList = []
    with open('jokes.txt', 'r') as jokefile:
        for jokes in jokefile:
            jokeList.append(jokes)
        randomJoke = random.choice(jokeList)
        randomJoke = randomJoke.split('<>')
        return  randomJoke



if __name__ == '__main__':
    currentJoke = dad_jokes()
    print(currentJoke[0])
    print(currentJoke[1])


