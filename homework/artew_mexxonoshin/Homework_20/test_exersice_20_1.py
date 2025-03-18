import requests
import pytest
import allure


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


# Получение списка всех объектов GET /object
@allure.feature("Управление объектами")
@allure.story("Получение списка объектов")
def test_all_object():
    with allure.step("Выполнение GET-запроса для получения списка объектов"):
        response = requests.get('http://167.172.172.115:52353/object')
    with allure.step("Проверка статус-кода и вывод результата"):
        if response.status_code == 200:
            print("Выполнение GET полный список объектов:")
            print(response.json())
        else:
            print(f"Ошибка: {response.status_code}")
        assert response.status_code == 200, (f'Ожидаемый результат:'
                                             f'Статус код 200 Фактический результат: {response.status_code}')


# Добавление новых объектов POST /object
def add_object(body):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://167.172.172.115:52353/object',
        json=body,
        headers=headers
    )
    return response


@allure.feature("Управление объектами")
@allure.story("Добавление новых объектов")
@allure.title("Тест добавления объектов с разными параметрами")
@pytest.mark.parametrize("body", [
    {"name": "Object1", "data": {"color": "white", "size": "small"}},
    {"name": "Object2", "data": {"color": "blue", "size": "medium"}},
    {"name": "Object3", "data": {"color": "red", "size": "large"}}
])
def test_add_object(body):
    with allure.step("Выполнение POST-запроса для добавления объекта"):
        response = add_object(body)

    with allure.step("Проверка статус-кода и вывод результата"):
        assert response.status_code == 200, (f'Ожидаемый результат:'
                                             f'Статус код 200 Фактический результат: {response.status_code}')
    print("\nДобавление нового объекта, методом POST. Объект успешно добавлен!")
    print("Ответ сервера:", response.json())


# Тест для изменения объекта методом PUT
@allure.feature("Управление объектами")
@allure.story("Изменение объекта методом PUT")
@pytest.mark.critical
def test_update_object_put(new_post):
    object_id = new_post
    update_body = {
        "name": "Update_PUT_Artew",
        "data": {"color": "black&white", "size": "XXXL"}
    }
    with allure.step("Выполнение PUT-запроса для изменения объекта"):
        response = requests.put(
            f'http://167.172.172.115:52353/object/{object_id}',
            json=update_body,
            headers={'Content-Type': 'application/json'}
        )
    with allure.step("Проверка статус-кода и вывод результата"):
        assert response.status_code == 200, (f'Ожидаемый результат:'
                                             f'Статус код 200 Фактический результат: {response.status_code}')
        allure.attach(str(response.json()), "Ответ сервера", allure.attachment_type.JSON)
        print("\nОбъект успешно изменен методом PUT!")
        print("Ответ сервера:", response.json())


# Тест для изменения объекта методом PATCH
@allure.feature("Управление объектами")
@allure.story("Изменение объекта методом PATCH")
@pytest.mark.medium
def test_update_object_patch(new_post):
    object_id = new_post
    update_body = {
        "data": {"color": "black&white&RED", "size": "XXL"}
    }
    with allure.step("Выполнение PATCH-запроса для изменения объекта"):
        response = requests.patch(
            f'http://167.172.172.115:52353/object/{object_id}',
            json=update_body,
            headers={'Content-Type': 'application/json'}
        )
    with allure.step("Проверка статус-кода и вывод результата"):
        assert response.status_code == 200, (f'Ожидаемый результат:'
                                             f'Статус код 200 Фактический результат: {response.status_code}')
        allure.attach(str(response.json()), "Ответ сервера", allure.attachment_type.JSON)
        print("\nОбъект успешно изменен методом PATCH!")
        print("Ответ сервера:", response.json())


# Тест для удаления объекта
@allure.feature("Управление объектами")
@allure.story("Удаление объекта")
def test_delete_object_test(new_post):
    object_id = new_post
    with allure.step("Выполнение DELETE-запроса для удаления объекта"):
        response = requests.delete(
            f'http://167.172.172.115:52353/object/{object_id}'
        )
    with allure.step("Проверка статус-кода и вывод результата"):
        assert response.status_code == 200, (f'Ожидаемый результат:'
                                             f'Статус код 200 Фактический результат: {response.status_code}')
        allure.attach(str(response.text), "Ответ сервера", allure.attachment_type.TEXT)
        print(f"\nОбъект с ID={object_id} успешно удалён!")


# pytest --alluredir=allure-results с сохранением результатов
# allure serve allure-results генерация отчета