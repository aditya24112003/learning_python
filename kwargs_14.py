"""def total_fruits(**kwargs):
    total = 0
    for amount in kwargs.values():
        total = amount + total
    return total
print(total_fruits(banana=5, mango=7, apple=8))
print(total_fruits(banana=5, mango=7, apple=8 , grapes=230))"""
"""def func(name ,*args, age =20 , **kwargs):
    return name , args , age , kwargs
print(func('aditya',1,2,3,a =2 , b =3))"""
"""def func1(l):
    return [i.capitalize() for i in l]
print(func1(['aditya','gaurav','paritosh']))"""
"""def word_count(l):
    count = {}
    for i in l:
        if i in count:
            count[i]= count[i]+1
        else:
            count[i]=1
    return count
print(word_count(['aditya','gaurav','paritosh','aditya','gaurav','aditya','paritosh']))"""
