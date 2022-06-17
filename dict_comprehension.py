"""#1
dict_square = {f"square of {num} is " : num**2 for num in range (1,11)}
for k ,v in dict_square.items():
    print(f"{k}:{v}")
#2
string = "aditya"
count_i = {i:string.count(i) for i in string}
print(count_i)

#3
list_3 = ['adi','adi','ashu','ashu','zamal','adi']
count_l = {i:list_3.count(i) for i in list_3}
print(count_l)
#4"""
"""def word_counter(l):
    return {i:l.count(i) for i in l}
l = ['adi','adi','ashu','ashu','zamal','adi']
print(word_counter(l))"""
'''def odd_even_fil(l):
    return {i :('even' if i%2==0 else 'odd') for i in l }
n = int(input("enter a number")
l=list (range(1,n+1)))
print(odd_even_fil(l))'''
def word_counter(l):
    word = {}
    for i in l:
        if i in word:
            word[i]= word[i] +1
        else:
            word[i] = 1
    return word
print(word_counter(['adi','adi','ashu','ashu','zamal','adi']))
"""def word_counter(l):
    return {i:l.count(i) for i in l}
print(word_counter(['adi','adi','ashu','ashu','zamal','adi']))"""

square_dict = {num: num*num for num in range(1, 11)}
print(square_dict)


