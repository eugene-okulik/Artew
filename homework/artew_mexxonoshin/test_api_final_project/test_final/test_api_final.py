import allure
import pytest
import requests
from test_api_final_project.conftest import core_client, auth_client, mem_client, post_client, put_client, delete_client


@allure.title("GET / - Проверка главной страницы API")
def test_welcome_page(core_client):
    response = core_client.check_welcome_page()
    print(f"Ответ сервера: {response.text}")


@allure.title("Авторизация с массивом вместо имени")
def test_auth_with_array_instead_of_name(auth_client):
    # Отправляем невалидные данные (используем правильное имя метода)
    auth_client.authorize_invalid(json_data={"name": []})
    auth_client.check_status(400)
    auth_client.check_html_error(
        expected_title="400 Bad Request",
        expected_message="Invalid parameters"
    )
    print("\nТест пройден: ошибка для массива получена")


@allure.title("Неавторизованный доступ")
def test_unauthorized_access(mem_client):
    # Удаляем заголовок авторизации
    mem_client.headers.pop('Authorization', None)
    mem_client.get_all_memes()
    mem_client.check_status(401)
    print("\nТест пройден: неавторизованный доступ отклонен")


@allure.title("Успешная авторизация")
def test_successful_authorization(auth_client):
    auth_client.authorize(name="TestUser")
    auth_client.check_status(200)
    assert hasattr(auth_client, 'token'), "Токен не получен"
    assert auth_client.token, "Токен пустой"
    print(f"\nТокен получен: {auth_client.token}")


@allure.title("GET /meme - Получение мемов с авторизацией 200")
def test_get_memes_with_auth(auth_client, mem_client):
    # Авторизуемся (если токен еще не получен)
    if not hasattr(auth_client, 'token') or not auth_client.token:
        test_successful_authorization(auth_client)

    mem_client.headers['Authorization'] = auth_client.token
    mem_client.get_all_memes()
    mem_client.check_status(200)
    print("Ответ получен, статус 200")

    response = mem_client.check_json_response()
    assert isinstance(response, dict), "Ответ должен быть словарем"
    assert 'data' in response, "В ответе должно быть поле data"


@allure.title("Проверка валидности токена")
def test_token_validation(auth_client):
    with allure.step("Авторизация пользователя"):
        auth_client.authorize(name="TestUser")
        auth_client.check_status(200)

    with allure.step("Проверка валидности токена"):
        auth_client.check_token()
        auth_client.check_status(200)
        assert auth_client.response.text.startswith("Token is alive."), (
            f"Ответ сервера должен начинаться с 'Token is alive.', получено: '{auth_client.response.text}'"
        )
# pytest test_api_final.py -v -s
# pytest test_api_final.py::test_token_validation -v -s
# pytest test_api_final.py::test_get_memes_with_auth -v -s


@allure.title("GET /meme/{id} - Получение мема по ID - 200")
def test_get_single_meme(auth_client, mem_client):
    auth_client.authorize("artew")
    auth_client.check_token_exists()
    mem_client.headers['Authorization'] = auth_client.token

    mem_client.get_all_memes()
    mem_client.check_status(200)

    # Проверяем JSON-ответ и получаем ID первого мема
    all_memes = mem_client.check_json_response()
    test_id = all_memes['data'][0]['id']

    # Получаем конкретный мем по ID
    mem_client.get_meme_by_id(test_id)
    mem_client.check_status(200)

    # Проверяем, что полученный мем имеет правильный ID
    meme_data = mem_client.check_json_response()
    assert meme_data['id'] == test_id, "ID полученного мема не совпадает с запрошенным"


@allure.title("GET /meme/{id} - Неавторизованный доступ к мему по ID → 401")
def test_get_single_meme_unauthorized(auth_client, mem_client):
    with allure.step("Получаем ID существующего мема"):
        auth_client.authorize("TestUser")
        auth_client.check_status(200)

        mem_client.headers['Authorization'] = auth_client.token
        mem_client.get_all_memes()
        mem_client.check_status(200)
        test_id = mem_client.check_json_response()['data'][0]['id']

    with allure.step("Проверяем доступ без авторизации"):
        mem_client.headers.pop('Authorization', None)  # Удаляем токен
        mem_client.get_meme_by_id(test_id)

        mem_client.check_status(401)
        response_text = mem_client.response.text

        assert "<title>401 Unauthorized</title>" in response_text, "Неверный заголовок ошибки"
        assert "<h1>Unauthorized</h1>" in response_text, "Неверный заголовок страницы"
        assert "Not authorized" in response_text, "Неверное сообщение об ошибке"


