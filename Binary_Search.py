#Analysis of Algorithms Assignment 3
#Giovanni Ruggirello

#---THIS CODE WILL NOT RUN WITHOUT Merge_Sort.py---#
from Merge_Sort import MergeSort

import random

#---Functions---#
#def BinarySearch():


#----Main Code ----#
def main():
    random.seed(0)

    array_100 = [random.random() for i in range(0,100)]

    print(len(array_100))

    MergeSort(array_100)

#main() #Uncomment/Comment to allow/disallow running standalone