import allure
import requests
from .final_endpoint import FinalEndpoint


class PostMem(FinalEndpoint):
    @allure.step("Добавление нового мема")
    def create_meme(self, text: str, url: str, tags: list, info: dict):
        meme_data = {
            "text": text,
            "url": url,
            "tags": tags,
            "info": info
        }
        self.response = requests.post(
            f"{self.base_url}/meme",
            json=meme_data,
            headers=self.headers
        )
        return self.response

    def create_fail_meme(self, **meme_data):
        """
        POST /meme - создание нового мема с ожидаемой ошибкой
        Принимает параметры как именованные аргументы или словарь
        """
        self.response = requests.post(
            f"{self.base_url}/meme",
            json=meme_data,
            headers=self.headers
        )
        return self.response
