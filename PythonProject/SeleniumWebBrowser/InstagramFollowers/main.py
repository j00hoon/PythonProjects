import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait


INSTAGRAM_URL = "https://www.instagram.com/"
SIMILAR_ACCOUNTS = ""
USERNAME = ""
PASSWORD = ""


class InstaFollower:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)

        self.chrome_path = "C:\Study\Tool\chromedriver\chromedriver.exe"
        self.service = Service(self.chrome_path)
        self.driver = webdriver.Chrome(service=self.service, options=self.options)


    def login(self):
        insta_login_url = "https://www.instagram.com/accounts/login/"
        self.driver.get(insta_login_url)
        time.sleep(3)

        input_email = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input")
        input_email.send_keys(USERNAME)
        input_password = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input")
        input_password.send_keys(PASSWORD)
        time.sleep(1)

        ### Log in
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button').click()

    def find_followers(self):
        time.sleep(5)

        ### Not now login info
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button").click()
        time.sleep(5)

        ### Not now notification
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
        time.sleep(5)

        ### Click search
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/a/div/div[1]/div').click()
        time.sleep(5)

        ### Input instagram channel
        input_search = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input")
        input_search.send_keys(SIMILAR_ACCOUNTS)
        time.sleep(5)

        ### Find instagram channel
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/a/div/div[2]/div[1]/div/div/div').click()
        time.sleep(5)

    def follow(self):
        ### Click "following" button"
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[3]/a/div').click()
        time.sleep(3)

        ### Follow one from "following"
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[3]/div[3]/button").click()
        time.sleep(3)

        ### Scroll down
        f_ody = self.driver.find_element(By.XPATH, "//div[@class='_aano']")
        scroll = 0
        while scroll < 5:  ### scroll 5 times, or get the real following numbers and use instead.
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', f_ody)
            time.sleep(2)
            scroll += 1



insta_followers = InstaFollower()

insta_followers.login()
insta_followers.find_followers()
insta_followers.follow()