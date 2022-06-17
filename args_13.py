def sum(*num):
    sum = 0
    for i in num:
        sum = sum + i
    return sum
print(sum(5,6,7))
print(sum(9,9,8,7,6,5,4,4))
# args with normal parameter
def add(num1,num2,*args):
    sum = 0
    for i in args:
        sum = sum +i
    return sum
print(add(1,2,3,4,5))
# args as arguments
def add(num1,num2,*args):
    sum = 0
    for i in args:
        sum = sum +i
    return sum
num = (1,2,3,4,5,6,7,8,9)
print(add(*num))
def power(num1,*args):
    if len(args)>0:
        return [i**num1 for i in args]
    else:
        return "you didn't pass args"
num = [1,2,3]
print(power(3,*num))


