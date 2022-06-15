"""l = input("enter a name")
letter_count = {}

for letter in l:
    if letter in letter_count:
        current_count = letter_count[word]
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
        print(a,b , end = "")
        for i in range(n-2):
            c = a+b
            a=b
            b=c
            print (b, end = "")
print(fibonacci_sequence(5))"""
"""def user_info(first_name,last_name,age=20):
    print(f"your first name is {first_name}")
    print(f"your last name is {last_name}")
    print(f"your age is {age}")
(user_info("adi","srivastva"))"""
def func():
    x = 7
    return x
print(func())