@allure.title("GET /meme/{id} - Запрос несуществующего мема → 404")
def test_get_nonexistent_meme(auth_client, mem_client):
    with allure.step("Авторизация"):
        auth_client.authorize("TestUser")
        auth_client.check_status(200)
        mem_client.headers['Authorization'] = auth_client.token

    with allure.step("Запрос несуществующего мема"):
        nonexistent_id = 99999999  # Заведомо несуществующий ID
        mem_client.get_meme_by_id(nonexistent_id)

        mem_client.check_status(404)
        response_text = mem_client.response.text

        assert "<title>404 Not Found</title>" in response_text, "Неверный заголовок ошибки"
        assert "<h1>Not Found</h1>" in response_text, "Неверный заголовок страницы"
        assert "The requested URL was not found" in response_text, "Неверное сообщение об ошибке"


@allure.title("POST /meme - Успешное создание мема → 200")
def test_create_meme_success(auth_client, post_client):
    with allure.step("Авторизация пользователя"):
        auth_client.authorize("TestUser")
        auth_client.check_status(200)
        auth_client.check_token_exists()  # Явная проверка токена
        post_client.headers['Authorization'] = auth_client.token

    test_data = {
        "text": "Funny Python Meme",
        "url": "https://example.com/python_meme.jpg",
        "tags": ["python", "testing"],
        "info": {"author": "pytest"}
    }

    with allure.step("Создание мема"):
        post_client.create_meme(**test_data)

    with allure.step("Проверка ответа сервера"):
        post_client.check_status(200)
        post_client.check_json_response()  # Проверяем что ответ JSON

        # Проверка полей через check_json_field()
        post_client.check_json_field('id')
        post_client.check_json_field('text', test_data['text'])
        post_client.check_json_field('url', test_data['url'])
        post_client.check_json_field('info', test_data['info'])
        post_client.check_json_field('updated_by')

        # Проверка тегов (с учетом возможного разного порядка)
        tags_response = post_client.response.json()['tags']
        assert set(tags_response) == set(test_data['tags']), (
            f"Теги не совпадают. Ожидалось: {test_data['tags']}, получено: {tags_response}"
        )


@allure.title("POST /meme - Попытка создать мем без авторизации 401 Unauthorized")
def test_create_meme_unauthorized(post_client):
    with allure.step("Подготовка тестовых данных"):
        test_data = {
            "text": "Funny Python Meme",
            "url": "https://example.com/python_meme.jpg",
            "tags": ["python", "testing"],
            "info": {"author": "pytest"}
        }

    with allure.step("Попытка создать мем без авторизации"):
        response = post_client.create_meme(**test_data)

    with allure.step("Проверка ошибки 401 Unauthorized"):
        post_client.check_html_error(
            expected_title="401 Unauthorized",
            expected_message="Not authorized"
        )
        print(f"Ответ сервера: {response.text}")

# pytest test_api_final.py::test_create_meme_unauthorized -v -s


@allure.title("POST /meme - Проверка обязательности полей → 400")
@pytest.mark.parametrize("missing_field", ["text", "url", "tags", "info"])
def test_create_meme_missing_field(auth_client, post_client, missing_field):
    with allure.step("Авторизация пользователя"):
        auth_client.authorize("TestUser")
        auth_client.check_status(200)
        auth_client.check_token_exists()
        post_client.headers["Authorization"] = auth_client.token

    test_data = {
        "text": "Funny Python Meme",
        "url": "https://example.com/python_meme.jpg",
        "tags": ["python", "testing"],
        "info": {"author": "pytest"}
    }

    with allure.step(f"Удаляем поле '{missing_field}'"):
        del test_data[missing_field]
        print(f"\n[DEBUG] Отправляем данные без поля: {missing_field}")
        allure.attach(
            f"Отсутствующее поле: {missing_field}\nОтправляемые данные: {test_data}",
            name="Тестовые данные"
        )

    with allure.step(f"Создание мема без поля '{missing_field}' и получение 400"):
        post_client.create_meme(**test_data)

        post_client.check_html_error(
            expected_title="400 Bad Request",
            expected_message="Missing required field",
            allowed_statuses=(400,)
        )

        response_text = post_client.response.text
        print(f"\n[DEBUG] Ответ сервера (status {post_client.response.status_code}):")
        print(response_text)

        allure.attach(
            response_text,
            name="Ответ сервера",
            attachment_type=allure.attachment_type.HTML
        )

