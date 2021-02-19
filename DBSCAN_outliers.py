# The DBSCAN_outliers function returns two data sets (DataFrame):
# - correct_data - data set that does not contain any outliers,
# - outliers_data - a data set containing outliers removed from the original set.
# DBSCAN algorithm has been implemented in the DBSCAN function in the Scikit-Learn library, in the Cluster module (https://github.com/scikit-learn/scikit-learn/blob/main/sklearn/cluster/_dbscan.py).




def DBSCAN_outliers(data, one_dimensional = False, eps=0.5, min_samples=5, metric='euclidean', metric_params=None, algorithm='auto', leaf_size=30, p=None, n_jobs=None):
    #---imports---
    import pandas as pd
    import seaborn as sns
    import numpy as np
    from scipy import stats
    import statistics as st
    import matplotlib.pyplot as plt
    #------
    from sklearn.cluster import DBSCAN 
    if one_dimensional == True:
        name_value = [data.name]
        data = data[~np.isnan(data)]
        data = data.values.reshape(-1, 1)
        model = DBSCAN(eps=eps, min_samples=min_samples, metric=metric, metric_params=metric_params, algorithm=algorithm, leaf_size=leaf_size, p=p, n_jobs=n_jobs)
        model_clusters = model.fit_predict(data)
        #klastry
        #colors = model_clusters.labels_
        data = pd.DataFrame(data, columns = name_value)
        data['Anomaly']=model_clusters
        filter = (data['Anomaly'] == -1)
        correct_data = data.drop(axis = 0, index = data.loc[filter].index)
        outliers_data = data[filter]
        correct_data = correct_data.drop('Anomaly', axis=1)
        outliers_data = outliers_data.drop('Anomaly', axis=1)
        return correct_data, outliers_data
    else:
        if data.isna().sum().all() != 0:
            data = data.dropna(axis = 0)
        model = DBSCAN(eps=eps, min_samples=min_samples, metric=metric, metric_params=metric_params, algorithm=algorithm, leaf_size=leaf_size, p=p, n_jobs=n_jobs)
        model_clusters = model.fit_predict(data)
        data['Anomaly']=model_clusters
        filter = (data['Anomaly'] == -1)
        correct_data = data.drop(axis = 0, index = data.loc[filter].index)
        outliers_data = data[filter]
        correct_data = correct_data.drop('Anomaly', axis=1)
        outliers_data = outliers_data.drop('Anomaly', axis=1)
        return correct_data, outliers_data
