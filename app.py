#pylint: disable=E1101

import pyfiglet
import clr
from random import choice
from request_joke import request_joke
from select_style import select_color

art = pyfiglet.figlet_format("Dad Joke 3000")
color = select_color()

selected_color = getattr(clr.bold, color)
art = selected_color(art)

print(art)


user_input = input("What type of joke do you want to hear? ")

response = request_joke(user_input)
results = response.json()["results"]


jokes = None
if len(results) > 1:
    jokes = "jokes"
elif len(results) > 0:
    joke = "joke"


if len(results) == 0:
    print(f"Sorry, I couldn\'t find a joke with your term: {user_input}")
else:
    random_result = choice(results)["joke"]
    print(
        f"I've got {len(results)} {jokes} about {user_input}. Here\'s one: \n{random_result} ")
