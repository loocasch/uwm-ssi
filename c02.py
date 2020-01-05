import math
from helpers import *
import random
# coding=utf-8

australian_TST = importFile("data/australian_TST.txt")
australian_TRN = importFile("data/australian_TRN.txt")

getNaiveBayes(australian_TST, australian_TRN, "c02", False)
