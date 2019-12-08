import math
# coding=utf-8


def getClassDecision(lists):
    tmpList = []
    for index, li in enumerate(lists, start=1):
        if(li[-1] not in tmpList):
            tmpList.append(li[-1])
    return tmpList


def getLengthClassDecision(lists, classDecisions):
    tmpList = {}

    for clDec in classDecisions:
        tmpList[clDec] = 0
        for li in lists:
            if(li[-1] == clDec):
                tmpList[clDec] += 1

    return tmpList


def getMinMaxAtributes(lists):
    tmpDictionary = {}
    for index, li in enumerate(lists, start=1):
        tmpDictionary['atr. {}'.format(index)] = {
            'max': max(li), 'min': min(li)}
    return tmpDictionary


def getUniqueAtributes(lists):
    tmpDictionary = {}
    for index, row in enumerate(lists, start=1):
        tmpList = []
        for item in row:
            if(item not in tmpList):
                tmpList.append(item)
        tmpDictionary['atr. {}'.format(index)] = sorted(tmpList)
    return tmpDictionary


def getStandardDeviation(lists, type):
    tmpDictionary = {}
    for index, li in enumerate(lists, start=1):
        n = len(li)  # Obliczanie N
        u = sum(li)/n  # Obliczanie u
        xusquared = 0
        for item in li:
            xusquared += (item - u) ** 2  # Obliczanie sum|x - u|^2

        # Obliczanie sqrt((sum|x - u|^2) / N)
        xusquared = math.sqrt(xusquared/n)
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


def getTransposeList(lists):
    return list(map(list, zip(*lists)))[:-1]


diabetes = []
dataFile = open("data/diabetes.txt", "r").read().splitlines()
for index, data in enumerate(dataFile):
    diabetes.append([])
    for n in data.split():
        diabetes[index].append(float(n))

classDecisions = getClassDecision(diabetes)
print("klasy decyzyjne:{} ".format(classDecisions))
print("=============================================================")

lengthclassDecisions = getLengthClassDecision(diabetes, classDecisions)

for item in lengthclassDecisions:
    print("klasa decyzyjna: {}  wielkosc: {}".format(
        item, lengthclassDecisions[item]))
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

classDecisions = getClassDecision(diabetes)
standardDeviationForClassDecisions = getStandardDeviationForClassDecisions(
    diabetes, classDecisions)

for standardDeviationForClassDecision in standardDeviationForClassDecisions:
    print('{} odchylenie standardowe: {}'.format(standardDeviationForClassDecision, getStandardDeviation(
        [standardDeviationForClassDecisions[standardDeviationForClassDecision]], 'class')))
