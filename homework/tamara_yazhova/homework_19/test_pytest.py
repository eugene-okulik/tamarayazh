import requests
import pytest


HEADERS = {"Content-type": "application/json"}
BASE_URL = 'http://167.172.172.115:52353/object'


@pytest.fixture(scope="session")
def add_messages_for_all():
    print("\nStart testing")
    yield
    print("\nTesting completed")

@pytest.fixture()
def add_message_for_each():
    print("\nbefore test")
    yield
    print("\nafter test")

@pytest.fixture()
def create_object():
    body = {"name": "Second object", "data": {"color": "red", "size": "small"}}
    response = requests.post(BASE_URL, json=body, headers=HEADERS)
    post_id = response.json()['id']
    yield post_id
    requests.delete(f'{BASE_URL}/{post_id}')

@pytest.mark.parametrize("name, data", [
    ("Object_1", {"color": "red", "size": "small"}),
    ("Object_2", {"color": "white", "size": "small"}),
    ("Object_3", {"color": "black", "size": "big"}),
])

@pytest.mark.critical
def test_create_post(name, data, add_messages_for_all, add_message_for_each):
    body = {"name": name, "data": data}
    response = requests.post(BASE_URL, json=body, headers=HEADERS)
    assert response.status_code == 200, f"Failed to create post: {response.status_code}, {response.text}"
    obj_id = response.json()['id']
    requests.delete(f'{BASE_URL}/{obj_id}')

@pytest.mark.medium
def test_get_all_posts(add_message_for_each):
    response = requests.get(BASE_URL)
    assert response.status_code == 200, f"Failed to get posts: {response.status_code}, {response.text}"

def test_update_post_put(create_object, add_message_for_each):
    post_id = create_object
    body = {
        "name": "Pulp Fiction",
        "data": {
            "director": "Tarantino",
            "genre": "crime"
        },
    }
    response = requests.put(
        f'{BASE_URL}/{post_id}', json=body, headers=HEADERS).json()
    assert response['name'] == 'Pulp Fiction'

def test_update_post_patch(create_object, add_message_for_each):
    post_id = create_object
    body = {"name": "Pulp Fiction-UPD"}
    response = requests.patch(
        f'{BASE_URL}/{post_id}', json=body, headers=HEADERS).json()
    assert response['name'] == 'Pulp Fiction-UPD', f"Failed to update post: {response}"

def test_delete_post(create_object, add_message_for_each):
    post_id = create_object
    response = requests.delete(f'{BASE_URL}/{post_id}')
    assert response.status_code == 200, f"Failed to delete post: {response.status_code}, {response.text}"
