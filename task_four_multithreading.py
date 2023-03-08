from multiprocessing.pool import ThreadPool
from pydantic import parse_obj_as
from typing import List


from resource.r_films import Films               # resource model
from models.datamodels.py_films import Film_      # pydantic model
from models.datamodels.py_characters import Character_
from models.datamodels.py_planets import Planet_
from models.datamodels.py_starships import StarShip_
from models.datamodels.py_vehicles import Vechicle_
from models.datamodels.py_species import Species_

from dal.db_conn_helper import get_db_conn
from dal.dml import insert_resource
from utils.fetch_data import hit_url, fetch_data_json
from utils.timing import timeit


@timeit
def store_characters():
    characters = film_data.characters
    characters_data = []

    char_columns = [
        "name",
        "height",
        "mass",
        "hair_color"
    ]

    for character in characters:
        response = hit_url(character)
        char = response.json()
        char = Character_(**char)
        char_values = [
            char.name,
            char.height,
            char.mass,
            char.hair_color
        ]

        char_id = int(character.split("/")[-2])
        result = insert_resource(
            "characters",
            "char_id",
            char_id,
            char_columns,
            char_values
        )
        characters_data.append(char)
    return characters_data


@timeit
def store_planets():
    planets = film_data.planets
    planets_data = []

    planet_columns = [
        "name",
        "climate",
        "diameter",
        "gravity"
    ]

    for planet in planets:
        response = hit_url(planet)
        plan_ = response.json()
        plan_ = Planet_(**plan_)
        planet_values = [
            plan_.name,
            plan_.climate,
            plan_.diameter,
            plan_.gravity
        ]
        planet_id = int(planet.split("/")[-2])
        result = insert_resource(
            "planet",
            "planet_id",
            planet_id,
            planet_columns,
            planet_values
        )
        planets_data.append(plan_)
    return planets_data


@timeit
def store_starships():
    starships = film_data.starships
    starships_data = []

    starship_column = [
        "name",
        "MGLT",
        "cargo_capacity",
        "consumables",
        "hyperdrive_rating"
    ]
    for starship in starships:
        response = hit_url(starship)
        star_ = response.json()
        star_ = StarShip_(**star_)
        starship_values = [
            star_.name,
            star_.MGLT,
            star_.cargo_capacity,
            star_.consumables,
            star_.hyperdrive_rating
        ]
        starship_id = int(starship.split("/")[-2])
        result = insert_resource(
            "starship",
            "starship_id",
            starship_id,
            starship_column,
            starship_values
        )

        starships_data.append(star_)
    return starships_data



@timeit
def store_vehicle():
    vehicles = film_data.vehicles
    vehicles_data = []

    vehicle_column = [
        "name",
        "model",
        "consumables",
        "cost_in_credits",
        "manufacturer"
    ]
    for vehicle in vehicles:
        response = hit_url(vehicle)
        veh_ = response.json()
        veh_ = Vechicle_(**veh_)
        vehicle_values = [
            veh_.name,
            veh_.model,
            veh_.consumables,
            veh_.cost_in_credits,
            veh_.manufacturer
        ]
        vehicle_id = int(vehicle.split("/")[-2])
        result = insert_resource(
            "vehicle",
            "vehicle_id",
            vehicle_id,
            vehicle_column,
            vehicle_values
        )

        vehicles_data.append(veh_)
    return vehicles_data


@timeit
def store_species():
    species = film_data.species
    species_data = []

    species_column = [
        "name",
        "average_height",
        "average_lifespan",
        "designation",
        "eye_colors"
    ]

    for specie in species:
        response = hit_url(specie)
        specie_ = response.json()
        specie_ = Species_(**specie_)
        species_value = [
            specie_.name,
            specie_.average_height,
            specie_.average_lifespan,
            specie_.designation,
            specie_.eye_colors
        ]

        species_id = int(specie.split("/")[-2])
        result = insert_resource(
            "species",
            "species_id",
            species_id,
            species_column,
            species_value
        )

        species_data.append(specie_)
    return species_data


if __name__ == "__main__":
    data = Films().get_sample_data(id_=1)
    film_data = Film_(**data)

    # create DB connection
    conn = get_db_conn()

    film_columns = [
        "title",
        "opening_crawl",
        "director",
        "producer",
        "release_date",
        "created",
        "edited",
        "url",
    ]

    film_values = [
        film_data.title,
        film_data.opening_crawl,
        film_data.director,
        film_data.producer,
        film_data.release_date,
        film_data.created.strftime("%y-%m-%d"),
        film_data.edited.strftime("%y-%m-%d"),
        film_data.url,
    ]

    result = insert_resource(
        "film", "film_id", film_data.episode_id, film_columns, film_values
    )

    pool = ThreadPool(5)

    characters = film_data.characters
    characters_list = pool.map(fetch_data_json, characters)
    char = parse_obj_as(List[Character_], characters_list)

    planets = film_data.planets
    planets_list = pool.map(fetch_data_json, planets)
    plan = parse_obj_as(List[Planet_], planets_list)

    starships = film_data.starships
    starships_list = pool.map(fetch_data_json, starships)
    star = parse_obj_as(List[StarShip_], starships_list)

    vehicles = film_data.vehicles
    vehicles_list = pool.map(fetch_data_json, vehicles)
    veh = parse_obj_as(List[Vechicle_], vehicles_list)

    species = film_data.species
    species_list = pool.map(fetch_data_json, species)
    specie = parse_obj_as(List[Species_], species_list)


    character_data = store_characters()
    planets_data = store_planets()
    starship_data = store_starships()
    vehicles_data = store_vehicle()
    species_data = store_species()

