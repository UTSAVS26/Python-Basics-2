# Function to Replace each vowel in the string with a specified character 
def replaceVowelsWithK(test_str, K):
     vowels = 'AEIOUaeiou'
     for ele in vowels:
          test_str = test_str.replace(ele, K)
     return test_str 
str11= input("Enter a String: ") 
K= input("Enter a Character: ")
print("Given String:", str11) 
print("Given Specified Character:", K)  
print("After replacing vowels with the specified character:", replaceVowelsWithK(str11, K))
