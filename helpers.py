import random
import numpy


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


def groupDecisions(decisions):
    tmpDictionary = {}
    sumCorectDecision = 0
    for decision in decisions:
        if(decisions[decision]['dec'] not in tmpDictionary):
            tmpDictionary[decisions[decision]['dec']] = {'correct': 0, 'count': 1}
        else:
            tmpDictionary[decisions[decision]['dec']]['count'] += 1
        if(decisions[decision]['correct']):
            tmpDictionary[decisions[decision]['dec']]['correct'] += 1
    for key in tmpDictionary:
        sumCorectDecision += tmpDictionary[key]['correct'] / tmpDictionary[key]['count']
    return sumCorectDecision


def getNaiveBayes(tst, train, nameFile, getGaccBacc):
    classDecisions = getClassDecisions(train)
    lengthClassDecisions = getLengthClassDecision(train, classDecisions)
    lengthRow = len(train)
    atributes = getTransposeAllAtributesList(train)
    counts = {}
    decisions = {}
    correctDecision = 0

    for index1, row in enumerate(tst, start=1):
        counts['x{}'.format(index1)] = {}
        for classDecision in classDecisions:
            counts['x{}'.format(index1)][classDecision] = {}
            for index2, item in enumerate(row[:-1]):
                counts['x{}'.format(index1)][classDecision]['a{}'.format(index2)] = 0
                count = 0
                for index3, atribute in enumerate(atributes[index2]):
                    if(item == atribute and classDecision == atributes[-1][index3]):
                        count += 1
                counts['x{}'.format(index1)][classDecision]['a{}'.format(index2)] = count

    for index1, count in enumerate(counts):
        for classDecision in counts[count]:
            for item in counts[count][classDecision]:
                if(counts[count][classDecision][item] == 0):
                    for itemClassDecision in counts[count]:
                        if(counts[count][itemClassDecision][item] != 0):
                            counts[count][itemClassDecision][item] += 1
            counts[count][classDecision]['p'] = lengthClassDecisions[classDecision] / lengthRow * (sum(counts[count][classDecision].values()) / lengthClassDecisions[classDecision])

        prevItem = None
        for index2, classDecision in enumerate(counts[count]):
            if(prevItem == None):
                prevItem = [counts[count][classDecision]['p'], classDecision]
                continue
            else:
                decisions[count] = {}
                if(prevItem[0] > counts[count][classDecision]['p']):
                    decisions[count]['dec'] = prevItem[1]
                elif(prevItem[0] == counts[count][classDecision]['p']):
                    decisions[count]['dec'] = random.choice(classDecisions)
                else:
                    decisions[count]['dec'] = classDecision
            if(decisions[count]['dec'] == tst[index1][-1]):
                decisions[count]['correct'] = True
                correctDecision += 1
            else:
                decisions[count]['correct'] = False

    if(getGaccBacc):
        globalAccuracy = correctDecision / len(decisions)
        balancedAccuracy = groupDecisions(decisions) / len(classDecisions)
        return globalAccuracy, balancedAccuracy
    else:
        dec_bayes = open("data/%s_dec_bayes.txt" % nameFile, "w+")
        dec_bayes.write("Obiekt tst\t\tUkryta decyzja eksperta\t\tDecyzja naszego klasyfikatora\t\tPoprawnie?\n")
        dec_bayes.write("-------------------------------------------------------------------------------------------------------------\n")
        for index, decision in enumerate(decisions):
            dec_bayes.write("%s\t\t\t\t%f\t\t\t\t%s\t\t\t%s\n" % (decision, tst[index][-1], decisions[decision]['dec'], 'Tak' if decisions[decision]['correct'] else 'Nie'))
        dec_bayes.write("-------------------------------------------------------------------------------------------------------------\n")
        dec_bayes.close()

        acc_bayes = open("data/%s_acc_bayes.txt" % nameFile, "w+")
        acc_bayes.write('Global Accuracy: {}\n'.format(correctDecision / len(decisions)))
        acc_bayes.write('Balanced Accuracy: {}\n'.format(groupDecisions(decisions) / len(classDecisions)))
        acc_bayes.close()
