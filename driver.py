# Author: Stan Fortoński
# Date: 02.05.2020
# Driver With Geo Location

from selenium import webdriver

def getDriver():
    geoEnable = webdriver.FirefoxOptions()
    geoEnable.set_preference('geo.enabled', True)
    geoEnable.set_preference('geo.provider.use_corelocation', True);
    geoEnable.set_preference('geo.prompt.testing', True);
    geoEnable.set_preference('geo.prompt.testing.allow', True);
    return webdriver.Firefox(options=geoEnable)