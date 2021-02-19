# Data Outliers detection

These functions are the final result of my engineering thesis.  

Abstract:
In the 21st century, data-related issues have become crucial for entrepreneurs and scientists. One of the most important elements of the data analysis process is the detection of outliers. This diploma thesis presents four ways to identify outliers. For one-dimensional data, these are the box plot method and the Z-Score method, and for high dimensional data, the DBSCAN clustering algorithm and the isolation forest algorithm. The mentioned methods have been implemented as functions using the Python language. On the basis of the collected knowledge and with the use of the created programs, a research experiment was carried out to detect outliers. On the basis of the obtained results, the presented methods have been compared.

## Boxplot method (boxplot_outliers.py)
The box plot method classifies observations as outliers when the distance from quartiles 1 and 3 is greater than the specified times the interquartile range (used for one-dimensional sets).

## Z-Score method (zscore_outliers.py)
The Z-Score method is used for attributes whose distribution is close to the normal one. An observation is considered to be outliers when its distance from the distribution center is greater than a given multiple of the standard deviation (used for one-dimensional sets).

## DBSCAN clustering (DBSCAN_outliers.py)
The DBSCAN grouping method checks whether in the n-dimensional space at a given distance from a given point there is a given minimum number of observations which classifies this point as a central point. If there are fewer but at least one of these points, the examined point is classified as a border point. Otherwise, the point is the outlier (used for one-dimensional sets).

## Isolation forest (isolationforest_outliers.py)
An isolation forest consists of isolation trees. An isolation tree is a certain graph data structure that is created by recursively splitting a data set in a node (vertex of the graph) based on a randomly selected attribute and a randomly selected value of that attribute. Tree growth ends when there are no grounds for further splitting the data set. Based on the number of splits, or the length of the path from the root to the last node, cases are classified as outliers or non-outliers. The shorter the path, the greater the probability of an outlier.
