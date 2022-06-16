import requests as req
from os import system

url = "https://restcountries.com/v3.1"

def menu():
    print("1. Search for country information")
    print("2. Download the flag of a country")
    print("3. Countries game")
    print("0. Exit the program")

def reloadMenu():
    print("")
    input("¡Pulse intro para volver al menu!")
    system("cls")        
    menu()

def formatText(country):
    for k,v in country.items():
        print(f"{k.capitalize()}: {v}")

def countryInfo():
    user = input("Writte the country you want search: ")
    data = req.get(f"{url}/name/{user}").json()
    # if len(data) >= 1:
    country = data[0]
    capital = country["capital"][0]
    population = country["population"]
    area = country["area"]
    language = country["languages"].values()