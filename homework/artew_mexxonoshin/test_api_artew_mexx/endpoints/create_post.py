import requests
import allure
from test_api_artew_mexx.endpoints.endpoint import Endpoint


class CreatePost(Endpoint):
    def __init__(self):
        super().__init__()
        self.object_id = None
        print(f"Инициализирован CreatePost, object_id: {self.object_id}")

    @allure.step("Создание нового (POST)")
    def create_new_post(self, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            self.url, json=body, headers=headers
        )
        self.json = self.response.json()
        self.object_id = self.json['id']
        print(f"Создан объект с ID: {self.object_id}")
        return self.response
