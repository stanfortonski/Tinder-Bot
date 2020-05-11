# Author: Stan Fortoński
# Date: 02.05.2020
# Tinder Bot Test

import sys, unittest
sys.path.insert(0, '..')
from time import sleep
from driver import getDriver
from tinder.login.tinderlogin import TinderLogin
from tinder.tinderbot import TinderBot

class TestTinderBot(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = getDriver()
        cls.login = TinderLogin(cls.driver)
        cls.login.logIn()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def setUp(self):
        self.bot = TinderBot(self.driver)
    
    def testLike(self):
        self.bot.like()
        self.assertEqual(self.bot.getTotalLikes(), 1)

    def testDislike(self):
        self.bot.dislike()
        self.assertEqual(self.bot.getTotalDislikes(), 1)

    def testPerform(self):
        self.bot.perform(wait=False)
        self.bot.perform(wait=False)
        self.bot.perform(wait=False)
        self.bot.perform(wait=False)
        self.bot.perform(wait=False)
        self.assertEqual(self.bot.getTotalActions(), 5)

if __name__ == '__main__':
    unittest.main()
