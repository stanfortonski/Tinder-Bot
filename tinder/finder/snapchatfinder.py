# Author: Stan Fortoński
# Date: 06.05.2020
# Snapchat Finder

from tinder.config import Config
from tinder.finder.finder import Finder

class SnapchatFinder(Finder):
    def __init__(self, driver):
        super().__init__(driver, '(snap|snapchat):? ?[\w.]+')

    def findAndSaveSnapchatNick(self):
        if Config['allow_to_save_snap']:
            return self.findAndSaveNick(Config['snap_file_path'])
        else:
            return False

    def __str__(self):
        if Config['allow_to_save_snap']:
            saves = self.getTotalSaves()
            return f'\n* Total Snapchat saves: {saves}'
        return ''