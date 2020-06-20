import os


class DataToTxt(object):
    def __init__(self, dirName):
        self.dirName = dirName

    def transferData(self, file):
        print(file, ' ----- file --------')

    def getData(self, dirName):
        files = []
        for root, dirs, filename in os.walk(dirName):
            for singleFile in filename:
                self.transferData(os.path.join(root, singleFile))


transDir = DataToTxt('./')
transDir.getData('./')
