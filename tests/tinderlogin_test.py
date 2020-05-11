# Author: Stan Fortoński
# Date: 02.05.2020
# Login To Tinder Test

import sys, unittest
sys.path.insert(0, '..')
from driver import getDriver
from tinder.login.tinderlogin import TinderLogin

class TestTinderLogin(unittest.TestCase):
    def setUp(self):
        self.driver = getDriver()

    def tearDown(self):
        self.driver.close()

    def testGoogleLogin(self):
        tl = TinderLogin(self.driver, type='google')
        tl.logIn()
        self.assertTrue(tl.isLogged())

    def testFacebookLogin(self):
        tl = TinderLogin(self.driver, type='facebook')
        tl.logIn()
        self.assertTrue(tl.isLogged())

if __name__ == '__main__':
    unittest.main()
