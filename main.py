#Analysis of Algorithms Assignment 3
#Giovanni Ruggirello
#---Run All Functions via main.py ---#

from Merge_Sort import MergeSort
from Binary_Search import BinarySearch
import random

#--Establish Random seed---#
random.seed(0)

#---Running Merge Sort---#
print("---Running Merge Sort Algorithm----")

mergeArray = [random.randint(0,10**7) for i in range(2**20)] #generates random numbered list to 2 to 20th

print (mergeArray[0:5]) #prints inital order of first 5 values
print (mergeArray[10000:10005]) #prins inital order of values 10000 to 10005

MergeSort(mergeArray) #runs merge sort algorithm

print (mergeArray[0:5]) #should be first 5 smallest values
print (mergeArray[10000:10005]) #should be 5 different values

#---Running Binary Search---#
print("\n---Running Binary Search Algorithm---")

array_100 = [random.randint(0, 10**10) for i in range(0,100)] #generates random numbered list to 100

MergeSort(array_100) #Sort array

#Print Array after its sorted
print(array_100)

#Grab Random Integers for value finding. 2 for array, 1 not in array
rand1 = random.randint(0,100)
rand2 = random.randint(0,100)
rand3 = random.randint(0,10**10)

#Set Values for Find Variables from Random Variables
find1 = array_100[rand1]
find2 = array_100[rand2]
find3 = rand3

print("\nSearching for {}, {}, and {}...".format(find1, find2, find3))

#Find Values via Binary Search
found1 = BinarySearch(array_100, 0, len(array_100) - 1, find1)
found2 = BinarySearch(array_100, 0, len(array_100) - 1, find2)
found3 = BinarySearch(array_100, 0, len(array_100) - 1, find3)

#Print Results
if found1 is None:
    print("\n{} does not exist in Array".format(find1))
    
else:
    print("\n{} exists in Array".format(find1))

if found2 is None:
    print("{} does not exist in Array".format(find2))
    
else:
    print("{} exists in Array".format(find2))
    
if found3 is None:
    print("{} does not exist in Array".format(find3))
    
else:
    print("{} exists in Array".format(find3))