# Program to find square root and check whether
# it is prime or not.
num=int(input("Enter a number: "))
import math
a= int(math.sqrt(num))
b=0
for i in range(2,a):
     if a%i==0:
          b= b+1
if b==0:
     print(a, "is a prime number")
else:
     print (a,"is not prime number")
