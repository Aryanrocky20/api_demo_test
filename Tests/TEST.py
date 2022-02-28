import requests
from requests.auth import HTTPBasicAuth
import json
from Helper.crudAPI import CRUDapi
import jsonpath

url = "https://reqres.in/api/users?page=2"
response = CRUDapi().getAPI(url)
if response.status_code == 200:
    assert True
    json_response = json.loads(response.text)
    print(json_response)
    data = jsonpath.jsonpath(json_response,"data")
# print(data[0][1]["id"])
# for i in data[0]:
#     print(i["id"])
    print(data)
    print("history")
else:
    print(response.status_code)
    assert False

