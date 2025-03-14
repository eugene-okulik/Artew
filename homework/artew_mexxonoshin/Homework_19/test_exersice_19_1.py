import requests
import pytest


# Фикстура для вывода сообщений перед и после всех тестов
@pytest.fixture(scope='session', autouse=True)
def session_fixture():
    print("\nStart testing")
    yield
    print("\nTesting completed")


# Фикстура для вывода сообщений перед и после каждого теста
@pytest.fixture(autouse=True)
def before_after_fixture():
    print("\nbefore test")
    yield
    print("\nafter test")


# Фикстура для добавления нового объекта
@pytest.fixture()
def new_post():
    body = {
        "name": "Artew",
        "data": {"color": "black&white", "size": "small"}
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://167.172.172.115:52353/object',
        json=body,
        headers=headers
    )
    if response.status_code == 200:
        print("Объект успешно добавлен! Для выполнения следующего метода PUT/PATCH")
        print("Ответ сервера:", response.json())
        object_id = response.json()['id']
        yield object_id
    else:
        print(f"Ошибка: {response.status_code}")
        print("Ответ сервера:", {response.text})

    delete_response = requests.delete(
        f'http://167.172.172.115:52353/object/{object_id}'
    )
    if delete_response.status_code == 200:
        print(f"\nОбъект с ID={object_id} успешно удалён после теста.")
    elif delete_response.status_code == 404:
        print(f"\nОбъект с ID={object_id} уже удалён")
    else:
        print(f"Ошибка при удалении объекта: {delete_response.status_code}\nОтвет сервера: {delete_response.text}")


def all_object():
    response = requests.get('http://167.172.172.115:52353/object')
    return response


def test_all_object():
    response = all_object()
    assert response.status_code == 200, f'Ожидаемый результат: Статус код 200 Фактический результат: {response.status_code}'
#    print("\nВыполнение GET запроса для получения полного списка объектов:")
#    print(response.json())


def add_object(body):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://167.172.172.115:52353/object',
        json=body,
        headers=headers
    )
    return response


@pytest.mark.parametrize("body",[
    {"name": "Object1", "data": {"color": "white", "size": "small"}},
    {"name": "Object2", "data": {"color": "blue", "size": "medium"}},
    {"name": "Object3", "data": {"color": "red", "size": "large"}}
])


def test_add_object(body):
    response = add_object(body)
    assert response.status_code == 200, f'Ожидаемый результат: Статус код 200 Фактический результат: {response.status_code}'
    print("\nДобавление нового объекта, методом POST. Объект успешно добавлен!")
    print("Ответ сервера:", response.json())


# Тест для изменения объекта методом PUT
@pytest.mark.critical
def test_update_object_put(new_post):
    object_id = new_post
    update_body = {
        "name": "Update_PUT_Artew",
        "data": {"color": "black&white", "size": "XXXL"}
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://167.172.172.115:52353/object/{object_id}',
        json=update_body,
        headers=headers
    )
    assert response.status_code == 200, (f'Ожидаемый результат:'
                                         f'Статус код 200 Фактический результат: {response.status_code}')
    print("\nОбъект успешно изменен методом PUT!")
    print("Ответ сервера:", response.json())


@pytest.mark.medium
def test_update_object_patch(new_post):
    object_id = new_post
    update_body = {
        "data": {"color": "black&white&RED", "size": "XXL"}
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://167.172.172.115:52353/object/{object_id}',
        json=update_body,
        headers=headers
    )
    assert response.status_code == 200, (f'Ожидаемый результат:'
                                         f'Статус код 200 Фактический результат: {response.status_code}')
    print("\nОбъект успешно изменен методом PATCH!")
    print("Ответ сервера:", response.json())


def test_delete_object_test(new_post):
    object_id = new_post
    response = requests.delete(
        f'http://167.172.172.115:52353/object/{object_id}'
    )
    assert response.status_code == 200, (f'Ожидаемый результат:'
                                         f'Статус код 200 Фактический результат: {response.status_code}')
    print(f"\nОбъект с ID={object_id} успешно удалён!")


# pytest -v
# pytest -vs
# pytest -v -m critical
# pytest -v -m medium
