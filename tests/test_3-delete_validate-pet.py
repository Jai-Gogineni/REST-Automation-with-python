import requests
import json
import pytest
import os

uri = "https://petstore.swagger.io/v2/pet"

def test_delete_pet():
    resp = requests.delete(uri + "/" + os.environ["petID"])
    assert resp.status_code == 200
  
    # Verify GET petId after DELETE
    resp = requests.get(uri + "/" + os.environ["petID"])
    assert resp.status_code == 404
    resp_body = resp.json()
    assert resp_body['code'] == 1
    assert resp_body['message'] == "Pet not found"
   

    


    
