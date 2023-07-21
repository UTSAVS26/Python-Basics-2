# Python program to print the reverse list of the original list
Num= [23, 54, 34, 44, 35, 66]
print ("The original list elements are: ",end=" ")
for i in Num:
     print (i, end=" ")
ln= len(Num)                        # total number of elements in Num list
i, ctr= 0, -1

# ctr value starts from right to left [-1,-2,-3,...]
# i will process all the elements in the list
print ("\n The reverse order list elements are: ",end=" ")
while i<=ln-1:
     print (Num[ctr], end=" ")
     ctr-=1
     i+=1
