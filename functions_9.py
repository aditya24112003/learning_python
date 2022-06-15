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
def odd_even(a):
    return a%2==0
print(odd_even(7))


