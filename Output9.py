fruit={ }
F1 = [‘Apple’ , ‘Banana’ , ‘apple’ , ‘Banana’]
for index in F1:
     if index in fruit:
          fruit[index]+=1
     else:
          fruit[index]=1
     print(fruit)
print(len(fruit))
