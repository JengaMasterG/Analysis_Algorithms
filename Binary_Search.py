#Analysis of Algorithms Assignment 3
#Giovanni Ruggirello

#---THIS CODE WILL NOT RUN WITHOUT Merge_Sort.py---#
from Merge_Sort import MergeSort

import random

#---Functions---#
def BinarySearch(arrayList, arrStart, arrLength, findValue):
    #Check that Array size is larger than 1
    if arrStart <= arrLength:
        #Find Middle fo Array
        arrHalf = int(len(arrayList)*0.5)

        mid = arrayList[arrHalf]
    
        if findValue == mid:
            return mid
    
        elif findValue < mid:
            return

        elif findValue > mid:
            return

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

    #Set Values for Find Variables from Random Variables
    find1 = array_100[rand1]
    find2 = array_100[rand2]
    find3 = rand3

    BinarySearch(array_100, 0, len(array_100) - 1,find1)

main() #Uncomment/Comment to allow/disallow running standalone