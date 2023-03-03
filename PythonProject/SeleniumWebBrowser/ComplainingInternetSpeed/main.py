import time
from selenium import webdriver
from selenium.webdriver.common.by import By


TWITTER_EMAIL = "jcoffee155@gmail.com"
TWITTER_PASSWORD = ""
USERNAME = "jcoffee155"
PROMISED_DOWN = 150
PROMISED_UP = 10


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        twitter_url = "https://twitter.com/"
        internet_speed_website_url = "https://www.speedtest.net/"

        self.driver.get(internet_speed_website_url)
        time.sleep(5)

        self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]").click()
        download_speed = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span")
        upload_speed = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span")
        message = f"Download speed : {download_speed.text}, Upload speed : {upload_speed.text}"

        time.sleep(60)
        self.driver.get(twitter_url)
        time.sleep(5)

        login_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/a/div/span/span")
        login_button.click()
        time.sleep(3)

        input_email = self.driver.find_element(By.NAME, "text")
        input_email.send_keys(TWITTER_EMAIL)
        time.sleep(3)

        next_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div")
        next_button.click()
        time.sleep(3)

        username_button = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")
        username_button.send_keys(USERNAME)
        time.sleep(3)

        next_button_2 = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div")
        next_button_2.click()
        time.sleep(3)

        input_password = self.driver.find_element(By.NAME, "password")
        input_password.send_keys(TWITTER_PASSWORD)
        time.sleep(3)

        login_button_2 = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div")
        login_button_2.click()
        time.sleep(3)

        input_tweet = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div")
        input_tweet.click()
        input_tweet_2 = self.driver.find_element(By.XPATH, '//div[contains(@aria-label, "Tweet text")]')
        input_tweet_2.send_keys(message)
        time.sleep(3)

        tweet_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span")
        tweet_button.click()


    def tweet_at_provider(self):
        pass


internet_speed = InternetSpeedTwitterBot()

internet_speed.get_internet_speed()
internet_speed.tweet_at_provider()

