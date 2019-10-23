import requests
import json
import pytest
import os

uri = "https://petstore.swagger.io/v2/pet"
headers = {'Content-Type': 'application/json'}

def test_create_pet():
    petName = "tradeIXPet"
    petStatus = "tradeIX-available"
    payload = {
        "id": 0,
        "category": {
            "id": 0,
            "name": "test-tradeIX"
        },
        "name": petName,
        "photoUrls": [
            'string'
        ],
        "tags": [
            {
                "id": 1234,
                "name": "tradeIX"
            }
        ],
        "status": petStatus
    }

    resp = requests.post(uri, data=json.dumps(
        payload, indent=4), headers=headers)
    assert resp.status_code == 200
    resp_body = resp.json()
    # Assign random id to petId var
    petId = resp_body['id']
    os.environ["petID"] = str(resp_body['id'])
    isinstance(petId, int)
    assert resp_body['name'] == petName
    isinstance(resp_body['category'], dict)
    isinstance(resp_body['status'], str)
    

    # Verify petId Record After Successful creation
    resp = requests.get(uri + "/" + str(petId))
    assert resp.status_code == 200
    resp_body = resp.json()
    assert resp_body['id'] == petId
    assert resp_body['name'] == petName
    assert resp_body['status'] == petStatus
    isinstance(resp_body['photoUrls'], list)
    isinstance(resp_body['tags'], list)

    


    
