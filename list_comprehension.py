"""negative = []
n = int(input("enter an number:"))
for i in range(1,n+1):
    negative.append(-i)
print(negative)
#2
negative1 = [-i for i in range (1,n+1)]
print(negative1)
#3
square_list = [i**2 for i in range (1,n+1)]
print(square_list)
#4 if and nested if in list comprehension
number_list = [i for i in range(1,n+1) if i%2==0 if i%5==0]
print(number_list)
#5
number_list1 = ["even" if i%2==0 else "odd" for i in range(1,n+1)]
print(number_list1)"""
"""#6
name = ['Aditya','Ashu','Adarsh']
list_1 = []
for i in name:
    list_1.append(i[0])
print(list_1)"""
"""name = ['Aditya','Ashu','Adarsh']
first_letter = [i[0] for i in name ]
print(first_letter)"""
"""l = ['abc','def','ghi']

rev_string = [i[::-1] for i in l]
print(rev_string)"""
"""def rev_string(l):
    return [i[::-1] for i in l]
print(rev_string(l = ['abc','def','ghi']))"""
"""def num_2_string(l):
    return [str(i) for i in l if type(i)==int or type(i) == float ]
print(num_2_string(['aditya',2,3,2.5,'ashu,98']))"""
"""def new_l(l):
    return [-i if i%2!=0 else i*4 for i in l]
print(new_l(range(1,11)))"""
list_2 = [1,2,3]
new_list = [[i for i in range(0,4)] for j in range (0,3) ]
print(new_list)
