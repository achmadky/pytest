import requests
import json
import jsonpath

baseUrl = "https://reqres.in/api/"
file = open('TestData/headers.json', "r")
headers = json.loads(file.read())
path = "users"


def test_get_users() :
    
    response = requests.post(url=baseUrl+path, headers=headers)
    responseJson = json.loads(response.text)
    assert response.status_code == 201
    print(responseJson)
    #assert jsonpath.jsonpath(responseJson,'$.data.error') == False