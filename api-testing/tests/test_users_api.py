from utils.api_client import APIClient
import json
import os


def load_test_data():
    data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "users.json")
    with open(data_path, "r") as file:
        return json.load(file)


def test_get_all_users():
    client = APIClient()
    response = client.get("/users")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0


def test_get_single_user():
    client = APIClient()
    response = client.get("/users/1")

    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_create_user():
    client = APIClient()
    test_data = load_test_data()

    response = client.post("/users", test_data["new_user"])

    assert response.status_code in [200, 201]
    assert response.json()["name"] == test_data["new_user"]["name"]