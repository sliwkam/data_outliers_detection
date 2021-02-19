# The zscore_outliers function returns two data sets (DataFrame):
# - correct_data - data set that does not contain any outliers,
# - outliers_data - a data set containing outliers removed from the original set.
# With the appropriate value of the function parameters, up to two distribution plots can be displayed: the distribution plot of the input data and the distribution plot of the output data.


def zscore_outliers(data, std_value, input_plot = False, output_plot = False, input_color = 'blue', output_color = 'green'):
    #---imports---
    import pandas as pd
    import seaborn as sns
    import numpy as np
    from scipy import stats
    import statistics as st
    import matplotlib.pyplot as plt
    #------
    data_std = data.std()
    data_mean = data.mean()
    cut_off = data_std * std_value
    lower_limit  = data_mean - cut_off 
    upper_limit = data_mean + cut_off
    filter = (data > upper_limit) | (data < lower_limit)
    outliers_data = data.loc[filter]
    correct_data = data.drop(axis = 0, index = data.loc[filter].index) 
    if output_plot == True and input_plot == True:
        fig, ax = plt.subplots(1,2, sharex=True)
        sns.distplot(correct_data, ax=ax[1], hist = False, kde = True, kde_kws = {'linewidth': 3, 'color': output_color}).set_title('Output data')
        sns.distplot(data, ax=ax[0], hist = False, kde = True, kde_kws = {'linewidth': 3, 'color': input_color}).set_title('Input data')
    elif input_plot == True:
        sns.distplot(data, hist = False, kde = True, kde_kws = {'linewidth': 3, 'color': input_color}).set_title('Input data')
        sns.xlim(min_lim, max_lim)
    elif output_plot == True:
        sns.distplot(correct_data, hist = False, kde = True, kde_kws = {'linewidth': 3, 'color': output_color}).set_title('Output data')
        sns.xlim(min_lim, max_lim)
    return correct_data, outliers_data
