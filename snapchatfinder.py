# Author: Stan Fortoński
# Date: 06.05.2020
# Snap Finder

import re
from config import Config
from selenium.common.exceptions import NoSuchElementException

class SnapchatFinder:
    def __init__(self, driver):
        self.__snapPattern = re.compile('(snap|snapchat):? ?[\w.]+')
        self.driver = driver
        self.__totalSnapSaves = 0

    def findAndSaveSnapchatNick(self, fileName=Config['snap_file_path']):
        driver = self.driver
        name = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[6]/div/div[1]/div/div/span').get_attribute('innerHTML')
        age = ''
        distance = ''
        try:
            age = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[6]/div/div[1]/div/span').get_attribute('innerHTML')
        except NoSuchElementException:
           pass

        try:
            distance = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[6]/div/div[2]/div/div/div/div[2]').get_attribute('innerHTML')
        except NoSuchElementException:
           pass   

        try:
            description = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[6]/div/div[2]/div/div/span').get_attribute('innerHTML')
            nick = self.__snapPattern.search(description.lower())
            if nick is not None:
                self.__saveData(fileName, name, age, distance, nick.group(), description)
                self.__totalSnapSaves += 1
                return True
            else:
                return False
        except NoSuchElementException:
            return False

    def __saveData(self, fileName, name, age, distance, snapNick, desc):
        with open(fileName, 'a') as file:
            file.write(f'{name} {age} {distance} {snapNick} | {desc}')

    def __str__(self):
        if Config['allow_to_save_snap']:
            return f'\n* Total Snapchat saves: {self.__totalSnapSaves}'
        return ''

    def getTotalSnapchatSaves(self):
        return self.__totalSnapSaves