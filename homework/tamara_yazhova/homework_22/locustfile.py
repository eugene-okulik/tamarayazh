from locust import task, HttpUser


class ObjectUser(HttpUser):
    id = None
    headers = {"Content-type": "application/json"}

    def on_start(self):
        body = {
            "name": "Second object",
            "data": {
                "color": "red",
                "size": "small"
            },
        }
        response = self.client.post('/object', json=body, headers=self.headers)
        self.id = response.json().get('id')

    @task(1)
    def get_all_objects(self):
        self.client.get('/object', headers=self.headers)

    @task(3)
    def get_one_object(self):
        self.client.get(f'/object/{self.id}', headers=self.headers)

    def on_stop(self):
        self.client.delete(f'/object/{self.id}', headers=self.headers)
