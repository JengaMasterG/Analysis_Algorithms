#Analysis of Algorithms Assignment 3
#Giovanni Ruggirello

#---THIS CODE WILL NOT RUN WITHOUT Merge_Sort.py---#
from Merge_Sort import MergeSort

import random

#---Functions---#
def BinarySearch(arrayList, find1, find2, find3):
    if:
    
    else:
        return -1


#----Main Code ----#
def main():
    random.seed(0)

    array_100 = [random.randint(0, 10**10) for i in range(0,100)] #generates random numbered list to 100

    print(array_100[1])

    MergeSort(array_100) #Sort array

    #Grab Random Integers for value finding. 2 for array, 1 not in array
    rand1 = random.randint(0,100)
    rand2 = random.randint(0,100)
    rand3 = random.randint(0,10**10)

    print(rand1, rand2, rand3)

    find1 = array_100[rand1]
    find2 = array_100[rand2]
    find3 = rand3

    BinarySearch(array_100, find1, find2,find3)

main() #Uncomment/Comment to allow/disallow running standalone