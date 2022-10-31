import requests
import json
import jsonpath

baseUrl = "https://reqres.in/api/"
file = open('TestData/headers-put.json', "r")
headers = json.loads(file.read())
path = "users/2"


def test_get_users() :
    
    response = requests.put(url=baseUrl+path, headers=headers)
    responseJson = json.loads(response.text)
    assert response.status_code == 200
    print(responseJson)
    #assert jsonpath.jsonpath(responseJson,'$.data.error') == False