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
            try:
                self.__doOutOfLikesPopup()
                fn.waitForPeople(self.driver)
                chanceToLike = randrange(1, 100)
                if chanceToLike <= Config['chance_to_like']:
                    self.like()
                else:
                    self.dislike()
                if wait:
                    fn.waitRandomTime()
            except SystemExit:
                raise
            except Exception:
                self.driver.get('https://tinder.com/app/recs')
                fn.waitRandomTime()

    def __doOutOfLikesPopup(self):
        driver = self.driver
        try:
            xpath_out_of_likes = '/html/body/div[2]/div/div/div[1]/div[2]/div[1]/span[1]/div/div/span/div/h3'
            driver.find_element_by_xpath(xpath_out_of_likes)
            print('Sorry, you do not have any likes for now. Try later.')
            sys.exit(1)
        except NoSuchElementException:
            pass

    def like(self):
        success = None
        likesButtons = ['/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button', '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button']
        for button in likesButtons:
            try:                                    
                self.driver.find_element_by_xpath(button).click()
                self.__totalLikes += 1
                success = True
                break
            except (ElementClickInterceptedException, NoSuchElementException):
                continue

        if not success:
            self.solveProblems()
            sleep(2)
            
    def dislike(self):
        success = None
        dislikesButtons = ['/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button', '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[2]/button']
        for button in dislikesButtons:
            try:                                    
                self.driver.find_element_by_xpath(button).click()
                self.__totalDislikes += 1
                success = True
                break
            except (ElementClickInterceptedException, NoSuchElementException):
                continue
        
        if not success:
            self.solveProblems()
            sleep(2)

    def solveProblems(self):
        try:
            self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[3]/button[2]').click()
        except (ElementClickInterceptedException, NoSuchElementException):
            pass

        try:                                    
            self.driver.find_element_by_xpath('/html/body/div[2]/div/div/button[2]').click()
        except (ElementClickInterceptedException, NoSuchElementException):
            pass

        try:
            self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[2]/div/div/div[1]/div/div[4]/button').click()
        except (ElementClickInterceptedException, NoSuchElementException):
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
