# Author: Stan Fortoński
# Date: 02.05.2020
# Login To Facebook Test

import unittest
from driver import getDriver
from facebooklogin import FacebookLogin

class TestFacebookLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = getDriver()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def setUp(self):
        self.fb = FacebookLogin(self.driver)

    def testLogin(self):
        self.fb.logIn()
        self.assertTrue(self.fb.isLogged())

if __name__ == '__main__':
    unittest.main()
