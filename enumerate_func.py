"""names = [ 'adi','ashu','gaurav','paritosh']
for position,name in enumerate(names):
    print ( position , name)"""
"""food = ['bread','eggs','rice']
print(list(enumerate(food)))"""
"""ist = [10,20,30,40,50]
print(dir(ist))
print(iter(ist))"""
from functools import reduce
def getsum(x,y):
    return x+y
def getprod(x,y):
    return x*y

Ist = [1,2,3,4,5]
s = reduce(getsum, Ist)
p = reduce(getprod, Ist)
print(s)
print(p)