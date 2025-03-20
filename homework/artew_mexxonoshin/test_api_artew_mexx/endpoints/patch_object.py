import requests
import allure

from test_api_artew_mexx.endpoints.endpoint import Endpoint


class PatchObject(Endpoint):
    @allure.step("Выполнение PATCH-запроса для изменения объекта")
    def update_object_patch(self, object_id, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(
            f"{self.url}/{object_id}", json=body, headers=headers
        )
        self.json = self.response.json()
        return self.response
