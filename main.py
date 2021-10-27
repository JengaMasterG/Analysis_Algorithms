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

B = [random.randint(0,10**7) for i in range(2**20)] #generates random numbered list to 2 to 20th

print (B[0:5]) #prints inital order of first 5 values
print (B[10000:10005]) #prins inital order of values 10000 to 10005

MergeSort(B) #runs merge sort algorithm

print (B[0:5]) #should be first 5 smallest values
print (B[10000:10005]) #should be 5 different values

#---Running Binary Search---#
print("---Running Binary Search Algorithm---")

array_100 = [random.randint(10**10) for i in range(0,100)] #generates random numbered list to 100

print(array_100[1])

MergeSort(array_100) #Sort array

#Grab Random Integers for value finding. 2 for array, 1 not in array
rand1 = random.randint(0,100)
rand2 = random.randint(0,100)
rand3 = random.randint(0, 10**10)

print(rand1, rand2, rand3)

#Grab Random Integers for value finding. 2 for array, 1 not in array
rand1 = random.randint(0,100)
rand2 = random.randint(0,100)
rand3 = random.randint(0,10**10)

print(rand1, rand2, rand3)

find1 = array_100[rand1]
find2 = array_100[rand2]
find3 = rand3

BinarySearch(array_100, find1, find2,find3)