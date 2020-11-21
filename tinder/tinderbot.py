# Author: Stan Fortoński
# Date: 02.05.2020
# Tinder Bot

import sys
from time import sleep
from random import randrange
from tinder.config import Config
import tinder.functions as fn
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException

class TinderBot:
    def __init__(self, driver):
        self.driver = driver
        self.__totalLikes = 0
        self.__totalDislikes = 0

    def perform(self, wait=True):
        if 'app/recs' in self.driver.current_url:
            self.__doOutOfLikesPopup()
            fn.waitForPeople(self.driver)
            chanceToLike = randrange(1, 100)
            if chanceToLike <= Config['chance_to_like']:
                self.like()
            else:
                self.dislike()
            if wait:
                fn.waitRandomTime()

    def __doOutOfLikesPopup(self):
        driver = self.driver
        try:
            driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[2]/div[1]/div/div[1]/div/div/span/div/div/div[1]/div')
            print('Sorry, you do not have any likes for now. Try later.')
            sys.exit()
        except NoSuchElementException:
            pass

    def like(self):
        try:
            self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button').click()
            self.__totalLikes += 1
        except ElementClickInterceptedException:
            self.solveProblems()
            sleep(2)
            
    def dislike(self):
        try:
            self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button').click()
            self.__totalDislikes += 1
        except ElementClickInterceptedException:
            self.solveProblems()
            sleep(2)

    def solveProblems(self):
        try:
            self.driver.find_element_by_xpath('/html/body/div[2]/div/div/button[2]').click()
        except NoSuchElementException:
            pass

        try:
            self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[2]/div/div/div[1]/div/div[4]/button').click()
        except NoSuchElementException:
            pass
        

    def __str__(self):
        total = self.getTotalActions()
        return f'=== Tinder results ===\n* Total actions: {total}\n* Total likes: {self.__totalLikes}\n* Total disLikes: {self.__totalDislikes}'

    def getTotalActions(self):
        return self.__totalLikes + self.__totalDislikes
    
    def getTotalLikes(self):
        return self.__totalLikes

    def getTotalDislikes(self):
        return self.__totalDislikes