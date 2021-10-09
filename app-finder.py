# Author: Stan Fortoński
# Date: 06.05.2020
# IG/Snap Finder Executable

from driver import getDriver
from tinder.login.tinderlogin import TinderLogin
import tinder.functions as fn
from tinder.finder.instagramfinder import InstagramFinder
from tinder.finder.snapchatfinder import SnapchatFinder
from selenium.common.exceptions import NoSuchElementException

driver = getDriver()
login = TinderLogin(driver)
igFinder = InstagramFinder(driver)
snapFinder = SnapchatFinder(driver)

print('=== Tinder Finder ===')
login.logIn()
if login.isLogged():
    print('=== Instagram/Snapchat Finding ===')
    while True:
        try:
            driver.get('https://tinder.com/app/recs')
            fn.waitForPeople(driver)
            igFinder.findAndSaveInstagramNick()
            snapFinder.findAndSaveSnapchatNick()
            if igFinder.getTotalSaves() != 0 and igFinder.getTotalSaves() % 10 == 0:
                print(igFinder, snapFinder)
            fn.waitRandomTime()
        except:
            fn.waitRandomTime()
else:
    print('Error: Failed to login to Tinder. Check your data or try later.')