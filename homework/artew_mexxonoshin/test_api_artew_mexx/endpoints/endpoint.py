import allure
import requests


class Endpoint:
    url = 'http://167.172.172.115:52353/object'
    response = None
    json= None
    headers = {'Content-Type': 'application/json'}

    @allure.step("Проверка статус-кода и вывод результата")
    def check_that_status_is_200(self):
        print(f"Получен статус код: {self.response.status_code}")
        print(f"Тело ответа: {self.response.text}")
        assert self.response.status_code == 200, (
            f'Ожидаемый результат:'
            f'Статус код 200 Фактический результат: {self.response.status_code}'
        )
