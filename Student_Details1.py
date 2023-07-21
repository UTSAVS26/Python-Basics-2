n = int(input("Enter number of students: ")) 
result = {} 
for i in range(n):
     print("Enter Details of student No.", i+1)
     rno = int(input("Roll No: ")) 
     marks1 = int(input("Marks of English: "))
     marks2 = int(input("Marks of Physics: "))
     marks3 = int(input("Marks of Maths: "))
     marks4 = int(input("Marks of Chemistry: "))
     marks5 = int(input("Marks of Biology: "))
     result[rno] = [marks1,marks2,marks3,marks4,marks5] 
print(result)
sum=(marks1+marks2+marks3+marks4+marks5)/5
print("Roll no.: ",rno,"Sum of all the Subjects is: ",sum)
