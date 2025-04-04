import allure


class Endpoint:
    url = 'http://167.172.172.115:52353/object'
    response = None
    json = None
    headers = {"Content-type": "application/json"}

    @allure.step('Check that response is 200')
    def check_that_status_is_200(self):
        assert self.response.status_code == 200

    @allure.step('Check that name is the same as sent')
    def check_response_name_is_correct(self, expected_name):
        assert self.json['name'] == expected_name
