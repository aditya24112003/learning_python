d = {"aditya": 20}
print(d)
a = {'key' :'value', 'cow' :'mooh'}
print(a['cow'])
# Dictionary is nothing but key value pairs
d1 = {}
# print(type(d1))
d2 = {"Aditya":"Burger",
      "Rohan":"Fish",
      "SkillF":"Roti",
      "Shubham":{"B":"maggie", "L":"roti", "D":"Chicken"}}
print(d2)

print(d2["Shubham"])
d3 = d2.copy()
del d3["Aditya"]
d2.update({"Leena":"Toffee"})
print(d2.keys())
print(d2.items())


d4 = {"Mutable": "Can change", "Imuatable": "Cannot change",
      "Thesis" : "Theory", "Fear":"Terror"}
print("Enter your word")
key = input()
print(d4[key])
