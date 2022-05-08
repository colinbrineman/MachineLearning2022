DROP TABLE Chicago_Airbnb_Listing_Dataset

-- Creating tables for Airbnb Chicago data
CREATE TABLE Chicago_Airbnb_Listing_Dataset (
     id INT,
     neighbourhood_cleansed VARCHAR(40) NOT NULL,
	 latitude FLOAT,
	 longitude FLOAT,
	 room_type VARCHAR (40) NOT NULL,
	 accommodates INT,
	 bathrooms_text VARCHAR (40),
	 bedrooms INT,
	 beds INT,
	 price MONEY,
	 minimum_nights INT,
	 maximum_nights INT,
	 minimum_minimum_nights INT,
	 maximum_minimum_nights INT,
	 minimum_maximum_nights INT,
	 maximum_maximum_nights INT,
	 minimum_nights_avg_ntm FLOAT,
	 maximum_nights_avg_ntm FLOAT,
	
	 	
     PRIMARY KEY (id),
     UNIQUE (id)
);

SELECT * FROM Chicago_Airbnb_Listing_Dataset
