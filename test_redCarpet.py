from redCarpet import *
from starlette.testclient import TestClient
import nest_asyncio
nest_asyncio.apply()

client = TestClient(app)
def test_get_location():
    response = client.get("/get_location", json={ "latitude": 26.6334,"longitude": 47.2164})
    assert response.status_code == 200
    assert response.json() == {
                                  "key": "IN/1100112",
                                  "place_name": "Connaught Place",
                                  "admin_name1": "New Delhi"
                                }
def test_get_using_postres():
    response = client.get("/get_using_postgres", json={ "latitude": 26.6334,"longitude": 47.2164})
    assert response.status_code == 200
    assert response.json() == [
                                  "IN/1100112",
                                  "IN/110332"
                                ]