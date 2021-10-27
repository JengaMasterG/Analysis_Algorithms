#Analysis of Algorithms Assignment 3
#Giovanni Ruggirello

#---THIS CODE WILL NOT RUN WITHOUT Merge_Sort.py---#
from Merge_Sort import MergeSort

import random

#---Functions---#
def BinarySearch(arrayList, arrStart, arrLength, findValue):
    #Check that Array size is larger than 1
    if arrLength >= arrStart:
        
        #Find Middle fo Array: Take Start of Array Value. Sub max 

        mid = arrStart + (arrLength - arrStart) // 2 #Ex. 0 + (99-0) // 2 = 50 as mid value
        
        if findValue == arrayList[mid]:
            return mid
    
        elif findValue < arrayList[mid]: #If value is LT mid value, search left side of array
            return BinarySearch(arrayList, arrStart, mid - 1, findValue)

        elif findValue > arrayList[mid]: #If value is GT mid value, search right side of arrray
            return BinarySearch(arrayList, mid + 1, arrLength, findValue)

        else:
            return -1


#----Main Code ----#
def main():
    random.seed(0)

    array_100 = [random.randint(0, 10**10) for i in range(0,100)] #generates random numbered list to 100

    print(array_100[1])

    MergeSort(array_100) #Sort array

    print(array_100[1])

    #Grab Random Integers for value finding. 2 for array, 1 not in array
    rand1 = random.randint(0,100)
    rand2 = random.randint(0,100)
    rand3 = random.randint(0,100)

    #Set Values for Find Variables from Random Variables
    find1 = array_100[rand1]
    find2 = array_100[rand2]
    find3 = rand3

    print("Searching for {}, {}, and {}...".format(find1, find2, find3))

    #Find Values via Binary Search
    found1 = BinarySearch(array_100, 0, len(array_100) - 1, find1)
    found2 = BinarySearch(array_100, 0, len(array_100) - 1, find2)
    found3 = BinarySearch(array_100, 0, len(array_100) - 1, find3)

    print(found1, found2, found3)

    #Print Results
    if found1 is None:
        print("{} does not exist in Array".format(find1))
    
    else:
        print("{} exists in Array".format(find1))

    if found2 is None:
        print("{} does not exist in Array".format(find2))
    
    else:
        print("{} exists in Array".format(find2))
    
    if found3 is None:
        print("{} does not exist in Array".format(find3))
    
    else:
        print("{} exists in Array".format(find3))

main() #Uncomment/Comment to allow/disallow running standalone