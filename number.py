# An example of a recursive function to
# find the factorial of a number
import time

def calc_factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""
    print(x)
    if x == 1:
        print(x)
        return 1
    else:
        print(x)
        return (x * calc_factorial(x-1))

t = time.time()
num = 4
print("The factorial of", num, "is", calc_factorial(num))
print("Time taken for 1st pgm : ",time.time()-t)
# ----------------------------------------------------------

fact = int(input("Enter number : "))
t1 = time.time()
n = fact - 1
while n != 0:
    print(fact, "*", n)
    fact = fact * n
    n -= 1
print("Final value of Factorial number = ",fact)
# 4 * 3 * 2 * 1
print("Time taken for 2nd pgm : ",time.time()-t1)