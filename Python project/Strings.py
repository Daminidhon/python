
#create string veriable
'''
s='welcome'
s=("welcome")
s=str("welcome")
s=str('welcome')

#creating empty string veriable
name=""
name=''
name=str()

#1.Mutable- can not change the value of Variable
#2.Immutalbe- can change the value of the Veriable
         #so the String is Immutable

str1="welcome"
print(id(str1))#4378285696  valude is changing

str1=str1+"to python"
print(id(str1)) # 4378487856  value ids changing

#if the value is changed after updation then is is Immutable
'''

#example 3 : + and * with string
# str="welcome"
# print(str+"programming")
# print(str*3) #welcomewelcomewelcome
# concatenation/joining

#Example4 : slicing
# startign index o
# ending index 1
'''
str="welcome"
print(str[1:3]) #el
print(str[:6])    #welcom here starting index is O by default
print(str [2:])   #lcome
print(str[1:-1])     #elcom last 1 char removed
print(str [1: -2])   #elco last 2 chars removed
'''
#example:5   ord() and chr()
'''
print(ord('A'))  # Returns the ASCII code of the character
print(chr(65)) #returns character represented by a ASCII Number

#example 6 max(), min(), len()

print(max("abc"))    #c
print(min("abc"))   #a
print(len("welcome"))  #7

#example 7 in, not in operators - returns -true/false
s="welcome"
print("come"in s)
print("lome"in s)
'''
'''
#Example 8: String comparison

print("tim" == "tie")          #False
print("free" != "freedom")     #True
print ("arrow" > "aron")       #True
print ("right" >= "left")      #True
print ("teeth" < "tee")        #False
print ("yellow" <= "fellow")   #False
print ("abc" > "")             #True
'''
'''
# Example9 : Testing strings True/False
s= "welcome to python"
print(s.isalnum())                    #False
print ("Welcome". isalpha())          #True
print("2012".isdigit())                #True
print("first Number".isidentifier())  #False
print(s.islower())                    #True
print ("WELCOME".isupper())           #True
print(" ".isspace())                  #True
'''
'''
#Example10 : Searching for Substrings
s= "welcome to python"
print(s.endswith("thort"))         #True
print(s.startswith("good"))       #False
print(s.find("come"))             #3
print(s.find("become"))           #-1 not found
print(s.count("t"))               #2  Returns number of occurrences of substituting the string (how many time t repeted )
'''


