#Analysis of Algorithms Assignment 3
#Giovanni Ruggirello

import random

#---Functions---#
def mergesort(arrayList):
   print (len(arrayList)) #size of array
   left = arrayList[0] #first value of array
   right = arrayList[-1] #last value of array

   print(left, right)

#----Main Code----#

random.seed(0)

B = [random.randint(0,10**7) for i in range(2**20)]

print (B[0:5])
print (B[10000:10005])

mergesort(B)
