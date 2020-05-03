# Author: Stan Fortoński
# Date: 02.05.2020
# Login To Google

from time import sleep
from selenium.webdriver.common.keys import Keys
from config import Config

class GoogleLogin:
    def __init__(self, driver):
        self.driver = driver
        self.login = Config['google']['login']
        self.password = Config['google']['password']
        self.__isLogged = False

    def logIn(self):
        print('=== Google Login ===')
        driver = self.driver
        driver.get('https://accounts.google.com/signin')
        sleep(1)
        driver.find_element_by_id('identifierId').send_keys(self.login)
        driver.find_element_by_id('identifierNext').click()
        sleep(1)
        driver.find_element_by_css_selector('#password > div:first-child > div > div:first-child > input').send_keys(self.password)
        driver.find_element_by_id('passwordNext').click()
        sleep(1)
        self.__isLogged = 'myaccount.google.com' in driver.current_url

    def isLogged(self):
        return self.__isLogged