# pytest test_api_final.py::test_create_meme_missing_field -v -s


@allure.title("POST /meme - Проверка обязательности полей - 400")
@pytest.mark.parametrize("missing_field", ["text", "url", "tags", "info"])
def test_create_meme_missing_field(auth_client, post_client, missing_field):
    with allure.step("Авторизация пользователя"):
        auth_client.authorize("TestUser")
        auth_client.check_status(200)
        post_client.headers['Authorization'] = auth_client.token
        print("Авторизация успешна")

    test_data = {
        "text": "Funny Python Meme",
        "url": "https://example.com/python_meme.jpg",
        "tags": ["python", "testing"],
        "info": {"author": "pytest"}
    }
    original_value = test_data.pop(missing_field)
    print(f"Удалено поле {missing_field}, значение было: {original_value}")
    print(f"Данные для отправки: {test_data}")


    with allure.step(f"Создание мема без поля '{missing_field}'"):
        post_client.create_fail_meme(meme_data=test_data)  # Явно передаем словарь

    with allure.step("Проверка ответа сервера"):
        print("Проверяем ответ...")
        post_client.check_status(400)
        print("Получен ожидаемый статус 400")

    debug_info = (
            f"\n=== Debug Info ===\n"
            f"Отсутствующее поле: {missing_field}\n"
            f"Отправленные данные: {test_data}\n"
            f"Ответ сервера:\n{post_client.response.text}\n"
            f"Status Code: {post_client.response.status_code}\n"
            f"=================="
    )

    allure.attach(
            f"Missing field: {missing_field}\n"
            f"Request data: {test_data}\n"
            f"Response: {post_client.response.text}",
            name="Debug info"
    )

    print(debug_info)


@allure.title("PUT /meme/<id> - Обновление мема")
def test_update_meme_unauthorized(put_client):
    with allure.step("Попытка обновления без токена и получение 401"):
        put_client.update_meme(
            meme_id=1,
            text="Unauthorized try",
            url="https://example.com/fake.jpg",
            tags=["test"],
            info={"error": "expected"}
        )
        put_client.check_status(401)
        print(put_client.response.text)


def test_update_meme(auth_client, post_client, put_client):
    with allure.step("Авторизация пользователя"):
        auth_client.authorize("ARTEW")
        auth_client.check_status(200)
        post_client.headers['Authorization'] = auth_client.token
        put_client.headers['Authorization'] = auth_client.token
        print("Успешная авторизация")

    with allure.step("Создание тестового мема"):
        post_client.create_meme(
            text="Original Python Meme",
            url="https://example.com/original.jpg",
            tags=["python", "original"],
            info={"author": "pytest"}
        )

        post_client.check_status(200)
        meme_id = post_client.response.json()["id"]
        print(f"Создан мем с ID, {meme_id}")

    with allure.step("Обновление данных мема"):
        updated_text = "Updated Python Meme"
        updated_url = "https://example.com/updated.jpg"
        updated_tags = ["python", "updated"]
        updated_info = {"author": "pytest-updated"}

        response = put_client.update_meme(
            meme_id=meme_id,
            text=updated_text,
            url=updated_url,
            tags=updated_tags,
            info=updated_info
        )

        print("Статус:", response.status_code)
        print("Ответ:", response.text)
        put_client.check_status(200)
        print("Мем успешно обновлён!")

    with allure.step("Обновление данных мема"):
        put_client.check_updated_data(
            expected_url=updated_url,
            expected_text=updated_text,
            expected_info=updated_info,
            expected_tags=updated_tags
        )


