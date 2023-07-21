number=int(input("Enter number: "))
count=0
digit=int(input("Enter digit to count: "))
n=number
while n>0:
     if int(n%10)==digit:
          count+=1
     n=int(n/10)
print(f"Number: {number}")
print(f"Digit {digit} appears {count} times.")
