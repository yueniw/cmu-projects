Data Preprocessing is done using Python in Jupyter Notebook for speed and efficiency in processing
- data_preprocessing_1.ipynb: First step of the data transformation stage using raw data.
- data_preprocessing_2.ipynb: Second step of the data transformation stage. 

The rest of the files are in R

- clustering.Rmd: uses hierarchical clustering using longitude and latitude of all stations, final selection of top 20 highest variance of availability stations, and all google map visualizations for clustering
- reshuffling_strategy.Rmd: generates plots for reshuffling patterns and availability trends. Also fits a logistic regression model to compare relationship between availability proportion and the odds of reshuffling (Yes vs No).
- model.Rmd: generates more columns, samples data and fits both Random Forest model and Logistic Regression model to the data and compare their confusion matrix of the Actual and the Predicted



