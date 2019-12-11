import math
from helpers import *
# coding=utf-8


def getStandardDeviation(lists, type):
    tmpDictionary = {}
    for index, li in enumerate(lists, start=1):
        n = len(li)  # Obliczanie N
        u = sum(li) / n  # Obliczanie u
        xusquared = 0
        for item in li:
            xusquared += (item - u) ** 2  # Obliczanie sum|x - u|^2

        # Obliczanie sqrt((sum|x - u|^2) / N)
        xusquared = math.sqrt(xusquared / n)
        if(type == 'atr'):
            tmpDictionary['atr. {}'.format(index)] = xusquared
        elif(type == 'class'):
            tmpDictionary = xusquared

    return tmpDictionary


def getStandardDeviationForClassDecisions(lists, classDecisions):
    tmpDictionary = {}
    for classDecision in classDecisions:
        tmpList = []
        for li in lists:
            if(classDecision == li[-1]):
                tmpList.extend(li)
        tmpDictionary['klasa decyzyjna {}'.format(
            classDecision)] = tmpList
    return tmpDictionary


diabetes = importFile("data/diabetes.txt")

classDecisions = getClassDecisions(diabetes)
print("klasy decyzyjne:{} ".format(classDecisions))
print("=============================================================")

lengthclassDecisions = getLengthClassDecision(diabetes, classDecisions)

for item in lengthclassDecisions:
    print("klasa decyzyjna: {}  wielkosc: {}".format(item, lengthclassDecisions[item]))
print("=============================================================")

minMaxAtributes = getMinMaxAtributes(getTransposeList(diabetes))
for item in sorted(minMaxAtributes):
    print("{} {}".format(item, minMaxAtributes[item]))

print("=============================================================")

uniqueAtributes = getUniqueAtributes(getTransposeList(diabetes))
for item in sorted(uniqueAtributes):
    print("{} {}".format(item, len(uniqueAtributes[item])))

print("=============================================================")

uniqueAtributes = getUniqueAtributes(getTransposeList(diabetes))
for item in sorted(uniqueAtributes):
    print("\n{} {}".format(item, uniqueAtributes[item]))

print("=============================================================")

standardDeviationForAttributes = getStandardDeviation(
    getTransposeList(diabetes), 'atr')

for item in sorted(standardDeviationForAttributes):
    print("{} odchylenie standardowe: {}".format(
        item, standardDeviationForAttributes[item]))

print("=============================================================")

classDecisions = getClassDecisions(diabetes)
standardDeviationForClassDecisions = getStandardDeviationForClassDecisions(diabetes, classDecisions)

for standardDeviationForClassDecision in standardDeviationForClassDecisions:
    print('{} odchylenie standardowe: {}'.format(standardDeviationForClassDecision, getStandardDeviation([standardDeviationForClassDecisions[standardDeviationForClassDecision]], 'class')))
