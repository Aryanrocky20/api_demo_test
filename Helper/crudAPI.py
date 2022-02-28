import requests
import os
import time

class CRUDapi:


    def getAPI(self,url):
        print("****** Get API ******")
        self.resp = requests.get(url)
        return self.resp

    def postAPI(self,url,data):
        print("****** Post API ******")
        self.resp = requests.post(url, data=data)
        return self.resp
