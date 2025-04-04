import allure
from test_api_tyazhova.endpoints.endpoint import Endpoint
import requests


class DeletePost(Endpoint):
    @allure.step('Delete post')
    def delete_post(self, post_id):
        self.response = requests.delete(f'{self.url}/{post_id}', headers=self.headers)
