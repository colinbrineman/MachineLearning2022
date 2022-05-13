# MachineLearning2022

#Ownership
* Rus - Machine Learning
* Al - Database management
* Colin - Github and Visualization
* Louisa - Visualization/Dashboarding
* Kristen - General Support/ ETL# Background
# Background
Airbnb provids travellers an easy and convenient place to stay during their travels. also is giving a great opportunity for many to earn extra revenue by listing their properties for residents to stay,in this Project we are analyzing Airbnb dataset of Chicago to draw interesting insights and address some questions.

Questions Addressed ?

1-Which are the popular neighborhoods, their average prices and no. of listings.

2-What are percent share of different property type and room type.

3-How the pricing is varying with location, property type, reviews.

# Why Airbnb ?

Airbnb is a leading website where people can book beds, rooms, apartments, homes etc. all around the world. It provides a platform for the people to rent out their places at their convenience without involving complex channels or doing major investments. Users can also find a place to stay at much competitive prices as compared to hotels. Through Airbnb, people can find place to stay even in the areas where the likelihood of having hotels is very less. Many a times, even people prefer to stay in local settings, with local people.

 Airbnb Statistics •7 million listings worldwide • 2.9 million hosts on Airbnb worldwide in 2022 • Worldwide value is $93.01 billion 

# Data Preparation

In this project, we will be using  open source Chicago Airbnb data https://www.kaggle.com/datasets/jinbonnie/chicago-airbnb-open-data?resource=download to help understand the trends of Airbnb in chicago area 
This dataset has 6398 observations and 16 features. we wanted to predict the price of a property per night using the type of property, the location , and the property’s review score.
price - quantitative variable for nightly rental price in U.S. dollars
Room_type - categorical variable with three levels: entire home/apt., shared room, and private room
neighborhood- location of the property
Review_score - rating of the property

# This Project Built With:
Python Pandas
PostgreSQL
HTML
CSS
Tableau 

# Database Management
For this project we set up the database our machine learning module would use. We utilized AWS to set up a Postgres DB hosted by AWS. The DB was then connected to pgAdmin in which the schema was set and data imported. Once fully connected the DB information was passed to into the jupyter notebook environment.

## Data Analysis

The data set was obtained from Inside Airbnb which does web scraping to gather data on rentals.
Key features were selected from the data set to be used in a machine learning model
- Neighborhood
- Room Type
- Accommodates
- Bedrooms
- Bathrooms
- Beds

The code below is the function used to clean the data and structure it to fit the machine learning model

![image](https://user-images.githubusercontent.com/92827264/168172563-ef4a3632-568f-46d8-a57b-2257edf8d561.png)

The following models were used to try and train the data
- Random Forest Classifier
- Neural Network

## Machine Learning

The first Machine Learning Model that was used for was a Random Forest Classifier Model. Since this model uses classification we had to use bins to classify each listing into a category. 

![image](https://user-images.githubusercontent.com/92827264/168172725-23cc93dd-1a53-4f6e-b9d8-d474e8fcd104.png)

The accuracy of this model was about 34%, which better than double from random.

![image](https://user-images.githubusercontent.com/92827264/168172754-9ee42190-3219-45ac-9522-ce2d536f38c9.png)

The next Machine Learning Model that was used was a Tensorflow Neural Network Model. This model had 86 features (which are the key features encoded) with 3 hidden layers. The accuracy of this model was about 37%

![image](https://user-images.githubusercontent.com/92827264/168172864-fb568e02-ec9f-47c4-b5c1-038d2cefb22d.png)
![image](https://user-images.githubusercontent.com/92827264/168172916-8d8073b2-b13f-4ea2-9438-20401c101992.png)

To improve on these models we would need more time to feature engineering. The dataset doesn’t give important information like quality of furnishings, appliances, or the place itself.


# Visualization Tool
 We used Tableau as the Data Visualization tool as it is a very powerful, secure and flexible end to end analytics platform where we can visualize our data quickly and easily by creating interactive dashboards and convey an overall story using storyboard. 
 
Target Audience The insights drawn could be helpful for both Hosts and Users. Hosts- People putting up their place for rental purpose. Users- People searching for accommodation.

Our storyboard has been categorized into Three categories-

Airbnb neighborhood analysis 
Property analysis
Pricing analysis

# The tableau visualization has been published and can be directly viewed using the following link: (Tableau server link):
https://public.tableau.com/app/profile/louisamam/viz/FinalProjectAirbnbchicago/ChicagoAirbnbneighbouhood?publish=yes


#Html link:
https://colinbrineman.github.io/MachineLearning2022/website/index.html
