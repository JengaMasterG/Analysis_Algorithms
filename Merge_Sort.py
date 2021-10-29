#Analysis of Algorithms Assignment 3
#Giovanni Ruggirello

import random

#---Functions---#

def mergeSort(arrayList): #Runs the Merge Sort Algorithm Functions

   if len(arrayList) > 1:
      half_array = int(len(arrayList)*0.5) #half the length of the array
   
      left = arrayList[:half_array] #left split of array
      right = arrayList[half_array:] #right half of array

      mergeSort(left)
      mergeSort(right)
      
      i = j = k = 0 #establishing loop variables

      while i < len(left) and j < len(right): #Sorting loop with two halves
         if left[i] < right[j]:
            arrayList[k] = left[i]
            i+=1
      
         else:
            arrayList[k] = right[j]
            j+=1
      
         k+=1
      
      #check for any leftover variables
      while i < len(left):
         arrayList[k] = left[i]
         i+=1
         k+=1
      
      while j < len(right):
         arrayList[k] = right[j]
         j+=1
         k+=1

   
#----Main Code----#
def main():
   random.seed(0) #creates random seed

   B = [random.randint(0,10**7) for i in range(2**20)] #generates random numbers

   print (B[0:5]) #prints inital order of first 5 values
   print (B[10000:10005]) #prins inital order of values 10000 to 10005

   mergeSort(B) #runs merge sort algorithm

   print (B[0:5]) #should be first 5 smallest values
   print (B[10000:10005]) #should be 5 different values

#main() #Uncomment/Comment to allow/disallow running standalone