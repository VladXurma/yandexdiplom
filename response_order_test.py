import configuration
import requests
import data
import sender_stand_request

def test_get_order():
    track = sender_stand_request.create_new_order(data.body).json()["track"]
    response = sender_stand_request.get_order(track)
    assert response.status_code == 200

# Владислав Никитин, 13-я когорта. Финальный проект. Инженер по тестированию плюс
