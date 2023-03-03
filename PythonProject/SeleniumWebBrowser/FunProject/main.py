import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)

# chrome_path = "C:\Study\Tool\chromedriver\chromedriver.exe"
# service = Service(chrome_path)
# driver = webdriver.Chrome(service=service, options=options)

driver = webdriver.Firefox()

URL = "https://tinder.com/"
EMAIL = ""
PASSWORD = ""

### Open firefox browser
driver.get(URL)

time.sleep(10)

### Click "Log in" button
login_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
login_button.click()

time.sleep(5)

### Click "Continue with google"
continue_button = driver.find_element(By.XPATH, '//*[@id="o1622039657"]/main/div/div/div[1]/div/div/div[3]/span/div[3]/button/div[2]/div[2]/div/div')
continue_button.click()

