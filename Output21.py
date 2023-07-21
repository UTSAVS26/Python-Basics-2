Num=[10,51,2,18,4,31,13,5,23,64,29]
print("List elements are: ",end=" ")
for i in Num:
     print(i,end=" ")
print()
element=int(input("Enter search element: "))
Flag=0
for i in Num:
     if (i==element):
          Flag=1
     if Flag==1:
          print("Element found in the list",element)
          break
     else:
          print("Element not found in the list",element)
          break
