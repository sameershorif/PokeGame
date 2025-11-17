import requests
import json
import random

# Get the list of pokemon from the API
url = 'https://pokeapi.co/api/v2/pokemon/'
response = requests.get(url)
pokemon_list = json.loads(response.text)['results']

print("Here are some Pokémon you can choose from:\n")
for pokemon in pokemon_list:
    print(pokemon['name'])

# Ask the user to choose a pokemon
print('\nEnter your pokemon:')

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

# Print the pokemon's data
print('Name: {}'.format(pokemon_data['name']))
print('Weight: {}'.format(weight_formatted) + "(kgs)")
print('Height: {}'.format(height_formatted) + "(m)")
print('Ability: {}'.format(ability['name']))


######### Random Pokemon assigned to CPU
print("\nThe CPU is choosing a Pokémon...")

random_id = random.randint(1, 386)

cpu_url = f'https://pokeapi.co/api/v2/pokemon/{random_id}/'
cpu_response = requests.get(cpu_url)
cpu_pokemon_data = json.loads(cpu_response.text)
cpu_name = cpu_pokemon_data['name']

print(cpu_pokemon_data['name'])
print(f"CPU Pokémon: {cpu_name}")

##### Battle

# to get ability
cpu_abilities = cpu_pokemon_data['abilities'][0]
cpu_ability = cpu_abilities['ability']

# to format height and weight properly
cpu_height = int(cpu_pokemon_data['height'])

cpu_height_formatted = cpu_height / 10

cpu_weight = int(cpu_pokemon_data['weight'])
cpu_weight_formatted = cpu_weight / 10

#these probably don't need to be printed until the user selects which stat to compare
#print('CPU Weight: {}'.format(cpu_weight_formatted) + "(kgs)")
#print('CPU Height: {}'.format(cpu_height_formatted) + "(m)")


#### User input of which stat they are wanting to compare
print('\nHeight [H], Weight [W]')

stat_compare = input("What stat are you wanting to compare?: 'H' or 'W' ").lower()

if stat_compare == 'h':
    print(f"\nYour Pokemons height is: {float(height_formatted)} (m) \nThe CPU's Pokemon height is {float(cpu_height_formatted)} (m)")
    if height > cpu_height:
        print("\nYou Win, \nyour pokemon is taller")
    elif height_formatted < cpu_height_formatted:
        print("\nYou Lose, \nyour pokemon is smaller")

if stat_compare == 'w':
    print(f"\nYour Pokemons weight is: {float(weight_formatted)} (kg) \nThe CPU's Pokemon weight is {float(cpu_weight_formatted)} (kg)")
    if weight_formatted > cpu_weight_formatted:
        print("\nYou Win, \n Your pokemon is heavier than the cpu's")
    elif weight_formatted < cpu_weight_formatted:
        print("\nYou Lose ,\n Your pokemon is lighter weight than the cpu's Pokemon weight")

