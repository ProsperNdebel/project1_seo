import requests
import database


#instantiate the database from here
ENG = database.engine
database.start_engine()

def menu():
    print("[1] Current Weather")
    print("[2] Past Weather")
    print("[3] Weather Forecast")
    print("[0] Exit the program\n")

def print_current_weather(data):
    location = data['location']['name']
    region = data['location']['region']
    country = data['location']['country']
    condition = data['current']['condition']['text']
    temperature = data['current']['temp_c']
    wind_speed = data['current']['wind_kph']
    humidity = data['current']['humidity']
    
    print("Location: ", location, ", ", region, ", ", country)
    print("Condition: ", condition)
    print("Temperature: ", temperature, "°C")
    print("Wind Speed: ", wind_speed, "kph")
    print("Humidity: ", humidity, "%")

def print_past_weather(data):
    location = data['location']['name']
    region = data['location']['region']
    country = data['location']['country']
    date = data['forecast']['forecastday'][0]['date']
    condition = data['forecast']['forecastday'][0]['day']['condition']['text']
    max_temp = data['forecast']['forecastday'][0]['day']['maxtemp_c']
    min_temp = data['forecast']['forecastday'][0]['day']['mintemp_c']
    
    print("Location: ", location, ", ", region, ", ", country)
    print("Date: ", date)
    print("Condition: ", condition)
    print("Max Temperature: ", max_temp, "°C")
    print("Min Temperature: ", min_temp, "°C")

def print_future_weather(data):
    location = data['location']['name']
    region = data['location']['region']
    country = data['location']['country']
    date = data['forecast']['forecastday'][0]['date']
    condition = data['forecast']['forecastday'][0]['day']['condition']['text']
    max_temp = data['forecast']['forecastday'][0]['day']['maxtemp_c']
    min_temp = data['forecast']['forecastday'][0]['day']['mintemp_c']
    
    print("Location: ", location, ", ", region, ", ", country)
    print("Date: ", date)
    print("Condition: ", condition)
    print("Max Temperature: ", max_temp, "°C")
    print("Min Temperature: ", min_temp, "°C")

menu()
choice = int(input("Enter your choice: "))
print("\n")

while choice != 0:
    if choice == 1:
        currCity = input("Enter full city name: ")
        print("\n")
        url = "http://api.weatherapi.com/v1/current.json?key=58fac11a92fa4083942221120232606&q=" + currCity
        current = requests.get(url)
        current = current.json()
        print("Current Weather in " + currCity)
        print_current_weather(current)
    elif choice == 2:
        pastCity = input("Enter full city name: ")
        pastDate = input("Enter a date within the last 7 days[YYYY-MM-DD]: ")
        print("\n")
        url = "http://api.weatherapi.com/v1/history.json?key=58fac11a92fa4083942221120232606&q=" + pastCity + "&dt=" + pastDate
        past = requests.get(url)
        past = past.json()
        print("Weather on " + pastDate +" in "+ pastCity)
        print_past_weather(past)
    elif choice == 3:
        futCity = input("Enter full city name: ")
        futDate = input("Enter a future date: ")
        print("\n")
        url = url = "http://api.weatherapi.com/v1/future.json?key=58fac11a92fa4083942221120232606&q=" + futCity + "&dt=" + futDate
        future = requests.post(url)
        future = future.json()
        print("Weather on " + futDate +" in "+ futCity)
        print_future_weather(future)
    else:
        print("Invalid Option")
    print()
    menu()
    choice = int(input("Enter your choice: "))

print("Thanks for using the program.")