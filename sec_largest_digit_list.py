# Python program to find the second largest digit in a list 'Num'
print("Enter the number of elements in a list: ")
N=int(input())
i=0
num=[]
while i<N:
     print("Enter list values: ")
     num1=int(input())
     num.append(num1)
     i+=1
print("The original list is: ",end='  ')
for i in range (N):
     print(num[i],end=' ')
if num[0]>num[1]:
     m,m2=num[0],num[1]
else:
     m,m2=num[1],num[0]
for x in num[2:]:
     if x>m:
          m2,m=m,x
     else:
          m2=x
print()
print("The second largest digit in a list is: ",m2)
