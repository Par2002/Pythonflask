# Day 9 :

# 1. Take a number from user and check whether it is prime or not. Use parameters to send the number to function.

# Eg. Enter a number 3
#        3 is prime

# 2. Write a function to print n factorial. Take n value as user input and pass as a parameter
# Eg. Enter a number 5
#       120
def prime(a):
    if a>1:
        for i in range(2,a):
            if a%i==0:
                print(a,"its not a prime number")
                break
        else:
            print(a,"its a prime number:")
    else:
        print(a,"its not a prime number")
    return a


a=int(input("Enter the number:"))
prime(a)
# _________________________________________________________________________________________
def fact(b):
    c=1
    for j in range(1,b+1):
        c=c*j
    print("factorial of",b,"is",c)
    
    return b 

b=int(input("Enter the factorial number:"))
fact(b)