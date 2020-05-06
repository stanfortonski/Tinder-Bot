# Author: Stan Fortoński
# Date: 05.05.2020
# Instagram Finder

import re
from config import Config
from selenium.common.exceptions import NoSuchElementException

class InstagramFinder:
    def __init__(self, driver):
        self.__instaPattern = re.compile('(ig|insta|instagram):? ?[\w.]+')
        self.driver = driver
        self.__totalInstaSaves = 0

    def findAndSaveInstagramNick(self, fileName=Config['ig_file_path']):
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
            nick = self.__instaPattern.search(description.lower())
            if nick is not None:
                self.__saveData(fileName, name, age, distance, nick.group(), description)
                self.__totalInstaSaves += 1
                return True
            else:
                return False
        except NoSuchElementException:
            return False

    def __saveData(self, fileName, name, age, distance, igNick, desc):
        with open(fileName, 'a') as file:
            file.write(f'{name} {age} {distance} {igNick} | {desc}')

    def __str__(self):
        if Config['allow_to_save_ig']:
            return f'\n* Total Instagram saves: {self.__totalInstaSaves}'
        return ''

    def getTotalInstagramSaves(self):
        return self.__totalInstaSaves