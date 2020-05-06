# Author: Stan Fortoński
# Date: 02.05.2020
# Login To Google Test

import unittest
from driver import getDriver
from googlelogin import GoogleLogin

class TestGoogleLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = getDriver()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def setUp(self):
        self.gl = GoogleLogin(self.driver)

    def testLogin(self):
        self.gl.logIn()
        self.assertTrue(self.gl.isLogged())

if __name__ == '__main__':
    unittest.main()
