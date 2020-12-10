# Author: Stan Fortoński
# Date: 02.05.2020
# Login To Tinder

from time import sleep
from tinder.config import Config
from tinder.login.googlelogin import GoogleLogin
from tinder.login.facebooklogin import FacebookLogin
from selenium.common.exceptions import NoSuchElementException

class TinderLogin:
    def __init__(self, driver, type = Config['login_method']):
        self.driver = driver
        self.type = type
        self.__isLogged = False
        if type == 'google':
            self.methodLogin = GoogleLogin(driver)
        elif type == 'facebook':
            self.methodLogin = FacebookLogin(driver)
        else:
            raise RuntimeError('Undefined or unrecognized login method to Tinder')

    def logIn(self):
        driver = self.driver
        self.methodLogin.logIn()
        if self.methodLogin.isLogged:
            works = False
            for i in range(0, Config['amount_of_login_attempts']):
                try:
                    print('=== Tinder login ===')
                    driver.execute_script('document.cookie = ""; localStorage.clear(); sessionStorage.clear();')
                    driver.get('https://tinder.com/')
                    sleep(2)
                    self.chooseLang()
                    sleep(2)
                    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button').click()
                    sleep(2)
                    if self.type == 'google':
                        self.__logInViaGoogle()
                    else:
                        self.__logInViaFacebook()
                    sleep(5)
                    self.__isLogged = 'tinder.com/app/recs' in driver.current_url
                    if self.__isLogged:
                        self.__closePopups()
                    works = True
                    break
                except NoSuchElementException:
                    works = False

            if not works:
                driver.close()
                print('Error: Login is no available now. Try later.')

    def __logInViaGoogle(self):
        button = self.driver.find_element_by_css_selector('button[aria-label~="Google"]')
        button.click()

    def __logInViaFacebook(self):
        driver = self.driver
        button = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button')
        if 'Facebook' in button.get_attribute('innerHTML'):
            button.click()
        else:
            driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/span/button').click()
            sleep(1)
            driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/span/div[3]/button').click()
            
    def __closePopups(self):
        driver = self.driver
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[1]/button').click()
        driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]').click()
        sleep(2)
        driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]').click()
        sleep(2)
        try:
            element = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/a')
            element.click()
            driver.get('https://tinder.com/app/recs')
            sleep(2)
        except NoSuchElementException:
            pass
       
    def isLogged(self):
        return self.__isLogged

    def chooseLang(self):
        try:
            self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/ul/li[1]/button').click()
        except NoSuchElementException:
            pass