# Author: Stan Fortoński
# Date: 02.05.2020
# Login To Facebook

from time import sleep
from tinder.config import Config
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
        try:
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="cookie-policy-banner-accept"]'))) 
        finally:
            element.click()

        driver.find_element_by_xpath('//*[@id="email"]').send_keys(self.login)
        driver.find_element_by_xpath('//*[@id="pass"]').send_keys(self.password)
        driver.find_element_by_css_selector('[data-testid="royal_login_button"]').submit()
        sleep(6)
        try:
            element = driver.find_element_by_css_selector('input[type="search"]')
            self.__isLogged = True
        except NoSuchElementException:
            self.__isLogged = False

    def isLogged(self):
        return self.__isLogged