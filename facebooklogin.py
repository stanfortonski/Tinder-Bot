# Author: Stan Fortoński
# Date: 02.05.2020
# Login To Facebook

from time import sleep
from config import Config

class FacebookLogin:
    def __init__(self, driver):
        self.driver = driver
        self.login = Config['facebook']['login']
        self.password = Config['facebook']['password']
        self.__isLogged = False

    def logIn(self):
        print('=== Facebook Login ===')
        driver = self.driver
        driver.get('https://www.facebook.com/')
        driver.find_element_by_xpath('//*[@id="email"]').send_keys(self.login)
        driver.find_element_by_xpath('//*[@id="pass"]').send_keys(self.password)
        driver.find_element_by_xpath('//*[@id="u_0_b"]').submit()
        sleep(6)
        try:
            element = driver.find_element_by_partial_link_text('Log out')
            self.__isLogged = False
        except:
            self.__isLogged = True

    def isLogged(self):
        return self.__isLogged