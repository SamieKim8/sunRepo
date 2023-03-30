import random
import final_hangman as fh

fruits = [
    "apple",
    "banana",
    "blueberry",
    "raspberry",
    "peach",
    "plum",
    "pear",
    "orange",
    "grapes",
    "mango",
    "lemon",
    "strawberry",
    "grapefruit",
    "watermelon",
    "blackberry"
]

animals = [        
    "sheep",
    "deer",
    "rabbit",
    "zebra",
    "squirrel",
    "horse",
    "mouse",
    "elephant",
    "monkey",
    "lion",
    "tiger",
    "fox",
    "wolf",
    "raccoon",
    "kangaroo"
]

countries = [
    "india",
    "france",
    "germany",
    "brazil",
    "italy",
    "turkey",
    "spain",
    "vietnam",
    "australia",
    "argentina",
    "iran",
    "poland",
    "greece",
    "israel",
    "switzerland"
]

used_fruits = []
used_animals = []
used_countries = []

# get random word based on user topic
def get_random_word():

    topic = fh.user_topic()

    if topic == fruits or topic == "fruits":
        word = random.choice(fruits)
        used_fruits.append(word)
        fruits.remove(word)
        return word
    elif topic == animals or topic == "animals":
        word = random.choice(animals)
        used_animals.append(word)
        animals.remove(word)
        return word
    elif topic == countries or topic =="countries":
        word = random.choice(countries)
        used_countries.append(word)
        countries.remove(word)
        return word
    else:
        print("Something went wrong. Please try again.")
