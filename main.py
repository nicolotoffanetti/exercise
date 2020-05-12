import test.data_pre_treatment_test
from src.import_dataset import Import_Dataset
from src.data_pre_treatment import dataNormalizer
from src.principal_component_analysis import bidimensionalPCA
from src.my_plot import myPlot

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']

def main():
    print('Executing main')

    try:
        # import dataset
        dataset = Import_Dataset(url, names).execute()
        # data pretreatment 
        myNormalizedDataset, labels = dataNormalizer(dataset, names).execute()
        # principal component analysis
        PCADataset = bidimensionalPCA(myNormalizedDataset, dataset[names[-1]]).execute()
        # produce the plot
        myPlot(PCADataset, labels).makePlot()

    except:
        print('An error occurred in executing main block')

if __name__ == '__main__':
    main()