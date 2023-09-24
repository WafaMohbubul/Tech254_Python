import random

import requests
import json

# Get the list of pokemon from the API
url = 'https://pokeapi.co/api/v2/pokemon/'
response = requests.get(url)
pokemon_list = json.loads(response.text)['results']

#Print all the pokemon names available
for pokemon in pokemon_list:
    print(pokemon['name'])

# Ask the user to choose a pokemon
print('Enter your pokemon:')


# Get the user's choice
choice = input().lower()

# Get the pokemon's data from the API
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(choice)
response = requests.get(url)
pokemon_data = json.loads(response.text)

# to get ability
abilities = pokemon_data['abilities'][0]
ability = abilities['ability']

# to format height and weight properly
height = int(pokemon_data['height'])
weight = int(pokemon_data['weight'])

height_formatted = height / 10
weight_formatted = weight / 10

# Print the pokemon's data of chosen one
print('Name: {}'.format(pokemon_data['name']))
print('Weight: {}'.format(weight_formatted) + "(kgs)")
print('Height: {}'.format(height_formatted) + "(m)")
print('Ability: {}'.format(ability['name']))

#CPU's pokemon choice
cpu_choice = random.choice(pokemon_list)
print("CPU Choice: ", cpu_choice['name'])

#print who is versing each other
print("ROUND 1: ", choice, "VS", cpu_choice['name'])

while True:
    #variables for random number generator between 1-6
    user_number = random.randint(1,6)
    computer_number = random.randint(1,6)

    #print numbers so we can see what numbers have been randomly generated
    print(choice, "played move number: ", user_number)
    print(cpu_choice['name'], "played move number: ", computer_number)

    #if conditions: whoever has the bigger number is the winner.
    #if user number is bigger, then they are the winner
    if user_number > computer_number:
        print(choice, "is the winner!")
        #exit loop is user is the winner
        break
    #if the numbers are the same, then it is a tie and DO NOT EXIT LOOP. Continue in the loop
    elif user_number == computer_number:
        print("It is a tie! Continue the game")
    #Only option left is if the computer number is larger which means the computer is the winner.
    else:
        print(cpu_choice['name'], "is the winner! Better luck next time")
        #if the computer number is larger, it has won so exit the loop
        break
