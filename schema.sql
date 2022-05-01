-- Creating tables for Airbnb Chicago data
CREATE TABLE airbnb_data_chicago (
     id INT,
     neighbourhood_cleansed VARCHAR(40) NOT NULL,
	 latitude INT,
	 longitude INT,
	 room_type VARCHAR (40) NOT NULL,
	 accommodates INT,
	 bathrooms_text INT,
	 bedrooms INT,
	 beds INT,
	 price INT,
	 minimum_nights INT,
	 maximum_nights INT,
	 minimum_minimum_nights INT,
	 maximum_minimum_nights INT,
	 minimum_maximum_nights INT,
	 maximum_maximum_nights INT,
	 minimum_nights_avg_ntm INT,
	 maximum_nights_avg_ntm INT,
	 coordinates NVARCHAR (50),
	 geopy_address VARCHAR (40),
	 zip_code INT,
	 median_household_income INT,
	 	
     PRIMARY KEY (id),
     UNIQUE (id)
);

SELECT * FROM airbnb_data_chicago
