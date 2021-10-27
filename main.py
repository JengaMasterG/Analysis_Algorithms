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

B = [random.randint(0,10**7) for i in range(2**20)] #generates random numbers

print (B[0:5]) #prints inital order of first 5 values
print (B[10000:10005]) #prins inital order of values 10000 to 10005

MergeSort(B) #runs merge sort algorithm

print (B[0:5]) #should be first 5 smallest values
print (B[10000:10005]) #should be 5 different values

#---Running Binary Search---#
print("---Running Binary Search Algorithm---")