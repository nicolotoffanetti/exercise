from sklearn.preprocessing import StandardScaler

class dataNormalizer():

    def __init__(self, inputDataset, inputFeaturesLabel):
        self.dataset = inputDataset
        self.features = inputFeaturesLabel[:-1]
        self.lables = inputFeaturesLabel[-1]
    
    def execute(self):
        try:
            # Separating the features
            x = self.dataset.loc[:, self.features].values
            # Separating the class
            y = self.dataset.loc[:,self.lables].values
            y = self.collectLabels(y)

            # Standardizing the features
            x = StandardScaler().fit_transform(x)

            return x,y
        except:
            print('An error occurred during execution of dataNormalizer main body')

    def collectLabels(self, inputLabels):
        aCollectedLabels = []

        for aElement in inputLabels:
            if aElement not in (aCollectedLabels):
                aCollectedLabels.append(aElement)
        
        return aCollectedLabels







