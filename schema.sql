-- Creating tables for Airbnb Chicago data
CREATE TABLE airbnb_data_chicago (
     id INT,
     name VARCHAR(40) NOT NULL,
	 host_id INT,
	 host_name VARCHAR(40) NOT NULL,
	 neighbourhood_group VARCHAR(40) NOT NULL,
	 neighbourhood VARCHAR (40) NOT NULL,
	 latitude INT,
	 longitude INT,
	 room_type VARCHAR (40) NOT NULL,
	 price INT,
	 minimum_nights INT,
	 number_of_reviews INT,
	 last_review date,
	 reviews_per_month INT,
	 calculated_host_listings_count INT,
	 availability_365 INT,
	
     PRIMARY KEY (id),
     UNIQUE (id)
);

SELECT * FROM airbnb_data_chicago
