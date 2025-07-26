# we add some staffs for testing our models
import factory
import pytest
from rest_framework.test import APIClient
from django.urls import reverse # type: ignore
from api.models import AfricanLeaders # type: ignore
from api.tests.factories import UserFactory, AfricanLeadersFactory


# we create api client fixtures 
@pytest.fixture
def api_client():
    return APIClient()

# we create auth client fixtures 
@pytest.fixture
def auth_client(api_client): # type: ignore
    user = UserFactory()  # type: ignore
    response = api_client.post("/api/token",{ # type: ignore
        "username":user.username,
        "password":"password123"
    }, format='json')
    access_token = response.data["access"] # type: ignore
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}") # type: ignore
    return api_client  # type: ignore


# we create test get method 
@pytest.mark.django_db
def test_jwt_get(auth_client):# # type: ignore
    AfricanLeadersFactory.create_batch(3) # type: ignore
    response = auth_client.get("/african-leaders/") # type: ignore
    assert response.status_code == 200 # type: ignore
    assert len(response.data) == 3 # type: ignore


# we create test post method 
@pytest.mark.django_db
def test_jwt_post(auth_client):# # type: ignore
    payload = { # type: ignore
        "name" : "Samia Suluhu",
        "country" : "Tanzania",
        "capital" : "Dodoma",
        "party" : "CCM",
        "population":"60 million",
        "gender" : "female",
        "age" : 50
    }
    response = auth_client.post("/african-leaders/",payload)# type: ignore
    assert response.status_code == 201 # type: ignore
    assert response.data["name"] == "Samia Suluhu" # type: ignore




# we create test put method 
@pytest.mark.django_db
def test_jwt_put(auth_client): # type: ignore
    african-leaders-factory = AfricanLeadersFactory()  # type: ignore
    update = { # type: ignore
        "name" : african-leaders-factory.name, # type: ignore
        "country" : "Zanzibar",
        "capital" : "Pemba",
        "party" : "CCM Visiwani",
        "population":"66 million",
        "gender" : "male",
        "age" : 60
    }
    response = auth_client.put(f"/african-leaders/{african-leaders-factory.id}",update) # type: ignore
    assert response.status_code == 200  # type: ignore
    assert response.data["name"] == "updated name" # type: ignore



# we create test delete method 
@pytest.mark.django_db
def test_jwt_delete(auth_client): # type: ignore
     african-leaders-factory = AfricanLeadersFactory()  # type: ignore
     response = auth_client.delete(f"/african-leaders/{african-leaders-factory.id}")# type: ignore
     assert response.status_code == 204 # type: ignore



# @pytest.mark.django_db
# def test_create_african_leaders():
#     client = APIClient()
#     url=reverse('african-leaders-list') # type: ignore
#     data={ # type: ignore
#         "name": "Kaham Mlau",
#         "country": "Tanzania",
#         "capital": "Daresalaam",
#         "party": "CCM",
#         "population": "60 million",
#         "gender": "male",
#         "age": 30,
#     }
#     response = client.post(url, data, format="json") # type: ignore
#     assert response.status_code == 201 # type: ignore
#     assert response.data["name"] == "Kaham Mlau" # type: ignore
    


