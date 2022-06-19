import requests as req
import random as rand
from os import system
# from utils import formatText, countryInfo, menu, reloadMenu

url = "https://restcountries.com/v3.1"

# data = req.get(url+"/all").json()
# res = req.get(f"{url}/name/{user}").json()


def menu():
    print("1. Search for country information")
    print("2. Download the flag of a country")
    print("3. Countries game")
    print("0. Exit the program")

def subMenuFindCountry():
    pass


def reloadMenu():
    print("")
    input("¡Pulse intro para volver al menu!")
    system("cls")        
    menu()

def formatText(country):
    for k,v in country.items():
        print(f"{k.capitalize()}: {v}")

def countryInfo(user):
    keys = ("capital", "population", "area", "languages")
    result = {k:None for k in keys}
    data = req.get(f"{url}/name/{user}").json()
    if len(data) >= 1:
        country = data[0]
        result["capital"] = country["capital"][0]
        result["population"] = country["population"]
        result["area"] = country["area"]
        result["languages"] = tuple(country["languages"].values())
        
    return result

def downloadFlag(countryName):
    country = req.get(f"{url}/name/{countryName}").json()
    flag = list(country[0]["flags"].values())[0]
    img = req.get(flag).content
    file = open(f"C:/Users/Guillermo/Documents/CursoPython/Countries/flags/{country[0]['name']['common']}.png", "wb")
    file.write(img)
    file.close()

def game(userRegion):
    region = req.get(f"{url}/region/{userRegion}").json()
    regionCountries = []
    for i in region:
        regionCountries.append(i["name"]["common"])
    regionCountries2 = regionCountries[rand.randrange(0, len(regionCountries))]
    capitalQuestion= {
        "Question": f"¿Cual es la capital de {regionCountries2}?",
        "key": "capital",
        "Answer": "COGEMOS EL PAIS Y SACAMOS SU CAPITAL PARA EVALUAR CON LA RESPUESTA DEL USUARIO {capital}",
        "UserAnswer": None
    },
    {
        "Question": f"¿Cual es la población de {regionCountries2}?",
        "Key": "population",
        "Answer": "COGEMOS EL PAIS Y SACAMOS SU POBLACION PARA EVALUAR CON LA RESPUESTA DEL USUARIO {population}",
        "UserAnswer": None
    }
    questions = [capitalQuestion["Question"], populationQuestion["Question"]]
    
    return regionCountries2 ,questions[rand.randrange(0,len(capitalQuestion))]



userInput = ""
while userInput != "0":
    if userInput == "":
       menu()
    elif userInput == "1":
        formatText(countryInfo(input("Writte the country you want search: ")))
        reloadMenu()
    elif userInput == "2":
        downloadFlag(input("Write the name of the country you want to download its flag: "))
        reloadMenu()
    elif userInput == "3":
        print("Choose one region from this list: ")
        print("- Africa")
        print("- Americas")
        print("- Asia")
        print("- Europe")
        print("- Oceania")
        print(game(input("¿What region are you looking for? ")))
        reloadMenu()
    else:
        print(f"¡ERROR! The option {userInput} is not available.¡Choose a correct option!")
        print("")
        menu()
    userInput = input("Choose one: ")
    system("cls")


