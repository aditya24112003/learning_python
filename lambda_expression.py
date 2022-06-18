def add(a,b):
    return a+b
print(add(2,3))
add1 = lambda a,b:a+b
print(add1 (1,2))
multiply = lambda a,b:a*b
print(multiply(2,3))
def is_even(a):
    return a%2== 0
print(is_even(6))
is_eve = lambda a:a%2==0
print(is_eve(8))
def last_ch(a):
    return a[-1]
print(last_ch("aditya srivastava"))
last_char = lambda a:a[-1]
print(last_char("adarsh"))
"""len_s = lambda s:True if len(s)>5 else False
print(len_s("aditya"))"""
len_s = lambda s:len(s)>5
print(len_s("aditya"))