import pandas as pd

class Import_Dataset():

    def __init__(self, inputUrl, inputNames):
        self.__dataset = []
        self.url = inputUrl
        self.names = inputNames

    def execute(self):
        try:
            print('Importing dataset from : '+ self.getUrl())
            print('With values : ', self.getNames())
            
            self.importing()
            imported_dataset = self.__dataset

            return imported_dataset
        except:
            print('An error occurred during the execution of import dataset main body')
    
    def getUrl(self):
        return self.url

    def getNames(self):
        return self.names

    def importing(self):
        self.__dataset = pd.read_csv(self.url, names=self.names)