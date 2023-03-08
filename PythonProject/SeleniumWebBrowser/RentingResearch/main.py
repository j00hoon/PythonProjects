from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup
import requests



### Get a list of renting properties
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLScTK_jnORAKZWLi3u4FmqwY4vBfl_lYYf82JlPU-KYtrXKOnQ/viewform?usp=sf_link"
RENTING_LIST_URL = "https://www.zillow.com/hoboken-nj/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A40.76331681914328%2C%22east%22%3A-73.99011211346433%2C%22south%22%3A40.72612109764213%2C%22west%22%3A-74.06778888653562%7D%2C%22mapZoom%22%3A15%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A501081%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A2600%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A25146%2C%22regionType%22%3A6%7D%5D%7D"
RENTING_LIST_HEADERS = {
    # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0",
    'User-Agent': 'Chrome',
    "Accept-Language": "en-US,en;q=0.5"
}



options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

chrome_path = "C:\Study\Tool\chromedriver\chromedriver.exe"
service = Service(chrome_path)
driver = webdriver.Chrome(service=service, options=options)

# driver = webdriver.Firefox()

driver.get(RENTING_LIST_URL)

# response = requests.get(url=RENTING_LIST_URL, headers=RENTING_LIST_HEADERS)
# renting_page = response.text
# print(renting_page)
# soup = BeautifulSoup(renting_page, "html.parser")

list_length = int(str(driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div/div/div[1]/div[1]/div[1]/div/span")
                      .text)
                  .split("results")[0])

address_list = []
price_list = []
link_list = []

scroll = driver.find_element(By.XPATH, '//*[@id="search-page-list-container"]')
for i in range(1, list_length):
    driver.execute_script(f"arguments[0].scrollTop = {i * 1000}", scroll)
    time.sleep(1)
    data = driver.find_element(By.CSS_SELECTOR, f"li.ListItem-c11n-8-85-1__sc-10e22w8-0:nth-child({i})")\
        .text
    try:
        address = data.split("\n")[0]
        price = data.split("\n")[1].split("/")[0]
        link = driver.find_element(By.XPATH,
                                   f"/html/body/div[1]/div[5]/div/div/div[1]/div[1]/ul/li[{i}]/div/div/article/div/div[1]/a") \
            .get_attribute("href")
        address_list.append(address)
        price_list.append(price)
        link_list.append(link)
    except (IndexError, NoSuchElementException):
        pass








### Fill the research form and update the Google sheet
RESEARCH_URL = "https://docs.google.com/forms/d/e/1FAIpQLSduFOdDtNvWC-_ODlRoVJ21RonjOhCU6OYGesNWoQe7IF09dg/viewform?usp=sf_link"
driver.get(url=RESEARCH_URL)

for index in range(0, len(address_list)):
    time.sleep(1)
    input_address = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    input_address.send_keys(address_list[index])
    input_price = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    input_price.send_keys(price_list[index])
    input_link = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    input_link.send_keys(link_list[index])
    driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[4]/a").click()






