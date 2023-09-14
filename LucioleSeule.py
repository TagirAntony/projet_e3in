SEUIL = 1.0
import random as random

#Q1 
def main():
    lucioleEnergie = random.uniform(0, 100)
    print("Energie de la luciole : ", lucioleEnergie)   
#print(main())


#Q2
def symboliseLuciole(niveauEnergie):
    if niveauEnergie >= SEUIL: 
        return "*"
    else:
        return "."
#print(symboliseLuciole(1.0))


#Q3
def afficheLuciole(niveauEnergie, verbeux):
    print(symboliseLuciole(niveauEnergie), end = "")
    if verbeux == True:
        print(" ", niveauEnergie)
    print()
#print(afficheLuciole(1.0, True))


#Q4
# Modifier manuellement et plusieurs fois le niveau d’énergie de la luciole, et afficher la luciole après chaque modification.
#print(main(10))


#Q5
def main():
    lucioleEnergie = random.uniform(0, 100)
    print("Energie de la luciole : ", lucioleEnergie)
    lucioleDeltaEnergie = random.uniform(0, 1)
    print("Delta Energie de la luciole : ", lucioleDeltaEnergie)
#print(main())


#Q6
def incrementeLuciole(niveauEnergie, deltaEnergie):
    return niveauEnergie + deltaEnergie 
#print(incrementeLuciole(1.0, 1.0))


#Q7
def main():
    lucioleEnergie = random.uniform(0, 100)
    print("Energie de la luciole : ", lucioleEnergie)
    lucioleDeltaEnergie = random.uniform(0, 1)
    print("Delta Energie de la luciole : ", lucioleDeltaEnergie)
    for i in range(5):
        lucioleEnergie = incrementeLuciole(lucioleEnergie, lucioleDeltaEnergie)
        print("Energie de la luciole : ", lucioleEnergie)
#print(main())


#Q8 
def simuleLucioleNbPas(nbPas):
    lucioleEnergie = random.uniform(0, 100)
    print("Energie de la luciole : ", lucioleEnergie)
    lucioleDeltaEnergie = random.uniform(0, 1)
    print("Delta Energie de la luciole : ", lucioleDeltaEnergie)
    for i in range(nbPas):
        lucioleEnergie = incrementeLuciole(lucioleEnergie, lucioleDeltaEnergie)
        afficheLuciole(lucioleEnergie, True)
#print(simuleLucioleNbPas(5))


#Q9
def simuleLucioleNbFlashs(nbFlashs):
    lucioleEnergie = random.uniform(0, 100)
    print("Energie de la luciole : ", lucioleEnergie)
    lucioleDeltaEnergie = random.uniform(0, 1)
    print("Delta Energie de la luciole : ", lucioleDeltaEnergie)
    for i in range(nbFlashs):
        lucioleEnergie = incrementeLuciole(lucioleEnergie, lucioleDeltaEnergie)
        afficheLuciole(lucioleEnergie, True)
        if lucioleEnergie >= SEUIL:
            print("Flash !")
#print(simuleLucioleNbFlashs(3))