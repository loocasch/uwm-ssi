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


data = importFile("data/australian.txt")
TrainAndTestLists = TrainAndTest(data, 0.5)
getNaiveBayes(TrainAndTestLists['test'], TrainAndTestLists['train'], "TrainAndTest")
