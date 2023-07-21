def toWords(amount):
     d_num = {'0':'Zero','1':'One','2':'Two','3':'Three','4':'Four',
              '5':'Five','6':'Six','7':'Seven','8':'Eight','9':'Nine'}
     amount = str(amount)
     st = ''
     for num in amount:
          i = d_num.get(num)
          st += (i+' ')
     return st.strip()
am = input("Enter the amount:  ")
words = toWords(am)
print("Amount in words is  --- ",words)
