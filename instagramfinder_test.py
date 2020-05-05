# Author: Stan Fortoński
# Date: 05.05.2020
# Instagram Finder Test

import unittest
from time import sleep
from tinderlogin import TinderLogin
from instagramfinder import InstagramFinder
from driver import getDriver

class TestIntagramFinder(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = getDriver()
        cls.login = TinderLogin(cls.driver)
        cls.login.logIn()

    @classmethod
    def tearDownClass(cls):
        pass #cls.driver.close()

    def setUp(self):
        self.insta = InstagramFinder(self.driver)

    def testInstagramSaving(self):
        testFileName = 'ig_test.txt'
        with open(testFileName, 'w') as file:
            file.write('')

        while True:
            self.driver.get('https://tinder.com/app/recs')
            sleep(5)
            result = self.insta.findAndSaveInstagramNick(fileName=testFileName)
            if result == True:
                self.assertTrue(True)
                break

if __name__ == '__main__':
    unittest.main()
