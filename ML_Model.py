import pandas as pd
import re
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt

original_df = pd.read_csv('Chicago_Airbnb_Listing_Dataset.csv')
airbnb_df = original_df

airbnb_df['price'] = airbnb_df['price'].str.replace('$', '')
airbnb_df['price'] = airbnb_df['price'].str.replace(',', '').astype(float)
airbnb_df.drop(airbnb_df[airbnb_df.price > 1000].index, inplace=True)
neighbourhoods = airbnb_df['neighbourhood_cleansed'].value_counts()

neighborhood_dict = dict(zip(neighbourhoods.index,np.arange(len(neighbourhoods.index))))

cleaning_df = airbnb_df
cleaning_df['neighbourhood_cleansed'] = cleaning_df['neighbourhood_cleansed'].apply(lambda x:neighborhood_dict[x])

cleaning_df['bathrooms_text'] = cleaning_df['bathrooms_text'].str.replace('-bath', '0.5')
cleaning_df['bathrooms_text'] = cleaning_df['bathrooms_text'].str.extract('(\d*\.\d+|\d+)', expand=False)
cleaning_df['bathrooms_text'] = cleaning_df['bathrooms_text'].astype(float)
cleaning_df = cleaning_df.dropna()

working_df = pd.get_dummies(cleaning_df)

#Start Machine Learning 
X = working_df.drop(['price','id','latitude','longitude','minimum_minimum_nights','maximum_minimum_nights','minimum_maximum_nights','maximum_maximum_nights','minimum_nights_avg_ntm','maximum_nights_avg_ntm'], axis=1)
y = working_df['price']