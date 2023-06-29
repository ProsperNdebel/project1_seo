--this file is for creating the data in my database when I run the command 
--mysql -u <username> -p <database_name> < schema.sql it inputs the tables defined below to this database



-- Schema for current weather
'CREATE TABLE current_weather (
    id INT PRIMARY KEY AUTO_INCREMENT,
    location VARCHAR(255) NOT NULL,
    temperature FLOAT,
    humidity FLOAT,
    wind_speed FLOAT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);'

-- Schema for future weather
CREATE TABLE future_weather (
    id INT PRIMARY KEY AUTO_INCREMENT,
    location VARCHAR(255) NOT NULL,
    forecast_date DATE,
    temperature_min FLOAT,
    temperature_max FLOAT,
    humidity FLOAT,
    wind_speed FLOAT
);

-- Schema for past weather
CREATE TABLE past_weather (
    id INT PRIMARY KEY AUTO_INCREMENT,
    location VARCHAR(255) NOT NULL,
    observation_date DATE,
    temperature FLOAT,
    humidity FLOAT,
    wind_speed FLOAT
);


-- --table that represents what fields a weather has
-- CREATE TABLE Weather (
--   id INT PRIMARY KEY,
--   city_id INT NOT NULL,
--   weather_date DATE NOT NULL,
--   temperature FLOAT,
--   humidity FLOAT,
--   pressure FLOAT,
--   wind_speed FLOAT,
--   description VARCHAR(255),
--   weather_type VARCHAR(255),
--   is_current_weather BOOLEAN,
--   is_forecast BOOLEAN,
--   is_historical BOOLEAN,
--   created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
--   FOREIGN KEY (city_id) REFERENCES City(id)
-- );


-- -- table that has cities
-- CREATE TABLE City (
--   id INT PRIMARY KEY,
--   name VARCHAR(255) NOT NULL,
--   country VARCHAR(255) NOT NULL
-- );


