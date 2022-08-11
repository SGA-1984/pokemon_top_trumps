import random

import requests

def pokemon_card():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()

return {
    'name': pokemon['name'],
    'id': pokemon['id'],
    'height': pokemon['height'],
    'weight': pokemon['weight'],
    }

pokemon1 = (pokemon_card())
pokemon2 = (pokemon_card())
pokemon3 = (pokemon_card())

player_choice_pokemon = input(f"Would you like to choose {pokemon1['name']}, {pokemon2['name']} or {pokemon3['name']}?")

rounds=int(input("How many rounds would you like to play? Enter 1, 2 or 3"))

def run():
    print ("Welcome to Pokemon Top Trumps!")
    pokemon_capital = (player_choice_pokemon['name'][0].upper()) + (player_choice_pokemon['name'][1:])
    print('You chose{}'.format(pokemon_capital))
    stat_choice = input('Which stat do you want to use? (id, height, weight) ')

    opponent_pokemon = pokemon_card()
    oppo_pokemon_capital = (opponent_pokemon['name'][0].upper()) + (opponent_pokemon['name'][1:])
    print('The opponent chose {}'.format(oppo_pokemon_capital))

    my_stat = player_choice_pokemon[stat_choice]
    opponent_stat = opponent_pokemon[stat_choice]
    player_score = 0
    opponent_score = 0

    if my_stat > opponent_stat:
        player_score += 1
        print("You win! Your score is", player_score, "Opponent score is", opponent_score)
    elif my_stat < opponent_stat:
        opponent_score += 1
        print("You lose! Your score is", player_score, "Opponent score is", opponent_score)
    else:
        print("Draw! Your score is", player_score, "Opponent score is", opponent_score)

run()