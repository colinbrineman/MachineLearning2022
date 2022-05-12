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

room_type_list = airbnb_df['room_type'].value_counts().index
accommodates_list = airbnb_df['accommodates'].value_counts().index
bathroom_list = airbnb_df['bathrooms_text'].value_counts().index
bedroom_list = airbnb_df['bedrooms'].value_counts().index
beds_list = airbnb_df['beds'].value_counts().index

def clean_listings(df):
    
    # Convert price type from string to float and remove $ sign and commas
    df['price'] = df['price'].str.replace('$', '')
    df['price'] = df['price'].str.replace(',', '').astype(float)
    df.drop(df[df.price > 1000].index, inplace=True)

    #Convert neighborhood name to a numerical number
    neighbourhoods = airbnb_df['neighbourhood_cleansed'].value_counts()
    neighborhood_dict = dict(zip(neighbourhoods.index,np.arange(len(neighbourhoods.index))))
    df['neighbourhood_cleansed'] = df['neighbourhood_cleansed'].apply(lambda x:neighborhood_dict[x])

    #Make bins for price ranges
    price_bins = [0.0, 49.0, 74.0, 99.0, 124.0, 149.0, 199.0, 299.0, 100000.0]
    price_labels = ['0-49','50-74','75-99','100-124','125-149','150-199', '200-299', '300+']

    #Convert Bathrooms from String to Float
    df['bathrooms_text'] = df['bathrooms_text'].str.replace('-bath', '0.5')
    df['bathrooms_text'] = df['bathrooms_text'].str.extract('(\d*\.\d+|\d+)', expand=False)
    df['bathrooms_text'] = df['bathrooms_text'].astype(float)    
    df["price_range"] = pd.cut(df["price"], price_bins, labels=price_labels)
    df.dropna()


     
    # Drop row that are not needed
    df.drop(['id','latitude','longitude','minimum_minimum_nights','maximum_minimum_nights',
            'minimum_maximum_nights','maximum_maximum_nights','minimum_nights_avg_ntm',
            'maximum_nights_avg_ntm', 'minimum_nights', 'maximum_nights'], axis=1, inplace=True)
    return df

working_df = clean_listings(original_df.copy())

working_df = pd.get_dummies(working_df)

#Start Machine Learning 
X = working_df.drop('price', axis=1)
y = working_df['price']

# Split Data to test and train
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

#Scale data
scaler = MinMaxScaler().fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)