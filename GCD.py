#Analysis of Algorithms Assignment 3
#Giovanni Ruggirello

#---Functions---#
def gcd(a, b):
    if a==0:
        return b
    
    else:
        return gcd(b%a, a)

def main():
    a = 24
    b = 55

    print("Find GCD of", a, b)
    print(gcd(a,b))

    a = 85
    b = 10

    print("Find GCD of", a, b)
    print(gcd(a,b))

#main() #Uncomment/Comment to allow/disallow running standalone