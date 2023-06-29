#all imports
import requests 
import pandas as pd
import sqlalchemy as db
from sqlalchemy import create_engine, text
from datetime import datetime



#create the engine
engine = create_engine("sqlite:///weather.db")

def start_engine():
    print('engine started') 
    with engine.connect() as connection:
        result = connection.execute(db.text("SELECT * FROM weathers ;")).fetchall()
        print(pd.DataFrame(result))


with engine.connect as connection:
    connection.execute('''CREATE TABLE current_weather (
    id INT PRIMARY KEY AUTO_INCREMENT,
    location VARCHAR(255) NOT NULL,
    temperature FLOAT,
    humidity FLOAT,
    wind_speed FLOAT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )''')

with engine.connect as connection:
    connection.execute('''CREATE TABLE past_weather (
    id INT PRIMARY KEY AUTO_INCREMENT,
    location VARCHAR(255) NOT NULL,
    observation_date DATE,
    temperature FLOAT,
    humidity FLOAT,
    wind_speed FLOAT
);''')

with engine.connect as connection:
    connection.execute('''CREATE TABLE future_weather (
    id INT PRIMARY KEY AUTO_INCREMENT,
    location VARCHAR(255) NOT NULL,
    forecast_date DATE,
    temperature_min FLOAT,
    temperature_max FLOAT,
    humidity FLOAT,
    wind_speed FLOAT
);''')





#this is done from the front end
# URL = 'http://api.weatherapi.com/v1/current.json?key=58fac11a92fa4083942221120232606&q=London&aqi=no'

# CITY = 'London'
# response = requests.get(URL)
# weather = response.json()



def insert_current_weather(location, temperature, humidity, wind_speed):
    """Insert current weather data into the 'current_weather' table"""
    query = text("INSERT INTO current_weather (location, temperature, humidity, wind_speed) "
                 "VALUES (:location, :temperature, :humidity, :wind_speed)")
    with engine.connect() as connection:
        connection.execute(query, location=location, temperature=temperature, humidity=humidity, wind_speed=wind_speed)

def insert_future_weather(location, forecast_date, temperature_min, temperature_max, humidity, wind_speed):
    """Insert future weather data into the 'future_weather' table"""
    query = text("INSERT INTO future_weather (location, forecast_date, temperature_min, temperature_max, humidity, wind_speed) "
                 "VALUES (:location, :forecast_date, :temperature_min, :temperature_max, :humidity, :wind_speed)")
    with engine.connect() as connection:
        connection.execute(query, location=location, forecast_date=forecast_date, temperature_min=temperature_min,
                           temperature_max=temperature_max, humidity=humidity, wind_speed=wind_speed)

def insert_past_weather(location, observation_date, temperature, humidity, wind_speed):
    """Insert past weather data into the 'past_weather' table"""
    query = text("INSERT INTO past_weather (location, observation_date, temperature, humidity, wind_speed) "
                 "VALUES (:location, :observation_date, :temperature, :humidity, :wind_speed)")
    with engine.connect() as connection:
        connection.execute(query, location=location, observation_date=observation_date, temperature=temperature,
                           humidity=humidity, wind_speed=wind_speed)

def delete_weather_record(table, record_id):
    """Delete a specific weather record from the specified table"""
    if table == "current_weather":
        table_name = "current_weather"
    elif table == "future_weather":
        table_name = "future_weather"
    elif table == "past_weather":
        table_name = "past_weather"
    else:
        print("Invalid table name.")
        return

    query = text(f"DELETE FROM {table_name} WHERE id = :record_id")
    with engine.connect() as connection:
        result = connection.execute(query, record_id=record_id)
        if result.rowcount > 0:
            print("Weather record deleted successfully!")
        else:
            print("Weather record not found.")

def read_weather_record(table, record_id):
    """Read a specific weather record from the specified table"""
    if table == "current_weather":
        table_name = "current_weather"
    elif table == "future_weather":
        table_name = "future_weather"
    elif table == "past_weather":
        table_name = "past_weather"
    else:
        print("Invalid table name.")
        return

    query = text(f"SELECT * FROM {table_name} WHERE id = :record_id")
    with engine.connect() as connection:
        result = connection.execute(query, record_id=record_id)
        weather_record = result.fetchone()
        if weather_record:
            print(weather_record)
        else:
            print("Weather record not found.")



# # Example usage: 
# insert_current_weather("New York", 25.5, 70.0, 10.2)
# insert_future_weather("Chicago", datetime.date(2023, 7, 1), 18.2, 28.5, 80.0, 12.0)
# insert_past_weather("Los Angeles", datetime.date(2023, 6, 27), 30.2, 65.0, 8.5)

# delete_weather_record("current_weather", 1)

# read_weather_record("future_weather", 1)

# display_all_records("past_weather")











