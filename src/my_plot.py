import matplotlib.pyplot as plt

class myPlot():
    def __init__(self, inputDataframe, inputLabels):
        self.__labels = inputLabels
        self.__dataFrame = inputDataframe

    def makePlot(self):
        try:
            labels = self.__dataFrame.columns.values

            fig = plt.figure(figsize = (8,8))
            ax = fig.add_subplot(1,1,1) 
            ax.set_xlabel('Principal Component 1', fontsize = 15)
            ax.set_ylabel('Principal Component 2', fontsize = 15)
            ax.set_title('2 component PCA', fontsize = 20)
            targets = self.__labels
            colors = ['r', 'g', 'b']
            for target, color in zip(targets, colors):
                indicesToKeep = self.__dataFrame[labels[-1]] == target
                ax.scatter(self.__dataFrame.loc[indicesToKeep, labels[0]]
                    , self.__dataFrame.loc[indicesToKeep, labels[1]]
                    , c = color
                    , s = 50)
            ax.legend(targets)
            ax.grid()

            plt.tight_layout()
            plt.savefig('scatter_plot.png')

            print('your plot has been saved in scatter_plot.png')

        except:
            print('An error occurred during the mainPlot execution')