# Author: Stan Fortoński
# Date: 06.05.2020
# Description Finder

import re
from selenium.common.exceptions import NoSuchElementException

class Finder:
    def __init__(self, driver, pattern):
        self.__pattern = re.compile(pattern)
        self.driver = driver
        self.__totalSaves = 0

    def findAndSaveNick(self, fileName):
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
            nick = self.__pattern.search(description.lower())
            if nick is not None:
                self.__saveData(fileName, name, age, distance, nick.group())
                self.__totalSaves += 1
                return True
            else:
                return False
        except NoSuchElementException:
            return False

    def __saveData(self, fileName, name, age, distance, nickname):
        with open(fileName, 'a') as file:
            file.write(f'\n{name} {age} {distance} {nickname}')

    def getTotalSaves(self):
        return self.__totalSaves