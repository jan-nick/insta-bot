from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time
import math

class InstaBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/accounts/login/')
        time.sleep(2)
        email = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(2)
        ui.WebDriverWait(bot, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".aOOlW.HoLwm"))).click()
    
    def like(self):
        bot = self.bot
        for i in range(1, 20):
            bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(3)
            posts = bot.find_elements_by_tag_name('article')
            for elem in posts:
                try:
                    bot.find_element_by_class_name('glyphsSpriteHeart__outline__24__grey_9').click()
                    time.sleep(1)
                except Exception as ex:
                    time.sleep(2)
                    

user = InstaBot('zionlp15@gmail.com', 'instaBot')
user.login()
user.like()