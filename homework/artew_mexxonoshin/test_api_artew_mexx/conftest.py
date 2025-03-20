import pytest
from .endpoints.create_post import CreatePost
from .endpoints.get_object import GetObject
from .endpoints.put_object import PutObject
from .endpoints.patch_object import PatchObject
from .endpoints.delete_object import DeleteObject


@pytest.fixture
def create_post_endpoint():
    print("Создан новый экземпляр CreatePost")
    return CreatePost()

@pytest.fixture
def delete_object():
    return DeleteObject()

@pytest.fixture
def get_all_object():
    return GetObject()


@pytest.fixture
def unique_object_id(create_post_endpoint, delete_object):
    print("Фикстура object_id: начало")

    # Создаем новый объект
    body = {"name": "Artew", "data": {"color": "black&white", "size": "small"}}
    create_post_endpoint.create_new_post(body)
    object_id = create_post_endpoint.object_id  # Получаем ID созданного объекта
    print(f"Фикстура object_id: создан объект с ID {object_id}")

    # Возвращаем ID для использования в тестах
    yield object_id

    # Удаляем объект после завершения теста
    print(f"Фикстура object_id: удаление объекта с ID {object_id}")
    delete_object.delete_object(object_id)
    print("Фикстура object_id: завершено")

@pytest.fixture
def update_object_put():
    return PutObject()

@pytest.fixture
def update_object_patch():
    return PatchObject()

