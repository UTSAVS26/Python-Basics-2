print("The Menu Driven Program for the following:-")
print(
"""1. Amount to Words Converter
2. Words to Amounts Converter
3. Binary to Decimal Converter 
4. Binary to Octal Converter 
5. Binary to Hex Converter 
6. Binary to Text Converter
7.Decimal to Binary Converter 
8. Decimal to Octal Converter 
9. Decimal to Hex Converter
10. Octal to Binary Converter 
11. Octal to Decimal Converter 
12. Octal to Hex Converter 
13. Hex to Binary Converter 
14. Hex to Decimal Converter 
15. Hex to Octal Converter
16. EXIT""")
x=int(input("Enter any Number in the Range 1-16: "))






# NUMBER TO WORDS IN PYTHON (INDIAN SYSTEM)
if x==1:
     print("\nWELCOME TO NUMBER TO WORDS CONVERTER IN INDIAN SYSTEM")
     def Words(n):
          units = ["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"] 
          teens = ["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen",
                       "Seventeen","Eighteen","Nineteen"] 
          tens = ["Twenty","Thirty","Fourty","Fifty","Sixty","Seventy","Eighty","Ninety"] 
          if n <=9:
               return units[n] 
          elif n >= 10 and n <= 19:
               return teens[n-10] 
          elif n >= 20 and n <= 99:
               return tens[(n//10)-2] + " " + (units[n % 10] if n % 10 !=0 else "") 
          elif n >= 100 and n <= 999:
               return Words(n//100) + " Hundred " + (Words(n % 100) if n % 100 !=0 else "") 
          elif n >= 1000 and n <= 99999:
               return Words(n//1000) + " Thousand " + (Words(n % 1000) if n % 1000 !=0 else "") 
          elif n >= 100000 and n <= 9999999:
               return Words(n//100000) + " Lakh " + (Words(n % 100000) if n % 100000 !=0 else "") 
          elif n >= 10000000:
               return Words(n//10000000) + " Crore " + (Words(n % 10000000) if n % 10000000 !=0 else "")
     n=int(input("Enter Number to be Converted in Words: "))
     print("The Equivalent Word of %d is: "%n, Words(n))
     print("***********************************************")


# WORDS TO NUMBER IN PYTHON
if x==2:
     print("\nWELCOME TO WORDS TO NUMBER CONVERTER")
     def toAmount(words):
          words = words.title()
          words = words.strip()   #So that words can be obtained from dictionary
          d_am = {'Zero': '0', 'One': '1', 'Two': '2', 'Three': '3', 'Four': '4', 'Five': '5',
                  'Six': '6', 'Seven': '7', 'Eight': '8','Nine': '9'}
          l = words.split()    #to make a list of words
          st = ''
          for word in l:
               i = d_am.get(word)
               if i == None:   #word not in dictionary
                    print("Please check for mistypes")
                    st += ' - '
               else:
                    st += i
          return st.strip()
     n=input("Enter Word to be Converted in Numbers: ")
     print("The Equivalent Number is: ", toAmount(n))
     print("***********************************************")


#BINARY TO DECIMAL CONVERTER
if x==3:
     print("Welcome to Binary to Decimal Converter.")
     num=int(input("Enter a binary number: "))
     def BintoDec(n):
          s,t=0,0
          while n>0:
               d=n%10
               s+=(d*(2**t))
               t+=1
               n//=10
          return s
     print("The Decimal Equivalent of %d is: "%num,BintoDec(num))



#BINARY TO OCTAL CONVERTER
if x==4:
     d_oct = {"000":"0","001":"1","010":"2","011":"3","100":"4",
              "101":"5","110":"6","111":"7"}
     print("Welcome to Binary to Octal Converter.")
     num=int(input("Enter a binary number: "))
     def BintoOct(binary):
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
     print("The Octal Equivalent of %d is: "%num,BintoOct(num))


#BINARY TO HEXADECIMAL CONVERTER.
if x==5:
     d_hex = {'0000':'0','0001':'1','0010':'2','0011':'3','0100':'4','0101':'5','0110':'6','0111':'7',
                   '1000':'8','1001':'9','1010':'A','1011':'B','1100':'C','1101':'D','1110':'E','1111':'F'}
     print("Welcome to Binary to Hexadecimal Converter.")
     num=int(input("Enter a binary number: "))
     def BintoHex(binary):
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
     print("The Hexadecimal Equivalent of %d is: "%num,BintoHex(num))


#BINARY TO WORDS CONVERTER.
if x==6:
     print("Welcome to Binary to Words Converter")
     a_binary_string = input("Enter a binary number: ")
     binary_values = a_binary_string.split()
     ascii_string = ""
     for binary_value in binary_values:
          an_integer = int(binary_value, 2)
          ascii_character = chr(an_integer)
          ascii_string += ascii_character
     print("The Equivalent Binary Word is: ",ascii_string)


#DECIMAL TO BINARY CONVERTER.
if x==7:
     print("Welcome to Decimal to Binary Converter ")
     n=int(input("Enter a decimal number: "))
     a=[]
     while(n>0):
          dig=n%2
          a.append(dig)
          n=n//2
     a.reverse()
     for i in a:
          print(i,end="")


#DECIMAL TO OCTAL CONVERTER.
if x==8:
     print("Welcome to Decimal to Octal Converter ")
     n=int(input("Enter a decimal number: "))
     a=[]
     while(n>0):
          dig=n%8
          a.append(dig)
          n=n//8
     a.reverse()
     for i in a:
          print(i,end="")


#DECIMAL TO HEXADECIMAL CONVERTER.
if x==9:
     print("Welcome to Decimal to Hexadecimal Converter ")
     n=int(input("Enter the decimal value: "))
     bs=' '
     while n!=0:
           r=n%16
           if int(r)==10:
                bs+='A'
           elif int(r)==11:
                bs+='B'
           elif int(r)==12:
                bs+='C'
           elif int(r)==13:
                bs+='D'
           elif int(r)==14:
                bs+='E'
           elif int(r)==15:
                bs+='F'
           else:
                bs+=str(r)
           n//=16
     for i in range(len(bs)-1,-1,-1):
           print(bs[i],end='')


#OCTAL TO BINARY CONVERTER.
if x==10:
     print("Welcome to Octal to Binary Converter")
     def OctToBin(octnum):
           binary=""
           while octnum != 0:
                d = int(octnum % 10)
                if d == 0:
                     binary = "".join(["000", binary])
                elif d == 1: 
                     binary = "".join(["001", binary]) 
                elif d == 2:
                     binary = "".join(["010", binary]) 
                elif d == 3:
                     binary = "".join(["011", binary]) 
                elif d == 4:
                     binary = "".join(["100", binary]) 
                elif d == 5: 
                     binary = "".join(["101", binary]) 
                elif d == 6: 
                     binary = "".join(["110",binary]) 
                elif d == 7: 
                     binary = "".join(["111", binary]) 
                else: 
                     binary = "Invalid Octal Digit"
                     break
                octnum = int(octnum / 10)
           return binary 
     octnum = int(input("Enter a Octal Value: "))
     final_bin = "" + OctToBin(octnum)
     print(octnum,":", final_bin)


#OCTAL TO DECIMAL CONVERTER
if x==11:
     print("Welcome to Octal to Decimal Converter")
     n=int(input("Enter a octal number: "))
     s,t=0,0
     while n>0:
          d=n%10
          s+=(d*(8**t))
          t+=1
          n//=10
     print(s)


#OCTAL TO HEXADECIMAL CONVERTER.
if x==12:
     print("Welcome to Octal to Hex Converter")
     i=0
     octal=int(input("Enter Octal number:"))
     Hex=['0']*50
     decimal = 0
     sem = 0
     while octal!=0:
          decimal=decimal+(octal%10)*pow(8,sem)
          sem+=1
          octal=octal// 10
     while decimal!=0:
          rem=decimal%16
          if rem<10:
               Hex[i]=chr(rem+48)
               i+=1
          else:
               Hex[i]=chr(rem+55)
               i+=1
          decimal//=16
     print("Hexadecimal number is: ",end="")
     for j in range(i-1,-1,-1):
          print(Hex[j],end="")


#HEXADECIMAL TO BINARY CONVERTER.
if x==13:
     print("WELCOME TO HEXADECIMALTO BINARY CONVERTER.")
     d_hex = {'0000':'0','0001':'1','0010':'2','0011':'3','0100':'4','0101':'5',
              '0110':'6','0111':'7','1000':'8','1001':'9','1010':'A','1011':'B',
              '1100':'C','1101':'D','1110':'E','1111':'F'}
     d_hex_rev = {}    #keys and values of d_hex are inverted
     for x,y in d_hex.items():
          d_hex_rev[y] = x
     def htb(hexa):
          hexa = str(hexa)
          final = ''
          for dig in hexa:
               i = d_hex_rev.get(dig)    #simply substitute each hexa with corresponding binary
               final += i
          return final
     inp = input("Enter the hexadecimal number:  ")
     out = htb(inp)
     print("Corrsponding binary number is:  ",out)


#HEXADECIMAL TO DECIMAL CONVERTER.
if x==14:
     print("Welcome to Hex to Decimal Converter")
     def hexadecimalToDecimal(hexnum):
          length = len(hexnum)
          base = 1
          dec_val = 0
          for i in range(length - 1, -1, -1):
               if hexnum[i] >= '0' and hexnum[i] <= '9':
                    dec_val += (ord(hexnum[i]) - 48) * base
                    base = base * 16
               elif hexnum[i] >= 'A' and hexnum[i] <= 'F':
                    dec_val += (ord(hexnum[i]) - 55) * base
                    base = base * 16
          return dec_val 
     if __name__ == '__main__':
          hexnum = input("Enter a Hexadecimal Value: ")
          print(hexnum,":",hexadecimalToDecimal(hexnum))

     
#HEXADECIMAL TO OCTAL CONVERTER.
if x==15:
     print("Welcome to Hex to Octal Converter")
     import math
     hex = input("Enter a Hexadecimal Value: ")
     oct = ""
     dec = i = 0
     c = len(hex) - 1
     while i < len(hex):
          d = hex[i]
          if d == '0' or d == '1' or d == '2' or d == '3' or d == '4' or d == '5':
               dec = dec + int(d) * int(math.pow(16, c))
          elif d == '6' or d == '7' or d == '8' or d == '9':
               dec = dec + int(d) * int(math.pow(16, c))
          elif (d == 'A') or (d == 'a'):
               dec = dec + 10 * int(math.pow(16, c))
          elif (d == 'B') or (d == 'b'):
               dec = dec + 11 * int(math.pow(16, c))
          elif (d == 'C') or (d == 'c'):
               dec = dec + 12 * int(math.pow(16, c))
          elif (d == 'D') or (d == 'd'):
               dec = dec + 13 * int(math.pow(16, c))
          elif (d == 'E') or (d == 'e'):
               dec = dec + 14 * int(math.pow(16, c))
          elif (d == 'F') or (d == 'f'):
               dec = dec + 15 * int(math.pow(16, c))
          else:
               print("INVALID INPUT")
               break
          i+= 1
          c -= 1
     while (dec > 0):
          oct = "".join([str(int(dec % 8)) , oct])
          dec = int(dec / 8)
     print(hex,":",oct)


#EXIT A PROGRAM.
if x==16:
     print("EXITING THE PROGRAM")
     import sys
     sys.exit()
