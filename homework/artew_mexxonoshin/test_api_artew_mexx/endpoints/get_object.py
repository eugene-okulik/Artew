import requests
import allure

from test_api_artew_mexx.endpoints.endpoint import Endpoint


class GetObject(Endpoint):
    @allure.step("Получение списка всех объектов (GET)")
    def get_all_object(self):
        self.response = requests.get(self.url)
        return self.response
