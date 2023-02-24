"""
The task 2 goes like following:
Pull data for  the first movie in star wars
Write the json data into a file named output.txt

SUBTASKS -
1. Output should be only list of names (first name & last name) of characters
in the movie.
2. Output should only print list of planet names used in the movie
3. Output should only print list of vehicle names used in the movie.
4. Output should only print list of starship names used in movie.
"""

import json
import requests

from pprint import pprint
from typing import Dict, List

from utils.fetch_data import hit_url

FIRST_FILM_URL = "https://swapi.dev/api/films/1/"


def write_data_into_file(data: Dict) -> None:
    """write dict data into file"""

    with open("output.txt", "w") as fp:
        fp.write(json.dumps(data))       #dict to str conversion (serialization)


def first_task() -> Dict:
    """Returns a dict object from swapi.dev/api/films/1"""
    response = requests.get(FIRST_FILM_URL)
    result_ = response.json()
    write_data_into_file(result_)
    return result_


def second_task(data_: Dict) -> List:
    """pull data from swapi characters sequentially"""

    characters = data_.get("characters")  # returns None by default

    names = []
    for character in characters:
        character_data = hit_url(character)   #return response
        character_data = character_data.json()  #convetred into json that is dict
        names.append(character_data.get("name"))

    # names = []
    # all_characters = fetch_data(characters)
    # for character in all_characters:
    #     names.append(character.get("name"))

    return names


def third_task(data_: Dict) -> List:
    planets = data_.get("planets")
    names = []
    for planet in planets:
        planet_data = hit_url(planet)
        planet_data = planet_data.json()
        names.append(planet_data.get("name"))

    return names


def forth_task(data_: Dict) -> List:
    vehicles = data_.get("vehicles")
    names = []
    for vehicle in vehicles:
        vehicle_data = hit_url(vehicle)
        vehicle_data = vehicle_data.json()   # dict
        names.append(vehicle_data.get("name"))

    return names


def fifth_task(data_: Dict) -> List:

    starships = data_.get("starships")
    models = []
    for starship in starships:
        starships_data = hit_url(starship)
        starships_data = starships_data.json()
        models.append(starships_data.get("model"))

    return models


if __name__ == "__main__":

    # first task
    first_result = first_task()
    pprint(first_result)

    # second task
    second_result = second_task(first_result)
    pprint(second_result)

    # third task
    third_result = third_task(first_result)
    pprint(third_result)

    forth_result = forth_task(first_result)
    pprint(forth_result)

    fifth_result = fifth_task(first_result)
    print(fifth_result)

