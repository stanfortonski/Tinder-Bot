# Author: Stan Fortoński
# Date: 05.05.2020
# Instagram Finder

from tinder.config import Config
from tinder.finder.finder import Finder

class InstagramFinder(Finder):
    def __init__(self, driver):
        super().__init__(driver, '(ig|insta|instagram):? ?[\w.]+')

    def findAndSaveInstagramNick(self):
        if Config['allow_to_save_ig']:
            return self.findAndSaveNick(Config['ig_file_path'])
        else:
            return False

    def __str__(self):
        if Config['allow_to_save_ig']:
            saves = self.getTotalSaves()
            return f'\n* Total Instagram saves: {saves}'
        return ''