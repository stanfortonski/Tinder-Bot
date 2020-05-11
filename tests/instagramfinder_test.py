# Author: Stan Fortoński
# Date: 05.05.2020
# Instagram Finder Test

import sys, unittest
sys.path.insert(0, '..')
from time import sleep
from driver import getDriver
from tinder.config import Config
from tinder.login.tinderlogin import TinderLogin
from tinder.finder.instagramfinder import InstagramFinder


class TestIntagramFinder(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = getDriver()
        cls.login = TinderLogin(cls.driver)
        cls.login.logIn()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def setUp(self):
        self.insta = InstagramFinder(self.driver)

    def changeNameScript(self, name):
        while True:
            try:
                self.driver.execute_script('document.querySelector("#content > div > div:nth-child(1) > div > main > div:nth-child(1) > div > div > div:nth-child(1) > div > div:nth-child(1) > div:nth-child(3) > div:nth-child(6) > div > div:nth-child(2) > div > div > span").innerHTML = "'+name+'"');
                break
            except:
                self.driver.get('https://tinder.com/app/recs')
                sleep(5)

    def testInstagramSaving(self):
        testFileName = Config['ig_file_path']
        with open(testFileName, 'w') as file:
            file.write('')

        self.changeNameScript('ig _x_te2st_x_')
        self.assertTrue(self.insta.findAndSaveNick(testFileName))

        self.changeNameScript('ig: _x_te2st_x_')
        self.assertTrue(self.insta.findAndSaveNick(testFileName))

        self.changeNameScript('ig:_x_te2st_x_')
        self.assertTrue(self.insta.findAndSaveNick(testFileName))

        self.changeNameScript('insta _x_te2st_x_')
        self.assertTrue(self.insta.findAndSaveNick(testFileName))

        self.changeNameScript('insta: _x_te2st_x_')
        self.assertTrue(self.insta.findAndSaveNick(testFileName))

        self.changeNameScript('insta:_x_te2st_x_')
        self.assertTrue(self.insta.findAndSaveNick(testFileName))

        self.changeNameScript('instagram _x_te2st_x_')
        self.assertTrue(self.insta.findAndSaveNick(testFileName))

        self.changeNameScript('instagram: _x_te2st_x_')
        self.assertTrue(self.insta.findAndSaveNick(testFileName))

        self.changeNameScript('instagram:_x_te2st_x_')
        self.assertTrue(self.insta.findAndSaveNick(testFileName))

if __name__ == '__main__':
    unittest.main()
