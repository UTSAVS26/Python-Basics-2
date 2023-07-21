#Program to check a given number is prime or not
num=int(input ("Enter Num: "))
flag=1
for i in range (2,num//2+1):
     if num%i==0:
          flag=0
          break
if flag==1:
     print (num,"is a Prime Number.")
else:
     print(num,"is Not a Prime Number.")
