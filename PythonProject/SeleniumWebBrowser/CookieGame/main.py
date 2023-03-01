from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


upgrade_id = ["buyCursor", "buyGrandma", "buyFactory", "buyMine", "buyShipment", "buyAlchemy lab", "buyPortal", "buyTime machine"]


def check_upgrade(driver):
    global upgrade_id

    money_for_upgrade = driver.find_elements(By.CSS_SELECTOR, "#rightPanel #store div b")
    upgrade_item_list = driver.find_elements(By.CSS_SELECTOR, "#rightPanel #store div")

    money = int(driver.find_element(By.ID, "money").text)

    # upgrade_money = 0
    upgrade_item = ""
    for upgrade in money_for_upgrade:
        try:
            if upgrade.is_displayed() and money > int(upgrade.text.split("-")[1].replace(",", "")):
                # upgrade_money = int(upgrade.text.split("-")[1].replace(",", ""))
                upgrade_item = str(upgrade.text.split("-")[0])
            else:
                break
        except StaleElementReferenceException:
            money_for_upgrade = driver.find_elements(By.CSS_SELECTOR, "#rightPanel #store div b")

    for index in range(0, len(upgrade_item_list)):
        if upgrade_item_list[index].is_displayed() and upgrade_item == upgrade_item_list[index].text.split("-")[0]:
            # print(f"{upgrade_item}   {index}")
            driver.find_element(By.ID, upgrade_id[index]).click()
            break


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

chrome_path = "C:\Study\Tool\chromedriver\chromedriver.exe"
service = Service(chrome_path)
driver = webdriver.Chrome(service=service, options=options)

cookie_game_url = "https://orteil.dashnet.org/experiments/cookie/"
driver.get(cookie_game_url)
start_time = int(time.time()) + 1

while True:
    if (int(time.time()) - start_time) % 5 == 0:
        check_upgrade(driver)

    driver.find_element(By.ID, "cookie").click()



