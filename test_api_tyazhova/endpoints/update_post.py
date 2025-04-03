import allure
import requests
from test_api_tyazhova.endpoints.endpoint import Endpoint


class UpdatePost(Endpoint):
    def __init__(self, url):
        self.url = url

    @allure.step("Update post with PUT")
    def update_post_put(self, post_id, body):
        self.response = requests.put(
            f'{self.url}/{post_id}', json=body, headers=self.headers
        )
        self.json = self.response.json()

    @allure.step("Update post with PATCH")
    def update_post_patch(self, post_id, body):
        self.response = requests.patch(
            f'{self.url}/{post_id}', json=body, headers=self.headers)
        self.json = self.response.json()
