import pytest
from test_api_tyazhova.endpoints.create_post import CreatePost
from test_api_tyazhova.endpoints.update_post import UpdatePost
from test_api_tyazhova.endpoints.delete_post import DeletePost
from test_api_tyazhova.endpoints.get_all_posts import GetPosts


url = 'http://167.172.172.115:52353/object'
headers = {"Content-type": "application/json"}


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
def create_post_endpoint():
    return CreatePost()


@pytest.fixture()
def update_post_endpoint():
    return UpdatePost(url)


@pytest.fixture()
def delete_post_endpoint():
    return DeletePost()


@pytest.fixture()
def get_posts_endpoint():
    return GetPosts()


@pytest.fixture()
def create_object(create_post_endpoint, delete_post_endpoint):
    body = {"name": "Second object", "data": {"color": "red", "size": "small"}}
    post_id = create_post_endpoint.create_new_post(body)
    yield post_id
    delete_post_endpoint.delete_post(post_id)
