import allure
from test_api_tyazhova.endpoints.endpoint import Endpoint
import requests


class GetPosts(Endpoint):
    @allure.step("Get all posts")
    def get_all_posts(self):
        self.response = requests.get(self.url, headers=self.headers)
        self.json = self.response.json()
