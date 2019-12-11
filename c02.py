import math
from helpers import *
import random
# coding=utf-8


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


australian_TST = importFile("data/australian_TST.txt")
australian_TRN = importFile("data/australian_TRN.txt")

classDecisions = getClassDecisions(australian_TRN)
lengthClassDecisions = getLengthClassDecision(australian_TRN, classDecisions)
lengthRow = len(australian_TRN)
atributes = getTransposeAllAtributesList(australian_TRN)
counts = {}
decisions = {}
correctDecision = 0

for index1, row in enumerate(australian_TST, start=1):
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
        if(decisions[count]['dec'] == australian_TST[index1][-1]):
            decisions[count]['correct'] = True
            correctDecision += 1
        else:
            decisions[count]['correct'] = False

dec_bayes = open("data/dec_bayes.txt", "w+")
dec_bayes.write("Obiekt tst\t\tUkryta decyzja eksperta\t\tDecyzja naszego klasyfikatora\t\tPoprawnie?\n")
dec_bayes.write("-------------------------------------------------------------------------------------------------------------\n")
for index, decision in enumerate(decisions):
    dec_bayes.write("%s\t\t\t\t%f\t\t\t\t%s\t\t\t%s\n" % (decision, australian_TST[index][-1], decisions[decision]['dec'], 'Tak' if decisions[decision]['correct'] else 'Nie'))
dec_bayes.write("-------------------------------------------------------------------------------------------------------------\n")
dec_bayes.close()

acc_bayes = open("data/acc_bayes.txt", "w+")
acc_bayes.write('Global Accuracy: {}\n'.format(correctDecision / len(decisions)))
acc_bayes.write('Balanced Accuracy: {}\n'.format(groupDecisions(decisions) / len(classDecisions)))
acc_bayes.close()
