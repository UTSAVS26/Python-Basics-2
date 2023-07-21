#Write python code to designa Menu Driven program
#for the following :
#1. AMOUNT to Words Converter and vice versa
#2. Binary to Decimal converter
#3. Decimal to Binary converter
#4. Decimal to Hex converter
#5. Decimal to Octal converter
#6. Binary to Decimal converter
#7. Binary to Hex converter
#8. Binary to Octal converter
#9. Binary to Text converter
#10. Hex to Decimal converter
#11. Hex to Binary converter
#12. Hex to Octal converter
#13. Octal to Decimal converter
#14. Octal to Binary converter
#15. Octal to Hex converter

##########################################################################################
#1

def toWords(amount):
     d_num = {'0':'Zero','1':'One','2':'Two','3':'Three','4':'Four','5':'Five','6':'Six','7':'Seven','8':'Eight','9':'Nine'}
     amount = str(amount)
     st = ''
     for num in amount:
          i = d_num.get(num)
          st += (i+' ')
     return st.strip()  #strip to remove last and first space

def toAmount(words):
     words = words.title()
     words = words.strip()   #So that words can be obtained from dictionary
     d_am = {'Zero': '0', 'One': '1', 'Two': '2', 'Three': '3', 'Four': '4', 'Five': '5', 'Six': '6', 'Seven': '7', 'Eight': '8', 'Nine': '9'}
     l = words.split()    #to make a list of words
     st = ''
     for word in l:
         i = d_am.get(word)
         if i == None:   #word not in dictionary
             print("Please check for mistypes")
             st += ' - '
         else:
             st += i
     return st.strip()   #strip to remove last and first space

###########################################################################################

#dictionaries for conversions
d_hex = {'0000':'0','0001':'1','0010':'2','0011':'3','0100':'4','0101':'5','0110':'6','0111':'7','1000':'8','1001':'9','1010':'A','1011':'B','1100':'C','1101':'D','1110':'E','1111':'F'}
d_hex_rev = {}    #keys and values of d_hex are inverted
for x,y in d_hex.items():
     d_hex_rev[y] = x
d_oct = {"000":"0","001":"1","010":"2","011":"3","100":"4","101":"5","110":"6","111":"7"}   #3 bits for octal
d_oct_rev = {}
for x,y in d_oct.items():
     d_oct_rev[y] = x

#2
def btd(binary):
     binary = str(binary)
     x = len(binary)-1    #one less for the powers to which the base will be raised
     base = 2
     final = 0
     for dig in binary:
         i = int(dig)*(base**x)
         final += i
         x -= 1
     return str(final)

#3
def dtb(dec):
     base = 2
     dec = int(dec)
     final = ''
     while dec!=0:    # dec is floor divided until it is zero
         rem = dec%base    #remainder on dividing by two
         dec = dec//base
         final += str(rem)    #remainder to be inserted in the string
     final = final[::-1]    #remainder to be taken from bottom till top
     return final

#4
def dth(dec):
     d_hex_n = {'10':'A','11':'B','12':'C','13':'D','14':'E','15':'F'}
     base = 16
     dec = int(dec)
     final = ''
     while dec!=0:
          rem = dec%base
          dec = dec//base
          if rem <=9:
               final += str(rem)
          else:
               final += d_hex_n.get(str(rem))
     final = final[::-1]
     return final

#5
def dto(dec):
     base = 8
     dec = int(dec)
     final = ''
     while dec!=0:
          rem = dec%base
          dec = dec//base
          final += str(rem)
     final = final[::-1]
     return final

#7
def bth(binary):
     binary = str(binary)
     x = len(binary)
     binary = ((4-(x%4))*'0')+binary   # i.e. the difference in 4 and remainder on dividing by 4
                                      # times 0 to be inserted at LHS to make groups
     final = ''
     x_n = len(binary)   #the length of the final string
     for i in range(0,x_n-1,4):    #x_n-1 because last digit not to be included in loop
          four_bit = binary[i:i+4]   #4 bits group
          hexa = d_hex.get(four_bit)
          final += hexa
     return final

#8
def bto(binary):
     binary = str(binary)
     x= len(binary)
     binary = ((3-(x%3))*'0')+binary
     final = ''
     x_n = len(binary)
     for i in range(0,x_n-1,3):
          three_bit = binary[i:i+3]
          octa = d_oct.get(three_bit)
          final += octa
     return final

#10
def htd(hexa):
     hexa = str(hexa)
     base = 16
     x = len(hexa)-1
     final = 0
     for dig in hexa:
          if dig.isalpha():    #to convert alphabets A,B,C,D,E,F into their numeric values
               d = {'A':'10','B':'11','C':'12','D':'13','E':'14','F':'15'}
               dig = dig.upper()
               dig = d.get(dig)
          i = int(dig)*(base**x)
          final += i
          x -= 1
     return str(final)

