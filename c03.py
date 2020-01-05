import numpy
import random

from helpers import *
from c02 import groupDecisions, getNaiveBayes


def TrainAndTest(lists, ratio):
    tmpDictionary = {}
    lengthRowList = len(lists)
    lengthColumnLists = len(lists[0])
    random.shuffle(lists)
    tmpDictionary['train'] = lists[:int(lengthRowList * ratio)]
    tmpDictionary['test'] = lists[int(lengthRowList * ratio):lengthRowList]
    return tmpDictionary


def MonteCarloCrossValidation(lists, numberFold, ratio):
    sumGlobalAccuracy = 0
    sumBalancedAccuracy = 0
    for fold in range(numberFold):
        x = getNaiveBayes(TrainAndTest(data, 0.5)['test'], TrainAndTest(data, 0.5)['train'], "MonteCarloCrossValidationFold%s" % (fold + 1), True)
        sumGlobalAccuracy += x[0]
        sumBalancedAccuracy += x[1]
    acc_bayes = open("data/MonteCarloCrossValidationAverage_acc_bayes.txt", "w+")
    acc_bayes.write('Average Global Accuracy: {}\n'.format(sumGlobalAccuracy / numberFold))
    acc_bayes.write('Average Balanced Accuracy: {}\n'.format(sumBalancedAccuracy / numberFold))
    acc_bayes.close()


data = importFile("data/australian.txt")

TrainAndTestLists = TrainAndTest(data, 0.5)
getNaiveBayes(TrainAndTestLists['test'], TrainAndTestLists['train'], "TrainAndTest", False)

MonteCarloCrossValidation(data, 5, 0.5)
