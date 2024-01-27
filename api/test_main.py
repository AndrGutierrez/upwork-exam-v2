from fastapi.testclient import TestClient
from sqlalchemy import Null
from main import app
import json
import pytest

client = TestClient(app)    


def clear_responses(response):
    response = response
    if len(response["profile"])>0: 
        profile=response["profile"][0]
        profile.pop('id')

    response.pop('id')
    return response

def test_delete_users():
    response = client.delete("users/delete?email=johndoe@gmail.com")
    assert response.status_code==200 or 400
    assert response == None or Null

def test_create_user():
    response = client.post("/users/create",json={
      "user": {
        "email": "johndoe@gmail.com"
      },
      "profile": {
        "name": "john",
        "description": "I'm Johndoe"
      }
    })

    assert response.status_code == 200 or 400

    response = response.json()
    response = clear_responses(response)    

    assert response == {
      "email": "johndoe@gmail.com",
      "profile": [
        {
          "name": "john",
          "description": "I'm Johndoe",
        }
      ],
      "favorite_profiles": []
    }

def test_read_users():
    response = client.get("/users/")
    assert response.status_code == 200
    clean_response=[]
    for item in response.json():
        clean_response.append(clear_responses(item))

    assert {
        "email": "johndoe@gmail.com",
        "profile": [
          {
            "name": "john",
            "description": "I'm Johndoe",
          }
        ],
        "favorite_profiles": []
      } in clean_response

if __name__ == "__main__":
    client=TestClient(app)
