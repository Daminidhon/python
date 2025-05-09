'''
list1 = ('a','b','c')
list2 = ('d','e','f')
list3 = list1+ list2

print(''.join(list3))
print(list3)
print (list1 +list2)
'''

n = 10
a, b = 0, 1
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b