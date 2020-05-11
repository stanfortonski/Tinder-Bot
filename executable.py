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

driver = getDriver()
login = TinderLogin(driver)
bot = TinderBot(driver)
igFinder = InstagramFinder(driver)
snapFinder = SnapchatFinder(driver)

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
        except NoSuchElementException as e:
            print(f'Error: {e}\nReport me: https://github.com/stanfortonski/Tinder-Bot')
            break
else:
    print('Error: Failed to login to Tinder. Check your data or try later.')