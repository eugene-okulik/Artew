import pytest

from test_api_artew_mexx.conftest import object_id

body_data = [
    {"name": "Object1", "data": {"color": "white", "size": "small"}},
    {"name": "Object2", "data": {"color": "blue", "size": "medium"}},
    {"name": "Object3", "data": {"color": "red", "size": "large"}}
]


@pytest.mark.parametrize('data', body_data)
def test_add_post_object(create_post_endpoint, data):
    create_post_endpoint.create_new_post(data)
    create_post_endpoint.check_that_status_is_200()


def test_get_all_object(get_all_object):
    get_all_object.get_all_object()
    get_all_object.check_that_status_is_200()


def test_update_object_put(object_id, update_object_put):
    print(f"Тест test_update_object_put: используемый object_id: {object_id}")
    update_body = {"name": "Update_PUT_Artew", "data": {"color": "black&white", "size": "XXXL"}}
    update_object_put.update_object_put(object_id, update_body)
    update_object_put.check_that_status_is_200()


def test_update_object_patch(object_id, update_object_patch):
    print(f"Тест test_update_object_patch: используемый object_id: {object_id}")
    update_body = {"data": {"color": "black&white&RED", "size": "XXL"}}
    update_object_patch.update_object_patch(object_id, update_body)
    update_object_patch.check_that_status_is_200()


def test_delete_object(object_id, delete_object):
    print(f"Тест test_delete_object: используемый object_id: {object_id}")
    delete_object.delete_object(object_id)
    delete_object.check_that_status_is_200()

# pytest -s
