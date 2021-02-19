# The isolationforest_outliers function returns two data sets (DataFrame):
# - correct_data - data set that does not contain any outliers,
# - outliers_data - a data set containing outliers removed from the original set.
# DBSCAN algorithm has been implemented in the DBSCAN function in the Scikit-Learn library, in the Cluster module;
# The DBSCAN feature was developed by the team of dr. Alberta Villanova del Moral (https://github.com/scikit-learn/scikit-learn/blob/main/sklearn/cluster/_dbscan.py).




def isolationforest_outliers(data, one_dimensional = False, n_estimators=100, max_samples='auto', contamination='auto', max_features=1.0, bootstrap=False, n_jobs=None, random_state=None, verbose=0, warm_start=False, behaviour='new' ):
    #---imports---
    import pandas as pd
    import seaborn as sns
    import numpy as np
    from scipy import stats
    import statistics as st
    import matplotlib.pyplot as plt
    #------
    from sklearn.ensemble import IsolationForest
    if one_dimensional == True:
        name_value = [data.name]
        data = data[~np.isnan(data)]
        data = data.values.reshape(-1, 1)
        #contamination=float(0.2)
        forest_model=IsolationForest(n_estimators=n_estimators, max_samples=max_samples, contamination=contamination, max_features=max_features, bootstrap=bootstrap, n_jobs=n_jobs, random_state=random_state, verbose=verbose,warm_start=warm_start, behaviour=behaviour)
        forest_model.fit(data)
        data = pd.DataFrame(data, columns = name_value)
        data_info = data.copy()
        data_info['Scores_value']=forest_model.decision_function(data)
        data_info['Anomaly']=forest_model.predict(data)
        filter = (data_info['Anomaly'] == -1)
        correct_data = data_info.drop(axis = 0, index = data.loc[filter].index)
        outliers_data = data_info[filter]
        correct_data = correct_data.drop(['Anomaly', 'Scores_value'], axis=1)
        outliers_data = outliers_data.drop(['Anomaly', 'Scores_value'], axis=1)
        return correct_data, outliers_data
    else:
        if data.isna().sum().all() != 0:
            data = data.dropna(axis = 0)
        #contamination=float(0.2)
        forest_model=IsolationForest(n_estimators=n_estimators, max_samples=max_samples, contamination=contamination, max_features=max_features, bootstrap=bootstrap, n_jobs=n_jobs, random_state=random_state, verbose=verbose, warm_start=warm_start, behaviour=behaviour)
        forest_model.fit(data)
        data_info = data.copy()
        data_info['Scores_value']=forest_model.decision_function(data)
        data_info['Anomaly']=forest_model.predict(data)
        filter = (data_info['Anomaly'] == -1)
        correct_data = data_info.drop(axis = 0, index = data.loc[filter].index)
        outliers_data = data_info[filter]
        correct_data = correct_data.drop(['Anomaly', 'Scores_value'], axis=1)
        outliers_data = outliers_data.drop(['Anomaly', 'Scores_value'], axis=1)
        return  correct_data, outliers_data
