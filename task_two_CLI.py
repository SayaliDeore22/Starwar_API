"""
The task 2 goes like following:
Pull data for  the first movie in star wars
Write the json data into a file named output.txt

SUBTASKS -
1. Output should be only list of names (first name & last name) of characters
in the movie.
2. Output should only print list of planet names used in the movie
3. Output should only print list of vehicle names used in the movie.

"""

import json
import requests
import argparse

from pprint import pprint
from typing import Dict, List

from utils.fetch_data import hit_url

FIRST_FILM_URL = "https://swapi.dev/api/films/1/"


def write_data_into_file(data: Dict) -> None:
    """write dict data into file"""

    with open("output.txt", "w") as fp:
        fp.write(json.dumps(data))       #dict to str conversion (serialization)


def get_data() -> Dict:
    """Returns a dict object from swapi.dev/api/films/1"""
    response = requests.get(FIRST_FILM_URL)
    result_ = response.json()
    write_data_into_file(result_)
    return result_


def main(data_: Dict) -> List:
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--resourse', default="characters", choices=["characters", "starships", "species",
                                                                          "vehicles", "planets"])
    args = parser.parse_args()
    print(args)
    resource_ = data_.get(args.resourse)

    names = []
    for res in resource_:
        resource_data = hit_url(res)
        resource_data = resource_data.json()
        names.append(resource_data.get("name"))
    return names



if __name__ == "__main__":
    result = get_data()
    print(result)
    main(result)

