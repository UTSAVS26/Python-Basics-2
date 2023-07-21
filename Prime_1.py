# Program to check if a number is prime or not
num = int(input("Enter a number: "))
# prime numbers are greater than 1
for i in range(2,num):
     # check for factors
     if (num % i) == 0:
          print(num,"is not a prime number")
          print(i,"times",num//i,"is",num)
          break
     else:
          print(num,"is a prime number")
# if input number is less than
# or equal to 1,the number is
#not a prime number
else:
     print(num,"is not a prime number")
