import pytest


TEST_DATA = [
    {"name": "Object_1", "data": {"color": "red", "size": "small"}},
    {"name": "Object_2", "data": {"color": "white", "size": "small"}},
    {"name": "Object_3", "data": {"color": "black", "size": "big"}},
]


@pytest.mark.parametrize('data', TEST_DATA)
@pytest.mark.critical
def test_create_post(create_post_endpoint, delete_post_endpoint, data):
    post_id = create_post_endpoint.create_new_post(data)
    create_post_endpoint.check_that_status_is_200()
    delete_post_endpoint.delete_post(post_id)


@pytest.mark.medium
def test_get_all_posts(get_posts_endpoint):
    get_posts_endpoint.get_all_posts()
    get_posts_endpoint.check_that_status_is_200()


def test_update_post_put(create_object, update_post_endpoint):
    body = {
        "name": "Pulp Fiction",
        "data": {
            "director": "Tarantino",
            "genre": "crime"
        },
    }
    update_post_endpoint.update_post_put(create_object, body)
    update_post_endpoint.check_that_status_is_200()


def test_update_post_patch(create_object, update_post_endpoint):
    body = {"name": "Pulp Fiction-UPD"}
    update_post_endpoint.update_post_patch(create_object, body)
    update_post_endpoint.check_that_status_is_200()


def test_delete_post(create_object, delete_post_endpoint):
    delete_post_endpoint.delete_post(create_object)
    delete_post_endpoint.check_that_status_is_200()
