from pprint import pprint
import argparse

from utils.randgen import ProduceChars
from utils.fetch_data import hit_url
from task_one import get_url

from resource.r_films import Films
from resource.r_planets import Planets
from resource.r_starships import Starships
from resource.r_characters import Characters
from resource.r_species import Species
from resource.r_vehicles import Vehicles

# pydentic classes
from models.datamodels.py_films import Film_
from models.datamodels.py_planets import Planet_
from models.datamodels.py_species import Species_
from models.datamodels.py_characters import Character_
from models.datamodels.py_starships import StarShip_
from models.datamodels.py_vehicles import Vechicle_


def Film_data():
    film_object = Films()
    total_films = film_object.get_count()
    print(f"Total films: {total_films}")
    film_data = film_object.get_sample_data()
    film_data = Film_(**film_data)
    print(f"Film data : {film_data}")
    film_url = film_object.get_resource_urls()
    print(f"Film url : {film_url}")
    print()

def Starship_data():
    starships_object = Starships()
    total_starships = starships_object.get_count()
    print(f"Total starships: {total_starships}")
    starships_data = starships_object.get_sample_data(id_= 9)
    starships_data = StarShip_(**starships_data)
    print(f"Starship data : {starships_data}")
    starship_url = starships_object.get_resource_urls()
    print(f"Starship url : {starship_url}")
    print()


def Planet_data():
    planet_object = Planets()
    total_planets = planet_object.get_count()
    print(f"Total planets: {total_planets}")
    planet_data = planet_object.get_sample_data()
    planet_data = Planet_(**planet_data)
    print(f"Planet data : {planet_data}")
    planet_url = planet_object.get_resource_urls()
    print(f"Planet url : {planet_url}")
    print()


def Characters_data():
    characters_object = Characters()
    total_characters = characters_object.get_count()
    print(f"Total characters : {total_characters}")
    characters_data = characters_object.get_sample_data()
    characters_data = Character_(**characters_data)
    print(f"Character data : {characters_data}")
    character_url = characters_object.get_resource_urls()
    print(f"Character Url : {character_url}")
    print()


def Species_data():
    species_object = Species()
    total_species = species_object.get_count()
    print(f"Total species : {total_species}")
    species_data = species_object.get_sample_data(id_=3)
    species_data = Species_(**species_data)
    print(f"Species data : {species_data}")
    species_url = species_object.get_resource_urls()
    print(f"Species url : {species_url}")
    print()


def Vehicle_data():
    vehicle_object = Vehicles()
    total_vehicle = vehicle_object.get_count()
    print(f"Total vehicle : {total_vehicle}")
    vehicle_data = vehicle_object.get_sample_data()
    vehicle_data = Vechicle_(**vehicle_data)
    print(f"Vehicle data : {vehicle_data}")
    vehicle_url = vehicle_object.get_resource_urls()
    print(f"Vehicle url : {vehicle_url}")
    print()


def main():
    Film_data()
    Starship_data()
    Species_data()
    Vehicle_data()
    Characters_data()
    Planet_data()


def random_data():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--limit", default=3, type=int)
    parser.add_argument("-s", "--start", default=1, type=int)
    parser.add_argument("-e", "--end", default=82, type=int)
    parser.add_argument("-r", "--resource", default="films", choices=["people", "planets", "starships",
                                                                     "species", "vehicles", "films"])

    args = parser.parse_args()
    print(f"arguments are {args}")

    obj = ProduceChars(args.start, args.end, args.limit)
    resource = [element for element in obj]
    content = []
    for item in resource:
        print(f"Items are {item}")
        response_url = get_url(args.resource, item)
        response_ = hit_url(response_url)
        data = response_.json()
        content.append(data)
        pprint(content)


if __name__ == "__main__":
    main()
    random_data()
