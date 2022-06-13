"""var1 = 6
var2 = 56
var3 = int(input())
if var3>var2:
    print("Greater")
elif var3==var2:
    print("Equal")
else:
    print("Lesser")

list1 = [5, 7, 3]18

print(15 in list1)
if 15 not in list1:
    print("No its not in the list")"""


"""n = int(input("enter your age : "))
if n<18:
    print("you are underage , hence you cannot drive")
elif n==18:
    print("come and give a test and we will think about it")
else :
    print("you can drive")"""



print("input first number")
a = int(input())
print("input second number")
b = int(input())
print("enter operator")
opr = input()

if a == 3 and b == 4 and opr == "+":
    print("10") #wrong asnwer
elif a == 5 and b == 6 and opr == "/":
    print("20") #wring answer
elif a == 5 and b == 6 and opr == "*":
    print("25") #wrong asnwer
elif opr == "*":
    print("the answer is", a * b)
elif opr == "/":
    print("the answer is", a/b)
elif opr == "-":
    print("the asnwer is ", a-b)
elif opr == "+":
    print("the answer is ", a+b)

