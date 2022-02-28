import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\\Users\\yash.chindalia\\PycharmProjects\\Pytest_Demo\\Drivers\\chromedriver.exe"

driver=webdriver.Chrome(chrome_driver_path)

driver.get('https://in.search.yahoo.com/?fr2=inr')
links = driver.find_elements(By.CSS_SELECTOR, "a")
print (links)
for link in links:
    r = requests.head(link.get_attribute('href'))
    print(link.get_attribute('href'), r.status_code)