"""sets_5 = {k**2 for k in range(1,11)}
print(sets_5)"""
"""names = ["aditya","gaurav","paritosh"]
sets_5 = {name[0] for name in names}
print((sets_5))"""

d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d3 = d1.copy()
d3.update(d2)
print(d3)