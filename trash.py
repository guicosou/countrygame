import random as ran
import requests as req
url = "https://restcountries.com/v3.1"

data = req.get(url+"/all").json()

a = list(filter(lambda countri: countri["name"]["common"], data))


pregunta1 = "¿Que hora es?"
pregunta2 = "¿Que dia es?"
pregunta3 = "¿Que mes es?"
pregunta4 = "¿Que año es?"
pregunta5 = "¿Que siglo es?"

lista = [pregunta1, pregunta2, pregunta3, pregunta4, pregunta5]

print(a)
print(lista[ran.randrange(1,5)])