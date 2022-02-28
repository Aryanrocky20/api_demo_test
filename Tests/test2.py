import requests
import jsonpath

p = {'session':"7d6f4aef-5faa-4373-ad9d-f99d1f824b21"}
url = 'https://optumapi-qa.mhddemo.com/optum/d2c/appointment/%d/confirmById'
appointmentid =  40132

response = requests.post(url=url % appointmentid, params=p)
print(response.status_code)
print(response.json())