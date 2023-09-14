SEUIL = 1.0
import random as random

#Q10
def creerLuciole():
    lucioleEnergie = random.uniform(0, 100)
    lucioleDeltaEnergie = random.uniform(0, 1)
    return [lucioleEnergie, lucioleDeltaEnergie]
#print(creerLuciole())

#Q11
def incrementeLuciole(luciole):
    luciole[0] = luciole[0] + luciole[1]
    return luciole
#print(incrementeLuciole([1.0, 1.0]))

#Q12
def creerPopulation(nbLucioles):
    population = []
    for i in range(nbLucioles):
        population.append(creerLuciole())
    return population
#print(creerPopulation(5))

#Q13
def main():
    population = creerPopulation(5)
    print(population)
#print(main())

#Q14
def prairieVide(nbLignes, nbColonnes):
    prairie = []
    for i in range(nbLignes):
        prairie.append([])
        for j in range(nbColonnes):
            prairie[i].append(None)
    return prairie
#print(prairieVide(5, 5))

#Q15
# Fonction affichePrairie qui prend en paramètres une prairie et une population de lucioles, et qui en réalise l’affichage en mode texte dans la console :
# - Une case inoccupée de la prairie est représentée par un espace.
# - Une case occupée par une luciole qui n’émet pas de flash par un point.
# - Une case occupée par une luciole qui émet un flash est représenté par une étoile.
# - Les bordures de la prairie sont représentées par des #.
def affichePrairie(prairie, population):
    for i in range(len(prairie)):
        print("#", end="")
        for j in range(len(prairie[i])):
            if prairie[i][j] == None:
                print(" ", end="")
            elif population[prairie[i][j]][0] >= SEUIL:
                print("*", end="")
            else:
                print(".", end="")
        print("#")
#print(affichePrairie(prairieVide(5, 5), creerPopulation(5)))

#16 
def main():
    population = creerPopulation(5)
    prairie = prairieVide(5, 5)
    affichePrairie(prairie, population)
#print(main())

#Q17
def prairieLucioles(nbLignes, nbColonnes, population):
    prairie = prairieVide(nbLignes, nbColonnes)
    for i in range(len(population)):
        ligne = random.randint(0, nbLignes-1)
        colonne = random.randint(0, nbColonnes-1)
        while prairie[ligne][colonne] != None:
            ligne = random.randint(0, nbLignes-1)
            colonne = random.randint(0, nbColonnes-1)
        prairie[ligne][colonne] = i
    return prairie
#print(prairieLucioles(5, 5, creerPopulation(5)))

#Q18
def main():
    population = creerPopulation(5)
    prairie = prairieLucioles(5, 5, population)
    affichePrairie(prairie, population)
#print(main())

#Q19
def simulationPrairie(nbPas, nbLignes, nbColonnes, population):
    prairie = prairieLucioles(nbLignes, nbColonnes, population)
    for i in range(nbPas):
        for j in range(len(population)):
            incrementeLuciole(population[j])
        affichePrairie(prairie, population)
#print(simulationPrairie(5, 5, 5, creerPopulation(5)))

#Q20
def main():
    population = creerPopulation(5)
    simulationPrairie(5, 5, 5, population)
#print(main())

#Q21
# Classe Luciole.py possédant comme attributs une énergie et un delta.
# Cette classe possède aussi SEUIL comme attribut de la classe.
class Luciole:
    SEUIL = 10
    def __init__(self, energie, delta):
        self.energie = energie
        self.delta = delta
    def __str__(self):
        return "Luciole(" + str(self.energie) + ", " + str(self.delta) + ")"


#Q22
class Luciole:
    SEUIL = 10
    def __init__(self, energie, delta):
        self.energie = energie
        self.delta = delta
    def __str__(self):
        return "Luciole(" + str(self.energie) + ", " + str(self.delta) + ")"
    def getEnergie(self):
        return self.energie
    def getDelta(self):
        return self.delta
    def setEnergie(self, energie):
        self.energie = energie
    def setDelta(self, delta):
        self.delta = delta

#Q23
class Luciole:
    SEUIL = 10
    def __init__(self, energie, delta):
        self.energie = energie
        self.delta = delta
    def __str__(self):
        return "Luciole(" + str(self.energie) + ", " + str(self.delta) + ")"
    def getEnergie(self):
        return self.energie
    def getDelta(self):
        return self.delta
    def setEnergie(self, energie):
        self.energie = energie
    def setDelta(self, delta):
        self.delta = delta
    def symboliseLuciole(self):
        if self.energie >= self.SEUIL:
            return "*"
        else:
            return "."
    def afficheLuciole(self):
        print(self.symboliseLuciole())
    def incrementeLuciole(self):
        self.energie += self.delta
        if self.energie < 0:
            self.energie = 0
        elif self.energie > 20:
            self.energie = 20

