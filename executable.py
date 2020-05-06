# Author: Stan Fortoński
# Date: 02.05.2020
# Proper Executable

from random import random
from driver import getDriver
from tinderlogin import TinderLogin
from tinderbot import TinderBot
from instagramfinder import InstagramFinder
from snapchatfinder import SnapchatFinder
from selenium.common.exceptions import NoSuchElementException
from config import Config

driver = getDriver()
login = TinderLogin(driver)
bot = TinderBot(driver)
igFinder = InstagramFinder(driver)
snapFinder = SnapchatFinder(driver)

login.logIn()
if login.isLogged():
    print('=== Tinder Perform ===')
    while True:
        try:     
            bot.perform()
            if Config['allow_to_save_ig']:
                igFinder.findAndSaveInstagramNick()
            if Config['allow_to_save_snap']:
                snapFinder.findAndSaveSnapchatNick()
            if bot.getTotalActions() % 10 == 0:
                print(bot)
                print(igFinder)
                print(snapFinder)
        except NoSuchElementException as e:
            print(f'Error: {e}\nReport me: https://github.com/stanfortonski/Tinder-Bot')
            break
else:
    print('Error: Failed to login to Tinder. Check your data or try later.')