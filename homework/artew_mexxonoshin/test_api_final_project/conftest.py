import pytest
from test_api_final_project.final_endpoints.auth import Auth
from test_api_final_project.final_endpoints.get_mem import GetMem
from test_api_final_project.final_endpoints.post_mem import PostMem
from test_api_final_project.final_endpoints.put_meme import PutMem
from test_api_final_project.final_endpoints.delete_meme import DeleteMem
from test_api_final_project.final_endpoints.core import CoreAPI

@pytest.fixture
def auth_client():
    """Фикстура для тестов авторизации"""
    client = Auth()
    yield client
    # Автоматическая очистка токена после теста
    client.headers.pop('Authorization', None)


@pytest.fixture
def mem_client():
    """Фикстура для работы с мемами"""
    client = GetMem()
    yield client
    # Автоматическая очистка токена после теста
    client.headers.pop('Authorization', None)


@pytest.fixture
def core_client():
    """Фикстура для системных эндпоинтов API"""
    client = CoreAPI()
    yield client


@pytest.fixture
def post_client():
    """Фикстура для создания мемов"""
    client = PostMem()
    yield client
    # Автоматическая очистка токена после теста
    client.headers.pop('Authorization', None)


@pytest.fixture
def put_client():
    """Фикстура для обновления мемов"""
    client = PutMem()
    yield client
    # Автоматическая очистка токена после теста
    client.headers.pop('Authorization', None)


@pytest.fixture()
def delete_client():
    """Фикстура для удаления мемов"""
    client = DeleteMem()
    yield client
    # Автоматическая очистка токена после теста
    client.headers.pop('Authorization', None)
