#conditional statement
# if  id..else   elif

#print a person is eligible for a vote or not





#Example 1
a=30
if a>20:
    print("true condition")
else:
    print("condition is false")

#Example2
if False:
    print("true condition")
else:
    print("condition is False")

#example3
if 0:
    print("true condition")
else:
    print("condition is False")

#example4
if 1:
    print("true condition")
else:
    print("condition is False")

#even or odd
a=20
if a%2==0:
    print("number is even")
else:
    print("Number is odd")

 #example
a=15
if a%2==0:
    print("number is even")
else:
    print("Number is odd")

#multiple statements under if else block
if True:
     print("Statement1")
     print("Statement2")
     print("Statement3")
else:
     print("Statement4")
     print("Statement5")
print("this ont a part of if and else blocks")

#single statement in single line
print("welcome") if True else print("python")
print("welcome") if False else print("python")
print("welcome") if 10<20 else print("out")
print("welcome") if 10>20 else print("out")

#multiple statements in single line
{print("welcome1"),print("python1")} if True else{print("welcome2"),print("python2")}
{print("welcome1"),print("python1")} if False else{print("welcome2"),print("python2")}

#elif command in python

a=100
if a==10:
    print("Ten")
elif a==20:
    print("Twenty")
elif a==30:
    print("Thirty")
else :    #optinal
    print("Not listed number")