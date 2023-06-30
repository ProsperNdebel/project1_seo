import requests

def menu():
    print("|              MENU               |")
    print("|[1] Current Weather              |")
    print("|[2] Past Weather                 |")
    print("|[3] Weather Forecast             |")
    print("|[4] View Saved Data              |")
    print("|[5] Delete Data from Saved Data  |")
    print("|[0] Exit the program             |")
    print("|_________________________________|/n")

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

def printPast(data):
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
    print("Min Temperature: ", min_temp, "°C\n")

    a = input("Do you want to save the data?[Y/N]? ")
    if a.upper() == "Y":
        saveData(location, date, condition, max_temp, min_temp)

def printFuture(data):
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
    print("Min Temperature: ", min_temp, "°C\n")

    a = input("Do you want to save the data?[Y/N]? ")
    if a.upper() == "Y":
        saveData(location, date, condition, max_temp, min_temp)

def printData():
    engine.execute("SELECT * FROM weather")
    rows = engine.fetchall()
    if len(rows) == 0:
        print("There is no saved data currently.")
    else:
        for row in rows:
            print("ID:", row[0])
            print("City:", row[1])
            print("Date:", row[2])
            print("Condition:", row[3])
            print("Max Temperature:", row[4], "°C")
            print("Min Temperature:", row[5], "°C")
            print()

def saveData(city, date, condition, max_temp, min_temp):
    engine.execute("INSERT INTO weather (city, date, condition, max_temp, min_temp) VALUES (?, ?, ?, ?, ?)", (city, date, condition, max_temp, min_temp))
    file.commit()
    print("Weather Data Saved.")

def deleteData(id):
    engine.execute("SELECT * FROM weather WHERE id=?", (id,))
    x = engine.fetchone()
    if (x):
        engine.execute("DELETE FROM weather WHERE id=?", (id,));
        print("The record was successfully deleted.\n")
    else:
        print("Record doesn't exist.\n")

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
        printPast(past)
    elif choice == 3:
        futCity = input("Enter full city name: ")
        futDate = input("Enter a future date: ")
        print("\n")
        url = url = "http://api.weatherapi.com/v1/future.json?key=58fac11a92fa4083942221120232606&q=" + futCity + "&dt=" + futDate
        future = requests.post(url)
        future = future.json()
        print("Weather on " + futDate +" in "+ futCity)
        printFuture(future)
    elif choice == 4:
        print("Stored Weather Data:\n")
        printData()
    elif choice == 5:
        rem=input("Enter the id-value for record to delete: ")
        deleteData(rem)
    else:
        print("Invalid Option\n")


    menu()
    choice = int(input("Enter your choice: "))

print("Thanks for using the program.")
