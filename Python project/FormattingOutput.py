name="Damini"
age= 25
salary= 50000.50

name,age,sal="damini", 25 ,50000.50

#Approach1
'''
print(name)
print(age)
print(salary)
print(name,age,salary)
'''
#Approach2
print("Name is:",name)
print("Age is:",age)
print("Sal is:",sal)

#opt- Name is: damini
#Age is: 25
#sal is: 50000.5

#Approach3
print ("Name is:%s Age is:%d. Salary is:%g" %(name, age, sal))

#Approach4
print("Name is:f{} Age is:f{} Salary is:{}" .format(name,age,sal))
print("Age is:{} Name is:{} Salary is:{}" .format(age, name, sal))