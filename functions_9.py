"""l = input("enter a name")
letter_count = {}

for letter in l:
    if letter in letter_count:
        current_count = letter_count[letter]
        new_count = current_count + 1
        letter_count[letter] = new_count
    else:
        letter_count[letter] = 1

print(letter_count)"""
"""def last_char(name):
    return name[-1]
print(last_char("adarsh"))"""
"""def odd_even(a):
    if a%2==0:
        return "even"
    else:
        return "odd"
print(odd_even(4))"""
"""def odd_even(a):
    if a%2==0:
        return "even"
    return "odd"
print((odd_even(9)))"""
"""def odd_even(a):
    return a%2==0
print(odd_even(7))
"""
"""def max_min(a,b):
    if a>b:
        return a
    else:
        return b
a= int(input("enter first number:"))
b = int(input("enter second number:"))
print("the greatest number is ",max_min(a,b))"""
"""def great_three(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    return c
a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))
print("the greatest of three numbers is ",great_three(a,b,c))"""
"""def fibonacci_sequence(n):
    a = 0 #first number
    b = 1 #second number
    if n == 1:
        print(a)
    elif n == 2:
        print (b)
    else:
        print(a ,b , end = " ")
        for i in range(n-2):
            c = a+b
            a=b
            b=c
            print (b, end = " ")
print(fibonacci_sequence(5))"""
"""def user_info(first_name,last_name,age=20):
    print(f"your first name is {first_name}")
    print(f"your last name is {last_name}")
    print(f"your age is {age}")
(user_info("adi","srivastva"))"""
"""def func():
    x = 7
    return x
print(func())"""
numbers= [1,2,3,4,5,6,7]
"""def square_list(l):
    square = []
    for i in l:
        square.append(i**2)
    return square
print(square_list(numbers))"""
"""def rev_list(l):
    list=[]
    for i in l:
        list = l[::-1]
    return list
print(rev_list(numbers))"""
"""def rev_list(l):
    l.reverse()
    return l
num = [1,2,3,4,5]
print(rev_list(num))"""
"""def rev_list(l):
    return l[::-1]
num = [1,2,3,4,5,6]
print(rev_list(num))"""
#to reverse the elements of list
"""num = ["apple", "mango", "orange", "banana"]
def rev_list (l):
    r_list = []
    for i in range(len(l)):
        pop_item = l.pop()
        r_list.append(pop_item)
    return r_list
print((rev_list(num)))"""
# to revesre the characters of elements in a list
"""def rev_elements(l):
    rev_list = []
    for i in l:
        rev_list.append(i[::-1])
    return rev_list
num = ["abc","apple", "cba","dbs"]
print(rev_elements(num))
"""
"""def fil_odd_even(l):
    list = []
    odd_nums = []
    even_nums = []
    for i in l:
        if i%2==0:
            even_nums.append(i)
        else:
            odd_nums.append(i)
    return odd_nums , even_nums
num = [1,2,3,4,5,6,7,8,9,10]
print(fil_odd_even(num))"""
# to find common elements between two lists
"""def commmon_elements(l1,l2):
    list_c = []
    for i in l1:
        if i in l2:
            list_c.append(i)
    return list_c
print(commmon_elements([1,2,3,4,5,6], [1,2,3,4,5]))"""
"""def great_diff(l1):
    return max(l1)-min(l1)
print(great_diff( [1,2,3,4,60]))"""
"""def list_counter(l1):
    count = 0
    for i in l1:
        if type(i)== list:
            count=count+1

    return count
print(list_counter( [1,2,[3,4],5,[6,7,8]]))"""
"""user_info = {'name': 'unknown', 'age': 'unknown'}
print(user_info)"""

"""d = {'name': 'unknown', 'age': 'unknown'}
d1 = d
print(d1.pop('name'))
print(d)"""
"""def cube(n):
    cubes= {}
    for i in range(1,n+1):
        cubes[i] = i**3
    return cubes
print(cube(3))
"""
def cubes(n):
    return {i : i**3 for i in range(1,n)}
print(cubes(5))
"""def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial((n-1))
n = int(input("enter a number :"))
print(factorial(n))
"""




