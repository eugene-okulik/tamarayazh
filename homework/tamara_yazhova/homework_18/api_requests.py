import requests


HEADERS = {"Content-type": "application/json"}


def get_all_posts():
    response = requests.get('http://167.172.172.115:52353/object')
    assert response.status_code == 200, f"Failed to get posts: {response.status_code}, {response.text}"
    print("Success! All posts received!")


def create_post():
    body = {
        "name": "Second object",
        "data": {
            "color": "red",
            "size": "small"
        },
    }
    response = requests.post('http://167.172.172.115:52353/object', json=body, headers=HEADERS)
    assert response.status_code == 200, f"Failed to create post: {response.status_code}, {response.text}"
    print("Success! Post created")
    return response.json()['id']


def update_post_put(post_id):
    body = {
        "name": "Pulp Fiction",
        "data": {
            "director": "Tarantino",
            "genre": "crime"
        },
    }
    response = requests.put(
        f'http://167.172.172.115:52353/object/{post_id}',
        json=body,
        headers=HEADERS
    ).json()
    assert response['name'] == 'Pulp Fiction'
    print("Success! Post updated by put.")


def update_post_patch(post_id):
    body = {
        "name": "Pulp Fiction-UPD"}

    response = requests.patch(
        f'http://167.172.172.115:52353/object/{post_id}',
        json=body,
        headers=HEADERS
    ).json()
    assert response['name'] == 'Pulp Fiction-UPD', f"Failed to update post: {response}"
    print("Success! Post updated by patch.")


def delete_post(post_id):
    response = requests.delete(f'http://167.172.172.115:52353/object/{post_id}')
    assert response.status_code == 200, f"Failed to delete post: {response.status_code}, {response.text}"
    print("Success! Post deleted.")


get_all_posts()
post_id = create_post()
update_post_put(post_id)
update_post_patch(post_id)
delete_post(post_id)
