# Author: Stan Fortoński
# Date: 02.05.2020
# Proper Executable

import sys
from random import random
from driver import getDriver
from tinderlogin import TinderLogin
from tinderbot import TinderBot
from selenium.common.exceptions import NoSuchElementException

driver = getDriver()
login = TinderLogin(driver)
bot = TinderBot(driver)

login.logIn()
if login.isLogged():
    print('=== Tinder Perform ===')
    while True:
        try:
            bot.perform()
            if bot.getTotalActions() % 10 == 0:
                bot.show()
        except NoSuchElementException as e:
            print(f'Error: {e}\nReport me: https://github.com/stanfortonski/Tinder-Bot')
            sys.exit()
else:
    print('Error: Failed to login to Tinder. Check your data or try later.')

    