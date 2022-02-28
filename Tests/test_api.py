from Helper.crudAPI import CRUDapi
import jsonpath
import json

class Test_main:


    def test_getapi(self):
        url = "https://reqres.in/api/users?page=2"
        response = CRUDapi().getAPI(url)
        if response.status_code == 200:
            assert True
            json_response = json.loads(response.text)
            #print(json_response)
            data = jsonpath.jsonpath(json_response, "data")
            # print(data[0][1]["id"])
            # for i in data[0]:
            #     print(i["id"])
            print(data)
        else:
            print(response.status_code)
            assert False

    def test_post(self):
        url = "https://reqres.in/api/users"
        payload = {"name": "morpheus",
                    "job": "leader"}
        response = CRUDapi().postAPI(url,payload)

        if response.status_code==201:
            assert True
            json_response = json.loads(response.text)
            print(json_response)

        else:
            print(response.status_code)
            assert False