@allure.title("Успешное удаление мема")
def test_successful_delete(auth_client, post_client, delete_client):
    with allure.step("Авторизация пользователя"):
        auth_client.authorize("ARTEW")
        auth_client.check_status(200)
        post_client.headers['Authorization'] = auth_client.token
        delete_client.headers['Authorization'] = auth_client.token
        print("Успешная авторизация")

    with allure.step("Создание тестового мема"):
        post_client.create_meme(
            text="DELETE Original Python Meme",
            url="https://example.com/delete_original.jpg",
            tags=["python", "delete_original"],
            info={"author": "delete_pytest"}
        )

        meme_id = post_client.response.json()['id']
        print(f"Создан мем с ID, {meme_id}")

    with allure.step("Удаление тестового мема"):
        delete_client.delete_meme(meme_id)
        delete_client.check_successful_delete(meme_id)
        print(f"Мем с ID: {meme_id} успешно удалён")

        allure.attach(
            f"Удалён мем ID: {meme_id}\n"
            f"Ответ сервера: {delete_client.response.text}",
            name="Результат удаления"
        )

# pytest test_api_final.py::test_successful_delete -v -s


@allure.title("Проверка удаления несуществующего мема")
def test_repeated_delete(auth_client, delete_client):
    with allure.step("Авторизация пользователя"):
        auth_client.authorize("ARTEW")
        delete_client.headers['Authorization'] = auth_client.token

    with allure.step("Попытка удалить заведомо несуществующий мем"):
        non_meme_id = 999999
        delete_client.delete_meme(non_meme_id)
        delete_client.check_repeated_delete(non_meme_id)

        allure.attach(
            f"Запрошено удаление ID: {non_meme_id}\n"
            f"Статус: {delete_client.response.status_code}\n"
            f"Ответ: {delete_client.response.text}",
            name="Результат удаления",
            attachment_type=allure.attachment_type.TEXT
        )
    print(f"Проверено удаление несуществующего мема ID: {non_meme_id}")


@allure.title("Попытка удаления чужого мема")
def test_unauthorization_delete(auth_client, post_client, delete_client):
    with allure.step("Авторизация пользователя-владельца"):
        auth_client.authorize("OWNER-user")
        owner_token = auth_client.token
        post_client.headers['Authorization'] = owner_token
        print("Авторизован владелец токена OWNER-user")

    with allure.step("Создание тестового мема под пользователем - OWNER-user"):
        post_client.create_meme(
            text="Чужой мем для теста",
            url="https://example.com/foreign_meme.jpg",
            tags=["test", "foreign"],
            info={"owner": "OwnerUser"}
        )

        meme_id = post_client.response.json()['id']
        print(f"Создан мем в ID: {meme_id}")

    with allure.step("Авторизация другого пользователя OTHER-user"):
        auth_client.authorize("OTHER-user")
        other_token = auth_client.token
        delete_client.headers['Authorization'] = other_token
        print("Авторизован пользователь OTHER-user")

    with allure.step("Попытка удаления чужого мема"):
        delete_client.delete_meme(meme_id)
        delete_client.check_unauthorized_delete()
        print(f"Проверено: OTHER-user не смог удалить мем: {meme_id}, владельца - OWNER-user")
        # print(f"Статус ответа: {delete_client.response.status_code}")
        # print(f"Ответ сервера:\n{delete_client.response.text}")

    allure.attach(
        f"Попытка удаления чужого мема c ID: {meme_id}\n"
        f"Ожидаемый статус: 403\n"
        f"Фактический статус: {delete_client.response.status_code}\n"
        f"Ответ: {delete_client.response.text}",
        name="Результат проверки прав доступа"
    )

    with allure.step("Проверка что мем остался доступен - OWNER-user-у для удаления"):
        post_client.headers['Authorization'] = owner_token
        response = requests.delete(
            f"{post_client.base_url}/meme/{meme_id}",
            headers={'Authorization': owner_token}
        )

        print(
            f" Мем: {meme_id} Доступен владельцу \n"
            f"Статус ответа на удаление: {response.status_code}\n"
            f"Тело ответа: {response.text}"
        )

# rm -rf allure-results
# pytest --alluredir=allure-results
# allure serve allure-results
