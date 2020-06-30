import os
import pandas as pd

class DataTransfer(object):

    def __init__(self, dirName):
        self.dirName = dirName

    def transferData(self, file):
        if file.split('.')[2] != 'py' and file.split('.')[2] != 'xml':
            print(file, ' file -----')


    def getData(self, dirName):
        files = []
        for root, dirs, filename in os.walk(dirName):
            for singleFile in filename:
                self.transferData(os.path.join(root, singleFile))

transDir = DataTransfer('./')
transDir.getData('./')
