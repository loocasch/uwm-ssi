def getClassDecisions(lists):
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


def getTransposeList(lists):
    return list(map(list, zip(*lists)))[:-1]


def getTransposeAllAtributesList(lists):
    return list(map(list, zip(*lists)))


def importFile(path):
    diabetes = []
    dataFile = open(path, "r").read().splitlines()
    for index, data in enumerate(dataFile):
        diabetes.append([])
        for n in data.split():
            diabetes[index].append(float(n))

    return diabetes
