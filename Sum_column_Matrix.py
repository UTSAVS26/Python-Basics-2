a=[[3,7,9,],[4,8,6,],[1,5,2]]
for x in range(0,3):
     s=0
     for y in range(0,3):
          s+=a[y][x]
     print("Sum of elements of ",x+1,"Column is: ",s)