#11
def htb(hexa):
     hexa = str(hexa)
     final = ''
     for dig in hexa:
          i = d_hex_rev.get(dig)    #simply substitute each hexa with corresponding binary
          final += i
     return final

#12
def hto(hexa):
     binary = htb(hexa)    #convert hexadecimal to binary
     binary = binary.lstrip('0000')    #remove all zeroes at LHS
     octa = bto(binary)     #convert binary to octal
     return octa

#13
def otd(octa):
     octa = str(octa)
     x = len(octa)-1
     base = 8
     final = 0
     for dig in octa:
          i = int(dig)*(base**x)
          x-=1
          final += i
     return final

#14
def otb(octa):
     octa = str(octa)
     final = ''
     for dig in octa:
          i = d_oct_rev.get(dig)
          final += i
     return final

#15
def oth(octa):
     binary = otb(octa)
     binary = binary.lstrip('0000')
     hexa = bth(binary)
     return hexa

############################################################################################
#main program


print("Menu Driven program to do the following:-")
print('''1. AMOUNT to Words Converter
2. Words to Amount Converter
3. Binary to Decimal Converter
4. Decimal to Binary Converter
5. Decimal to Hex Converter
6. Decimal to Octal Converter
7. Binary to Hex Converter
8. Binary to Octal Converter
9. Binary to Text Converter
10. Hex to Decimal Converter
11. Hex to Binary Converter
12. Hex to Octal Converter
13. Octal to Decimal Converter
14. Octal to Binary Converter
15. Octal to Hex converter''')

inp = input("Enter your option (1 to 15): ")
print()
if not inp.isdigit():   #input is not a digit
     print("Enter a correct option!")
else:
     inp =int(inp)
     if inp >15 or inp<1:    #value out of range
          print("Enter correct range of values")
     elif inp == 1:
          print("-------------Amount to Words Converter-------------")
          am = input("Enter the amount:  ")
          words = toWords(am)
          print("Amount in words is  --- ",words)
     elif inp == 2:
          print("-------------Words to Amount converter-------------")
          words = input("Enter the words:  ")
          am = toAmount(words)
          print("Amount is  --- ",am)
     elif inp == 3:
          print("-------------Binary to Decimal converter-------------")
          inp = input("Enter the binary number:  ")
          out = btd(inp)
          print("Corrsponding decimal number is  --- ",out)
     elif inp == 4:
          print("-------------Decimal to Binary converter-------------")
          inp = input("Enter the decimal number:  ")
          out = dtb(inp)
          print("Corrsponding binary number is  --- ",out)
     elif inp == 5:
          print("-------------Decimal to Hex converter-------------")
          inp = input("Enter the decimal number:  ")
          out = dth(inp)
          print("Corrsponding hexadecimal number is  --- ",out)
     elif inp == 6:
          print("-------------Decimal to Octal converter-------------")
          inp = input("Enter the decimal number:  ")
          out = dto(inp)
          print("Corrsponding octal number is  --- ",out)
     elif inp == 7:
          print("-------------Binary to Hex converter-------------")
          inp = input("Enter the binary number:  ")
          out = bth(inp)
          print("Corrsponding hexadecimal number is  --- ",out)
     elif inp == 8:
          print("-------------Binary to Octal converter-------------")
          inp = input("Enter the binary number:  ")
          out = bto(inp)
          print("Corrsponding octal number is  --- ",out)
     elif inp == 9:
          print("-------------Binary to Text converter-------------")   #INCOMPLETE
          inp = input("Enter the binary number:  ")
          out = btd(inp)
          print("Corrsponding decimal number is  --- ",out)
     elif inp == 10:
          print("-------------Hex to Decimal converter-------------")
          inp = input("Enter the hexadecimal number:  ")
          out = htd(inp)
          print("Corrsponding decimal number is  --- ",out)
     elif inp == 11:
          print("-------------Hex to Binary converter-------------")
          inp = input("Enter the hexadecimal number:  ")
          out = htb(inp)
          print("Corrsponding binary number is  --- ",out)
     elif inp == 12:
          print("-------------Hex to Octal converter-------------")
          inp = input("Enter the hexadecimal number:  ")
          out = hto(inp)
          print("Corrsponding octal number is  --- ",out)
     elif inp == 13:
          print("-------------Octal to Decimal converter-------------")
          inp = input("Enter the octal number:  ")
          out = otd(inp)
          print("Corrsponding decimal number is  --- ",out)
     elif inp == 14:
          print("-------------Octal to Binary converter-------------")
          inp = input("Enter the octal number:  ")
          out = otb(inp)
          print("Corrsponding binary number is  --- ",out)
     else:    #inp == 15
          print("-------------Octal to Hex converter-------------")
          inp = input("Enter the octal number:  ")
          out = oth(inp)
          print("Corrsponding hexadecimal number is  --- ",out)
