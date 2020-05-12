import pandas as pd
from sklearn.decomposition import PCA

class bidimensionalPCA():
    def __init__(self, inputNormalizedFeatures, inputLabelabelColumn):
        self.normalizedDataset = inputNormalizedFeatures
        self.labelColumn = inputLabelabelColumn

    def execute(self):
        try:
            pca = PCA(n_components = 2)
            principalComponents = pca.fit_transform(self.normalizedDataset)
            partialDataFrame = pd.DataFrame(data = principalComponents, 
                    columns = ['principal component 1', 'principal component 2'])
            
            finalDataFrame = pd.concat([partialDataFrame, self.labelColumn], axis = 1) 
            
            return finalDataFrame 
        except:
            print('An error occurred during the execution of bidimensionalPCA main body')