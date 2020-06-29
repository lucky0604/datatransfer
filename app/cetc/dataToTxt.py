import os
import pandas as pd


class DataToTxt(object):
    def __init__(self, dirName):
        self.dirName = dirName

    def transferData(self, file):
        if file.split('.')[2] != 'py':
            json_file = pd.read_json(file)
            # print(len(json_file))
            # print(range(len(json_file)))
            for i in range(len(json_file)):
                # print(i)
                txtFile = json_file.loc[i]
                # print(txtFile)
                if len(txtFile.Data) > 0:
                    data = txtFile.Data['classifications']
                    result = []
                    result.append(txtFile.imageName)
                    for j in data:
                        result.append(j['activeOption'])
                    final = ' '.join(result)
                    with open(txtFile.imageName.split('.')[0] + '.txt', 'w') as file_handle:
                        file_handle.write(final)
                        file_handle.write(' ')

    def getData(self, dirName):
        files = []
        for root, dirs, filename in os.walk(dirName):
            for singleFile in filename:
                self.transferData(os.path.join(root, singleFile))


transDir = DataToTxt('./')
transDir.getData('./')
