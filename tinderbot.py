# Author: Stan Fortoński
# Date: 02.05.2020
# Tinder Bot

import random
import sys
from time import sleep
from config import Config
from selenium.common.exceptions import NoSuchElementException

class TinderBot:
    def __init__(self, driver):
        self.driver = driver
        self.__totalLikes = 0
        self.__totalDislikes = 0
        self.__totalMatches = 0

    def perform(self):
        if 'app/recs' in self.driver.current_url:
            self.__doMatch()
            self.__doOutOfLikesPopup()
            chanceToLike = random.randrange(1, 100)
            if chanceToLike <= Config['chance_to_like']:
                self.like()
            else:
                self.dislike()
            sleep(self.__getWaitTimeInSec())

    def __doOutOfLikesPopup(self):
        driver = self.driver
        try:
            driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[2]/div[1]/div/div[1]/div/div/span/div/div/div[1]/div')
            print('Sorry, you do not have any likes for now. Try later.')
            sys.exit()
        except NoSuchElementException:
            pass

    def __doMatch(self):
        try:        
            mess = Config['match_message']
            if len(mess) == 0:
                pass
            else:
                pass
        except NoSuchElementException:
            pass

    def __closeMatch(self):
        pass

    def __sendMessage(self):
        pass

    def like(self):
        self.__totalLikes += 1
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button').click()

    def dislike(self):
        self.__totalDislikes += 1
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button').click()

    def __str__(self):
        total = self.getTotalActions()
        return f'Total actions: {total}\nTotal likes: {self.__totalLikes}\nTotal disLikes: {self.__totalDislikes}\n Total matches: {self.__totalMatches}'

    def show(self):
        print(self)

    def __getWaitTimeInSec(self):
        maxTime = Config['max_wait_time_between_action_in_sec']
        minTime = Config['min_wait_time_between_action_in_sec']
        return max(min(random.random() * maxTime, maxTime), minTime)

    def getTotalActions(self):
        return self.__totalLikes + self.__totalDislikes

    def getTotalMatches(self):
        return self.__totalMatches
    
    def getTotalLikes(self):
        return self.__totalLikes

    def getTotalDislikes(self):
        return self.__totalDislikes