import requests

#GET
# def test_user_details():
#     response = requests.get("https://jsonplaceholder.typicode.com/users/1")
#     data = response.json()
#     assert response.status_code == 200
#     assert data["id"] == 1
#     assert data["username"] == "Bret"

#POST
# def test_create_user():
#     payload = {
#         "name": "Daniel",
#         "job": "SDET"
#     }
#     response = requests.post("https://jsonplaceholder.typicode.com/todos",json=payload)
#     assert response.status_code == 201

#PUT
# def test_update_user():
#     payload = {
#         "name": "Adame"
#     }
#     response = requests.put("https://jsonplaceholder.typicode.com/users/1",json=payload)
#     assert response.status_code == 200

#DELETE
def test_delete_user():
    response = requests.delete("https://jsonplaceholder.typicode.com/users/1")
    assert response.status_code == 200
