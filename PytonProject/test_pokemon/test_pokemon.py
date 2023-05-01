import pytest
import requests

# "trainer_token": "147960980c6dad9942d02a2eeab5deba", 

def test_stastus_code():
    url = "https://pokemonbattle.me:9104/trainers"
    header = {"Content-Type": "application/json"}
    response = requests.get(url, headers=header)
    assert response.status_code == 200

def test_name_trainer():
    url = "https://pokemonbattle.me:9104/trainers?trainer_id=4167"
    header = {"Content-Type": "application/json"}
    response = requests.get(url, headers=header)
    response = response.json()
    assert response["trainer_name"] == "Феникс"

