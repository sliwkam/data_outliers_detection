"""
The boxplot_outliers function returns two data sets (DataFrame):
- correct_data - data set that does not contain any outliers,
- outliers_data - a data set containing outliers removed from the original set.
With the appropriate value of the function parameters, up to two box plots can be displayed: the box plot of the input data and the box plot of the output data.
"""

def boxplot_outliers(data, interval, input_plot = False, output_plot = False, input_color = 'blue', output_color = 'green', orientation = 'h'):
    #---imports---
    import pandas as pd
    import seaborn as sns
    import numpy as np
    from scipy import stats
    import statistics as st
    import matplotlib.pyplot as plt
    #------
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    filter = (data < Q1 - interval * IQR) | (data > Q3 + interval *IQR)
    correct_data = data.drop(axis = 0, index = data.loc[filter].index)
    outliers_data = data[filter]
    if output_plot == True and input_plot == True:
        fig, ax =plt.subplots(1,2)
        sns.boxplot(data, ax=ax[0], orient = orientation, color = input_color).set_title('Input data')
        sns.boxplot(correct_data, ax=ax[1], orient = orientation, color = output_color).set_title('Output data')
        plt.tight_layout()
        fig.show()
    elif output_plot == True:
        sns.boxplot(correct_data, orient = orientation, color = output_color).set_title('Output data')
    elif input_plot == True:
        sns.boxplot(data, orient = orientation, color = input_color).set_title('Input data')
    return correct_data, outliers_data