#Q24
class Luciole:
    SEUIL = 10
    def __init__(self, energie, delta):
        self.energie = energie
        self.delta = delta
    def __str__(self):
        return "Luciole(" + str(self.energie) + ", " + str(self.delta) + ")"
    def getEnergie(self):
        return self.energie
    def getDelta(self):
        return self.delta
    def setEnergie(self, energie):
        self.energie = energie
    def setDelta(self, delta):
        self.delta = delta
    def symboliseLuciole(self):
        if self.energie >= self.SEUIL:
            return "*"
        else:
            return "."
    def afficheLuciole(self):
        print(self.symboliseLuciole())
    def incrementeLuciole(self):
        self.energie += self.delta
        if self.energie < 0:
            self.energie = 0
        elif self.energie > 20:
            self.energie = 20
    @staticmethod
    def creerLuciole():
        energie = random.randint(0, 20)
        delta = random.randint(-5, 5)
        return Luciole(energie, delta)

#Q25
class Luciole:
    SEUIL = 10
    def __init__(self, energie, delta):
        self.energie = energie
        self.delta = delta
    def __str__(self):
        return "Luciole(" + str(self.energie) + ", " + str(self.delta) + ")"
    def getEnergie(self):
        return self.energie
    def getDelta(self):
        return self.delta
    def setEnergie(self, energie):
        self.energie = energie
    def setDelta(self, delta):
        self.delta = delta
    def symboliseLuciole(self):
        if self.energie >= self.SEUIL:
            return "*"
        else:
            return "."
    def afficheLuciole(self):
        print(self.symboliseLuciole())
    def incrementeLuciole(self):
        self.energie += self.delta
        if self.energie < 0:
            self.energie = 0
        elif self.energie > 20:
            self.energie = 20
    @staticmethod
    def creerLuciole():
        energie = random.randint(0, 20)
        delta = random.randint(-5, 5)
        return Luciole(energie, delta)
    def simuleLucioleNbPas(self, nbPas):
        for i in range(nbPas):
            self.incrementeLuciole()
            self.afficheLuciole()

#Q26
class Population:
    def __init__(self, listeLucioles):
        self.listeLucioles = listeLucioles

#Q27
class Population:
    def __init__(self, listeLucioles):
        self.listeLucioles = listeLucioles
    def __str__(self):
        return "Population(" + str(self.listeLucioles) + ")"
    def getListeLucioles(self):
        return self.listeLucioles
    def setListeLucioles(self, listeLucioles):
        self.listeLucioles = listeLucioles

#Q28
class Prairie:
    def __init__(self, listeListe, population):
        self.listeListe = listeListe
        self.population = population

#Q29
class Prairie:
    def __init__(self, listeListe, population):
        self.listeListe = listeListe
        self.population = population
    def __str__(self):
        return "Prairie(" + str(self.listeListe) + ", " + str(self.population) + ")"
    def getListeListe(self):
        return self.listeListe
    def getPopulation(self):
        return self.population
    def setListeListe(self, listeListe):
        self.listeListe = listeListe
    def setPopulation(self, population):
        self.population = population
    @staticmethod
    def creerPrairieVide(nbLignes, nbColonnes):
        listeListe = []
        for i in range(nbLignes):
            listeListe.append([])
            for j in range(nbColonnes):
                listeListe[i].append(".")
        return Prairie(listeListe, Population([]))

#Q30
class Prairie:
    def __init__(self, listeListe, population):
        self.listeListe = listeListe
        self.population = population
    def __str__(self):
        return "Prairie(" + str(self.listeListe) + ", " + str(self.population) + ")"
    def getListeListe(self):
        return self.listeListe
    def getPopulation(self):
        return self.population
    def setListeListe(self, listeListe):
        self.listeListe = listeListe
    def setPopulation(self, population):
        self.population = population
    @staticmethod
    def creerPrairieVide(nbLignes, nbColonnes):
        listeListe = []
        for i in range(nbLignes):
            listeListe.append([])
            for j in range(nbColonnes):
                listeListe[i].append(".")
        return Prairie(listeListe, Population([]))
    def affichePrairie(self):
        for i in range(len(self.listeListe)):
            for j in range(len(self.listeListe[i])):
                print(self.listeListe[i][j], end="")
            print()

