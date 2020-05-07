# Author: Stan Fortoński
# Date: 02.05.2020
# Proper Executable

from random import random
from time import sleep
from driver import getDriver
from tinderlogin import TinderLogin
from tinderbot import getWaitTimeInSec
from tinderbot import waitForPeople
from instagramfinder import InstagramFinder
from snapchatfinder import SnapchatFinder
from selenium.common.exceptions import NoSuchElementException

driver = getDriver()
login = TinderLogin(driver)
igFinder = InstagramFinder(driver)
snapFinder = SnapchatFinder(driver)

print('=== Tinder Finder Only Start ===')
login.logIn()
if login.isLogged():
    print('=== Instagram/Snapchat Finding ===')
    while True:
        try:
            driver.get('https://tinder.com/app/recs')
            waitForPeople(driver)
            igFinder.findAndSaveInstagramNick()
            snapFinder.findAndSaveSnapchatNick()
            if igFinder.getTotalSaves() != 0 and igFinder.getTotalSaves() % 10 == 0:
                print(igFinder, snapFinder)
            sleep(getWaitTimeInSec())
        except NoSuchElementException as e:
            print(f'Error: {e}\nReport me: https://github.com/stanfortonski/Tinder-Bot')
            break
else:
    print('Error: Failed to login to Tinder. Check your data or try later.')