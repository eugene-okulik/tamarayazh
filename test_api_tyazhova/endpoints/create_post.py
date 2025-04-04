import requests
import allure
from test_api_tyazhova.endpoints.endpoint import Endpoint


class CreatePost(Endpoint):
    @allure.step('Create new post')
    def create_new_post(self, body):
        self.response = requests.post(
            self.url,
            json=body,
            headers=self.headers
        )
        self.json = self.response.json()
        return self.json["id"]
