import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


EMAIL = "j00hoon1101@gmail.com"
PASSWORD = ""

LINKED_URL = "https://www.linkedin.com/jobs/search/?currentJobId=3506991390&distance=25&f_E=2&f_TPR=r604800&geoId=105080838&keywords=python%20developer"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

chrome_path = "C:\Study\Tool\chromedriver\chromedriver.exe"
service = Service(chrome_path)
driver = webdriver.Chrome(service=service, options=options)




driver.get(LINKED_URL)

time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "body > div.base-serp-page > header > nav > div > a.nav__button-secondary.btn-md.btn-secondary-emphasis").click()

