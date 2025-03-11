import requests


# Получение списка всех объектов GET /object
def all_object():
    response = requests.get('http://167.172.172.115:52353/object')
    if response.status_code == 200:
        print("Выполнение GET полный список объектов:")
        print(response.json())
    else:
        print(f"Ошибка: {response.status_code}")


all_object()


# Добавление нового объекта POST /object
def add_object():
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
        print("Добавление нового объекта, методом POST. Объект успешно добавлен!")
        print("Ответ сервера:", response.json())
    else:
        print(f"Ошибка: {response.status_code}")
        print("Ответ сервера:", response.text)


add_object()


# Изменение существующего объекта PUT /object/<id>
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
        print("Объект успешно добавлен! Для выполнения следующего метода PUT")
        print("Ответ сервера:", response.json())
        return response.json()['id']
    else:
        print(f"Ошибка: {response.status_code}")
        print("Ответ сервера:", response.text)
        return None


def put_object():
    post_id = new_post()
    body = {
        "name": "Artew",
        "data": {"color": "black&white", "size": "XXL"}
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://167.172.172.115:52353/object/{post_id}',
        json=body,
        headers=headers
    )
    if response.status_code == 200:
        print("Объект успешно изменен методом PUT!")
        print("Ответ сервера:", response.json())
    else:
        print(f"Ошибка: {response.status_code}")
        print("Ответ сервера:", response.text)


put_object()


# Изменение существующего объекта PATCH /object/<id>
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
        print("Объект успешно добавлен! Для выполнения следующего метода PATCH")
        print("Ответ сервера:", response.json())
        return response.json()['id']
    else:
        print(f"Ошибка: {response.status_code}")
        print("Ответ сервера:", response.text)
        return None


def patch_object(post_id):
    # post_id = new_post()
    body = {
        "data": {"color": "black&white&RED", "size": "XXL"}
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://167.172.172.115:52353/object/{post_id}',
        json=body,
        headers=headers
    )
    if response.status_code == 200:
        print("Объект успешно изменен PATCH!")
        print("Ответ сервера:", response.json())
    else:
        print(f"Ошибка: {response.status_code}")
        print("Ответ сервера:", response.text)


# patch_object(post_id)


# Удаление объекта DELETE /object/<id>
def delete_object(post_id):
    # post_id = new_post()
    response = requests.delete(
        f'http://167.172.172.115:52353/object/{post_id}'
    )
    if response.status_code == 200:
        print(f"Объект с id={post_id} успешно удалён!")
    else:
        print(f"Ошибка при удалении объекта: {response.status_code}")
        print("Ответ сервера:", response.text)


post_id = new_post()

if post_id:
    patch_object(post_id)
    delete_object(post_id)
