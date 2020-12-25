# Author: Stan Fortoński
# Date: 02.05.2020
# Proper Executable

from random import random
from driver import getDriver
from tinder.login.tinderlogin import TinderLogin
from tinder.tinderbot import TinderBot
from tinder.finder.instagramfinder import InstagramFinder
from tinder.finder.snapchatfinder import SnapchatFinder
from selenium.common.exceptions import NoSuchElementException
from tinder.config import Config
from time import sleep

driver = getDriver()
login = TinderLogin(driver)
bot = TinderBot(driver)
igFinder = InstagramFinder(driver)
snapFinder = SnapchatFinder(driver)
errors = 0

print('=== TinderBot Start ===')
login.logIn()
if login.isLogged():
    print('=== Tinder Perform ===')
    while True:
        try:     
            bot.perform()
            igFinder.findAndSaveInstagramNick()
            snapFinder.findAndSaveSnapchatNick()
            if bot.getTotalActions() % 10 == 0:
                print(bot, igFinder, snapFinder)
            errors = 0
        except NoSuchElementException as e:
            errors += 1
            if errors >= Config['amount_of_avoid_errors']:
                print(f'Error: {e}\nReport me: https://github.com/stanfortonski/Tinder-Bot')
                break
            else:
                driver.get('https://tinder.com/app/recs')
                sleep(5)
else:
    print('Error: Failed to login to Tinder. Check your data or try later.')