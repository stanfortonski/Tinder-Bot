# Author: Stan Fortoński
# Date: 02.05.2020
# Proper Executable

from random import random
from driver import getDriver
from tinderlogin import TinderLogin
from tinderbot import TinderBot
from selenium.common.exceptions import NoSuchElementException

try:
    driver = getDriver()
    login = TinderLogin(driver)
    bot = TinderBot(driver)

    login.logIn()
    if login.isLogged():
        while True:
            try:
                bot.perform()
                if bot.getTotalActions() % 10 == 0:
                    bot.show()
            except NoSuchElementException:
                print('Warning: Can\'t find element.')
    else:
        print('Error: Failed to login to Tinder. Check your data or try later.')
except:
    print('Error: Something was missing. Report me: https://github.com/stanfortonski/Tinder-Bot')