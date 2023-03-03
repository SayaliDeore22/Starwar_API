from resource.base import ResourceBase
from utils.fetch_data import hit_url
from typing import Dict, List
import requests


class Films(ResourceBase):
    """
    Film class related functionality https://swapi.dev/
    """

    def __init__(self) -> None:
        super().__init__()
        self.relative_url = "/api/films"

    def get_count(self):
        complete_url = self.home_url + self.relative_url
        response = hit_url(complete_url)
        data = response.json()
        count = data.get("count")
        return count

    def get_sample_data(self, id_: int = 1) -> Dict:

        absolute_url = self.home_url + self.relative_url + f"/{id_}"
        response = hit_url(absolute_url)
        data = response.json()
        return data

    def get_resource_urls(self) -> List:
        data_ = []
        complete_url = self.home_url + self.relative_url
        response = hit_url(complete_url)
        data = response.json()
        url = data.get("results")
        for data in url:
            data_.append(data["url"])

        return data_












