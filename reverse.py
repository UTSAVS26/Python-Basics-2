# Program to print the reverse order of the number which is obtained from the user
Orig_num=int(input("Enter three digit number: "))              # Original Number
num=Orig_num
Rev_num=0                                                                       # Reverse Number
while num>0:
     digit =num%10
     Rev_num = Rev_num *10+digit
     num=int(num//10)
print ("Original Number is: ", Orig_num)
print ("Reverse Number is: ", Rev_num)
