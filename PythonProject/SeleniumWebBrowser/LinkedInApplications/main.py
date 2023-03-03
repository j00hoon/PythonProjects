import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


EMAIL = "j00hoon1101@gmail.com"
PASSWORD = ""

LINKED_URL = "https://www.linkedin.com/jobs/search/?currentJobId=3506991390&distance=25&f_E=2&f_TPR=r604800&geoId=105080838&keywords=python%20developer"
# LINKED_URL = "https://www.linkedin.com/jobs/search/?currentJobId=3498543160&f_E=2%2C3&f_TPR=r604800&geoId=105080838&keywords=python&location=New%20York%2C%20United%20States&refresh=true"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

chrome_path = "C:\Study\Tool\chromedriver\chromedriver.exe"
service = Service(chrome_path)
driver = webdriver.Chrome(service=service, options=options)




driver.get(LINKED_URL)

time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "body > div.base-serp-page > header > nav > div > a.nav__button-secondary.btn-md.btn-secondary-emphasis").click()

input_email = driver.find_element(By.NAME, "session_key")
input_email.send_keys("j00hoon1101@gmail.com")

input_password = driver.find_element(By.NAME, "session_password")
input_password.send_keys(PASSWORD)

driver.find_element(By.CSS_SELECTOR, "#organic-div > form > div.login__form_action_container > button").click()
time.sleep(3)




