import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import requests
from celery.result import AsyncResult
from maintq import *

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Safari()

    def test_get_location(self):
        driver = self.driver
        x="aksjhdakjsd"
        k=gl.delay(28.65,77.2167)

        pq={'key': 'IN/110003', 'place_name': 'Aliganj', 'admin_name1': 'New Delhi'}
        print(k)
        assert pq== AsyncResult(str(k),app=app).get()
    def test_get_using_postgre(self):
        driver = self.driver
        r = requests.get('http://127.0.0.1:8000/get_using_postgres', json={
         "key": "IN/110332",
         "place_name": "Connaught Place",
         "admin_name1": "New Delhi",
         "latitude": 26.6334,
         "longitude": 47.2164,
         "accuracy": 44.0
        })
        pq=[
  "IN/1100112",
  "IN/110332"
]
        assert pq==r.json()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()