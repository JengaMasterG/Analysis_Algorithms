#Analysis of Algorithms Assignment 3
#Giovanni Ruggirello

#---Functions---#
def fibonacciRecursive(n):

    if n <=1:
        return n
    
    else:
        return(fibonacciRecursive(n-1) + fibonacciRecursive(n-2))

def powerRecursive(n):

    if n <2:
        return n
    
    else:
        sum = n**2 + (n-1)**2
        return sum

#---Main Function---#
def main():

    n_input = int(input("Please enter a number for Fibonacci sequence: ")) #user input for variable > 0

    if n_input <= 0: #Error Handling
        print("That is not a valid input!")
    
    else:
        print("Your Fibonacci Sequence: ")
        for i in range(n_input):
            print(fibonacciRecursive(i))
        
        print("Sums of n: ")
        for i in range(n_input):
            print(powerRecursive(i))

main() #Uncomment/Comment to allow/disallow running standalone