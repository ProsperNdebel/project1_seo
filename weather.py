import requests
import json
import pprint

def menu():
    print("[1] Current Weather")
    print("[2] Past Weather")
    print("[3] Weather Forecast")
    print("[0] Exit the program\n")

menu()
choice = int(input("Enter your choice: "))

while choice != 0:
    if choice == 1:
        currCity = input("Enter full city name: ")
        url = "http://api.weatherapi.com/v1/current.json?key=58fac11a92fa4083942221120232606&q=" + currCity
        current = requests.post(url)
        current = current.json()
        pprint.pprint(current)
    elif choice == 2:
        pastCity = input("Enter full city name: ")
        pastDate = input("Enter a date within the last 7 days: ")
        url = "http://api.weatherapi.com/v1/history.json?key=58fac11a92fa4083942221120232606&q=" + pastCity + "&dt=" + pastDate
        past = requests.post(url)
        past = past.json()
        pprint.pprint(past)
    elif choice == 3:
        futCity = input("Enter full city name: ")
        futDate = input("Enter a future date: ")
        url = "http://api.weatherapi.com/v1/future.json?key=58fac11a92fa4083942221120232606&q=" + futCity + "&dt=" + futDate
        future = requests.post(url)
        future = future.json()
        pprint.pprint(future)
    else:
        print("Invalid Option")
    print()
    menu()
    choice = int(input("Enter your choice: "))

print("Thanks for using the program.")


