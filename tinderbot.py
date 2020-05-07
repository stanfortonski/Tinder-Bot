# Author: Stan Fortoński
# Date: 02.05.2020
# Tinder Bot

import sys
import random
from time import sleep
from config import Config
from selenium.common.exceptions import NoSuchElementException

class TinderBot:
    def __init__(self, driver):
        self.driver = driver
        self.__totalLikes = 0
        self.__totalDislikes = 0

    def perform(self, wait=True):
        if 'app/recs' in self.driver.current_url:
            self.__doOutOfLikesPopup()
            waitForPeople(driver)
            chanceToLike = random.randrange(1, 100)
            if chanceToLike <= Config['chance_to_like']:
                self.like()
            else:
                self.dislike()
            if wait:
                sleep(getWaitTimeInSec())

    def __doOutOfLikesPopup(self):
        driver = self.driver
        try:
            driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[2]/div[1]/div/div[1]/div/div/span/div/div/div[1]/div')
            print('Sorry, you do not have any likes for now. Try later.')
            sys.exit()
        except NoSuchElementException:
            pass

    def like(self):
        self.__totalLikes += 1
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button').click()

    def dislike(self):
        self.__totalDislikes += 1
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button').click()

    def __str__(self):
        total = self.getTotalActions()
        return f'=== Tinder results ===\n* Total actions: {total}\n* Total likes: {self.__totalLikes}\n* Total disLikes: {self.__totalDislikes}'

    def getTotalActions(self):
        return self.__totalLikes + self.__totalDislikes
    
    def getTotalLikes(self):
        return self.__totalLikes

    def getTotalDislikes(self):
        return self.__totalDislikes

def getWaitTimeInSec():
    maxTime = Config['max_wait_time_between_action_in_sec']
    minTime = Config['min_wait_time_between_action_in_sec']
    return max(min(random.random() * maxTime, maxTime), minTime)

def waitForPeople(driver):
    while True:
        try:
            element = driver.find_element_by_css_selector('.beacon__circle')
            sleep(30)
        except NoSuchElementException:
            break