import os
import sys

print("Hello You!")
print("Ik ben Piter")
print("Wat is jouw naam?")
voorNaam = input()

print("Jouw naam is:")
print("Hello " + str(voorNaam))
print("Ik ben een nieuwkomer op het Media College Amsterdam")
print("")
print("Door een aantal vragen over mij te beantwoorden leer je mij beter kennen")
print("")
print("")


def q1():
    print("Waar kom ik vandaan?")
    print("")
    print(" A. Amsterdam")
    print(" B. Castricum")
    print(" C. Zaandam")
    a1 = input(" Kies 'A', 'B' of 'C' >>>>> ")
    if (a1 == "B"):
        print("")
        print("Goed!")
    elif (a1 != "B"):
        print("Fout!")
q1()

def q2():
    print("Hoe oud ben ik?")
    print("")
    print(" A. 17")
    print(" B. 18")
    print(" C. 16")
    a2 = input(" Kies 'A', 'B' of 'C' >>>>> ")
    if (a2 == "A"):
        print("")
        print("Goed!")
    elif (a2 != "A"):
        print("Fout!")
q2()

def q3():
    print("Heb ik (een) broer(s) of zus(sen)?")
    print("")
    print(" A. 1 zus en 1 broer")
    print(" B. 2 broers")
    print(" C. 1 broer")
    a3 = input(" Kies 'A', 'B' of 'C' >>>>> ")
    if (a3 == "C"):
        print("")
        print("Goed!")
    elif (a3 != "C"):
        print("Fout!")
q3()

dontclose = input()
