import numpy
import random

from helpers import *


def TrainAndTest(lists, ratio):
    tmpDictionary = {}
    lengthRowList = len(lists)
    lengthColumnLists = len(lists[0])
    lists = random.sample(lists, lengthRowList)
    tmpDictionary['train'] = lists[:int(lengthRowList * ratio)]
    tmpDictionary['test'] = lists[int(lengthRowList * ratio):lengthRowList]
    return tmpDictionary


def MonteCarloCrossValidation(lists, numberFold, ratio):
    sumGlobalAccuracy = 0
    sumBalancedAccuracy = 0
    for fold in range(numberFold):
        naiveBayes = getNaiveBayes(TrainAndTest(data, 0.5)['test'], TrainAndTest(data, 0.5)['train'], "MonteCarloCrossValidationFold", True)
        sumGlobalAccuracy += naiveBayes[0]
        sumBalancedAccuracy += naiveBayes[1]
    acc_bayes = open("data/MonteCarloCrossValidationAverage_acc_bayes.txt", "w+")
    acc_bayes.write('Average Global Accuracy: {}\n'.format(sumGlobalAccuracy / numberFold))
    acc_bayes.write('Average Balanced Accuracy: {}\n'.format(sumBalancedAccuracy / numberFold))
    acc_bayes.close()


def CrossValidation(lists, k):
    lengthRowList = len(lists)
    n = int(lengthRowList / k)
    lists = random.sample(lists, lengthRowList)
    chunkLists = [lists[i:i + n] for i in range(0, len(lists), n)]
    for index, li in enumerate(chunkLists):
        if(len(li) != n):
            chunkLists.pop(index)
    sumGlobalAccuracy = 0
    sumBalancedAccuracy = 0
    for tst in chunkLists:
        trainList = []
        for trn in chunkLists:
            if(tst != trn):
                for t in trn:
                    trainList.append(t)

        naiveBayes = getNaiveBayes(tst, trainList, "CrossValidation", True)
        sumGlobalAccuracy += naiveBayes[0]
        sumBalancedAccuracy += naiveBayes[1]
    acc_bayes = open("data/CrossValidationAverage_acc_bayes.txt", "w+")
    acc_bayes.write('Average Global Accuracy: {}\n'.format(sumGlobalAccuracy / k))
    acc_bayes.write('Average Balanced Accuracy: {}\n'.format(sumBalancedAccuracy / k))
    acc_bayes.close()


data = importFile("data/australian.txt")

TrainAndTestLists = TrainAndTest(data, 0.5)
getNaiveBayes(TrainAndTestLists['test'], TrainAndTestLists['train'], "TrainAndTest", False)

MonteCarloCrossValidation(data, 5, 0.5)

CrossValidation(data, 5)
