"""
This module defines pydantic (provides Py3 data-classes validation out of the box) models used
for validation and (de)serialization in API requests/responses.
"""
from models.basemodel import Base
from typing import List, Optional

class Species_(Base):
    """
        Pydantic model class meant to validate the data for `Species` object from
        single resource endpoint from starwars API.
    """

    average_height: str
    average_lifespan: str
    classification: str
    designation: str
    eye_colors: str
    hair_colors: str
    homeworld: Optional[str]
    language: str
    name: str
    skin_colors: str

    people: Optional[List[str]]
    films: Optional[List[str]]


if __name__ == "__main__":
    data = {
        "name": "Wookie",
        "classification": "mammal",
        "designation": "sentient",
        "average_height": "210",
        "skin_colors": "gray",
        "hair_colors": "black, brown",
        "eye_colors": "blue, green, yellow, brown, golden, red",
        "average_lifespan": "400",
        "homeworld": "https://swapi.dev/api/planets/14/",
        "language": "Shyriiwook",
        "people": [
            "https://swapi.dev/api/people/13/",
            "https://swapi.dev/api/people/80/"
        ],
        "films": [
            "https://swapi.dev/api/films/1/",
            "https://swapi.dev/api/films/2/",
            "https://swapi.dev/api/films/3/",
            "https://swapi.dev/api/films/6/"
        ],
        "created": "2014-12-10T16:44:31.486000Z",
        "edited": "2014-12-20T21:36:42.142000Z",
        "url": "https://swapi.dev/api/species/3/"
    }

    obj = Species_(**data)
    print(obj)
    breakpoint()