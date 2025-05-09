'''
num1=input("Enter first Number:")
num2=input("Enter second Number:")

print(type(num1)) #str
print(type(num2))  #str

print(num1+num2) #opt is 1020 bec it a string type of veriable
'''
#Approach 1
'''
num1=int(input("Enter first Number:"))
num2=int(input("Enter second Number:"))

print(type(num1))  #int
print(type(num2))  #int

print(num1+num2)  #opt = 30 (10+20) int type of veriable
                  # Enter first Number10
                  #Enter second Number20
                  #<class 'int'>
                  #<class 'int'>
                  #30
'''
#Approach 2
'''
num1=input("Enter first Number:")
num2=input("Enter second Number:")

print(int(num1)+int(num2))  #opt 30  #int
'''
#example
num1=input("Enter first decimal Number:")
num2=input("Enter second decimal Number:")

print(type(num1)) #str
print(type(num2))  #str

print(float(num1)+float(num2))  #opt 8.7