#Q31
class Prairie:
    def __init__(self, listeListe, population):
        self.listeListe = listeListe
        self.population = population
    def __str__(self):
        return "Prairie(" + str(self.listeListe) + ", " + str(self.population) + ")"
    def getListeListe(self):
        return self.listeListe
    def getPopulation(self):
        return self.population
    def setListeListe(self, listeListe):
        self.listeListe = listeListe
    def setPopulation(self, population):
        self.population = population
    @staticmethod
    def creerPrairieVide(nbLignes, nbColonnes):
        listeListe = []
        for i in range(nbLignes):
            listeListe.append([])
            for j in range(nbColonnes):
                listeListe[i].append(".")
        return Prairie(listeListe, Population([]))
    def affichePrairie(self):
        for i in range(len(self.listeListe)):
            for j in range(len(self.listeListe[i])):
                print(self.listeListe[i][j], end="")
            print()
    @staticmethod
    def prairieLucioles(nbLignes, nbColonnes, population):
        prairie = Prairie.creerPrairieVide(nbLignes, nbColonnes)
        for i in range(len(population.getListeLucioles())):
            ligne = random.randint(0, nbLignes - 1)
            colonne = random.randint(0, nbColonnes - 1)
            while prairie.getListeListe()[ligne][colonne] != ".":
                ligne = random.randint(0, nbLignes - 1)
                colonne = random.randint(0, nbColonnes - 1)
            prairie.getListeListe()[ligne][colonne] = population.getListeLucioles()[i].symboliseLuciole()
        return prairie

#Q32
class Prairie:
    def __init__(self, listeListe, population):
        self.listeListe = listeListe
        self.population = population
    def __str__(self):
        return "Prairie(" + str(self.listeListe) + ", " + str(self.population) + ")"
    def getListeListe(self):
        return self.listeListe
    def getPopulation(self):
        return self.population
    def setListeListe(self, listeListe):
        self.listeListe = listeListe
    def setPopulation(self, population):
        self.population = population
    @staticmethod
    def creerPrairieVide(nbLignes, nbColonnes):
        listeListe = []
        for i in range(nbLignes):
            listeListe.append([])
            for j in range(nbColonnes):
                listeListe[i].append(".")
        return Prairie(listeListe, Population([]))
    def affichePrairie(self):
        for i in range(len(self.listeListe)):
            for j in range(len(self.listeListe[i])):
                print(self.listeListe[i][j], end="")
            print()
    @staticmethod
    def prairieLucioles(nbLignes, nbColonnes, population):
        prairie = Prairie.creerPrairieVide(nbLignes, nbColonnes)
        for i in range(len(population.getListeLucioles())):
            ligne = random.randint(0, nbLignes - 1)
            colonne = random.randint(0, nbColonnes - 1)
            while prairie.getListeListe()[ligne][colonne] != ".":
                ligne = random.randint(0, nbLignes - 1)
                colonne = random.randint(0, nbColonnes - 1)
            prairie.getListeListe()[ligne][colonne] = population.getListeLucioles()[i].symboliseLuciole()
        return prairie
    def simulationPrairie(self, nbIterations):
        for i in range(nbIterations):
            self.affichePrairie()
            print()
            self.population.deplacementLucioles()
            self.population.miseAJourLucioles()
            

#Q33
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import time

class Prairie:
    def __init__(self, listeListe, population):
        self.listeListe = listeListe
        self.population = population
    def __str__(self):
        return "Prairie(" + str(self.listeListe) + ", " + str(self.population) + ")"
    def getListeListe(self):
        return self.listeListe
    def getPopulation(self):
        return self.population
    def setListeListe(self, listeListe):
        self.listeListe = listeListe
    def setPopulation(self, population):
        self.population = population
    @staticmethod
    def creerPrairieVide(nbLignes, nbColonnes):
        listeListe = []
        for i in range(nbLignes):
            listeListe.append([])
            for j in range(nbColonnes):
                listeListe[i].append(".")
        return Prairie(listeListe, Population([]))
    def affichePrairie(self):
        for i in range(len(self.listeListe)):
            for j in range(len(self.listeListe[i])):
                print(self.listeListe[i][j], end="")
            print()
    @staticmethod
    def prairieLucioles(nbLignes, nbColonnes, population):
        prairie = Prairie.creerPrairieVide(nbLignes, nbColonnes)
        for i in range(len(population.getListeLucioles())):
            ligne = random.randint(0, nbLignes - 1)
            colonne = random.randint(0, nbColonnes - 1)
            while prairie.getListeListe()[ligne][colonne] != ".":
                ligne = random.randint(0, nbLignes - 1)
                colonne = random.randint(0, nbColonnes - 1)
            prairie.getListeListe()[ligne][colonne] = population.getListeLucioles()[i].symboliseLuciole()
        return prairie
    def simulationPrairie(self, nbIterations):
        for i in range(nbIterations):
            self.affichePrairie()
            print()
            self.population.deplacementLucioles()
            self.population.miseAJourLucioles()
    def simulationPrairieTkinter(self, nbIterations):
        fenetre = Tk()
        fenetre.title(" Simulation de la prairie ") 
        fenetre.geometry("500x500")
        fenetre.resizable(width=False, height=False)
        fenetre.configure(background="grey")
        for i in range(nbIterations):
            self.affichePrairie()
            print()
            self.population.deplacementLucioles()
            self.population.miseAJourLucioles()
        fenetre.mainloop()