# Program to check a given number is prime or not
num=int(input ("Enter Num?"))
for i in range (2,num//2+1):
     if num%i==0:
          print (num,"is Not a Prime Number")
          break
     else:
          print(num,"is a Prime Number")
