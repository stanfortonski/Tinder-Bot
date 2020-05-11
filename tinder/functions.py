# Author: Stan Fortoński
# Date: 07.05.2020
# Additional Functions

from random import random
from time import sleep
from tinder.config import Config
from selenium.common.exceptions import NoSuchElementException

def waitRandomTime():
    maxTime = Config['max_wait_time_between_action_in_sec']
    minTime = Config['min_wait_time_between_action_in_sec']
    sleep(max(min(random() * maxTime, maxTime), minTime))

def waitForPeople(driver):
    while True:
        try:
            element = driver.find_element_by_css_selector('.beacon__circle')
            sleep(20)
        except NoSuchElementException:
            break