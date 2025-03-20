import requests
import allure

from test_api_artew_mexx.endpoints.endpoint import Endpoint


class DeleteObject(Endpoint):
    @allure.step("Выполнение DELETE-запроса для удаления объекта")
    def delete_object(self, object_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.delete(
            f"{self.url}/{object_id}", headers=headers
        )
        return self.response
