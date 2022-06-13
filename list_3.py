# List Methods :
#l1=[1,8,4,3,15,20,25,89,65]       #l1 is a list
#print(l1)

"""l1.sort()
print(l1)      #l1 after sorting
l1.reverse()
print(l1)     """ #l1 after reversing all elements
#print(l1[3])
#print(l1[::-1])#for reverse
"""numbers = [2,7,1,3]
numbers.append(9)
numbers.append(27)
numbers.insert(1,29)
print(numbers)
numbers[2]= 87 # list is mutable
print(numbers)"""

"""a= int(input("enter first number: "))
b = int(input("enter second number: "))
temp = a
a= b
b=temp
print(a,b)"""
"""a= int(input("enter first number: "))
b = int(input("enter second number: "))
(a,b) = (b,a)
print(a,b)"""
l1 =[1,2,3,4,5,6]
l1 = max(l1)
print(l1)
input_string = input('Enter elements of a list separated by space ')

user_list = input_string.split()
user_list = max(user_list)

print('list: ', user_list)

