from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

chrome_path = "C:\Study\Tool\chromedriver\chromedriver.exe"
service = Service(chrome_path)
driver = webdriver.Chrome(service=service, options=options)


### Scrape price of a product from Amazon
# amazon_product_url = "https://www.amazon.com/Instant-Pot-Ultra-Programmable-Sterilizer/dp/B06Y1MP2PY/ref=dp_fod_3?pd_rd_w=zJ9QN&content-id=amzn1.sym.8ec84471-8e07-456a-83de-89571ec52fe8&pf_rd_p=8ec84471-8e07-456a-83de-89571ec52fe8&pf_rd_r=3G76S2K3MESABEKA13ZS&pd_rd_wg=tsHFQ&pd_rd_r=39a27bed-eb62-4548-8f0b-abc1e2562c54&pd_rd_i=B06Y1MP2PY&psc=1"
#
# driver.get(amazon_product_url)
# price = driver.find_element(By.CLASS_NAME, "a-offscreen")
#
# print(price.get_attribute('outerHTML'))
# print(price.get_attribute('innerHTML'))
#




### Scrape all upcoming events from python org
# python_org_url = "https://www.python.org/"
# driver.get(python_org_url)
#
# YEAR = 2023
# event_dict = {}
#
# events_time = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
# events_name = driver.find_elements(By.CSS_SELECTOR, ".event-widget .menu a")
#
# for index in range(len(events_name)):
#     event_dict[index] = {
#         "time":events_time[index].text,
#         "name":events_name[index].text
#     }
#
# print(event_dict)










### Wikipedia
# wikipedia_url = "https://en.wikipedia.org/wiki/Main_Page"
# driver.get(wikipedia_url)
#
# count = driver.find_element(By.CSS_SELECTOR, "#articlecount")
# number_of_articles = count.find_element(By.CSS_SELECTOR, "#articlecount > a:nth-child(1)")
# print(number_of_articles.text)











### App Brewery sign up
signup_url = "https://web.archive.org/web/20220120120408/https://secure-retreat-92358.herokuapp.com/"
driver.get(signup_url)

input_fname = driver.find_element(By.NAME, "fName")
input_fname.send_keys("Seunghoon")

input_lname = driver.find_element(By.NAME, "lName")
input_lname.send_keys("Baik")

input_email = driver.find_element(By.NAME, "email")
input_email.send_keys("j00hoon1101@gmail.com")

driver.find_element(By.CSS_SELECTOR, ".btn").click()

# driver.quit()
