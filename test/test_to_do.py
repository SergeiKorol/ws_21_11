import requests


#@pytest.mark.xfail
def test_add_edit():
    # Создается задача
    body = {"title":"generated","completed":False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    old_id = response.json()["id"]

    # Редактирование задачи
    body = {"title":"generated-1"}
    response = requests.patch(f'https://todo-app-sky.herokuapp.com/{id}', json=body)
    new_id = response.json()["id"]
    response = requests.get(f'https://todo-app-sky.herokuapp.com/{id}')

    assert old_id == new_id
