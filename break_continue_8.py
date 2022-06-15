"""i = 0
while i<45:
    print(i)
    if i ==22:
        break
    i=i+1"""
"""for i in range(1,101):
    if i%3==0:
        break
    print(i)"""
"""for i in range(1,101):
    if i%3==0:
        continue
    print(i)"""

"""l = ['apple','boy','apple','cricket','dog','cricket','cricket']
word_count = {}

for word in l:
    if word in word_count:
        current_count = word_count[word]
        new_count = current_count + 1
        word_count[word] = new_count
    else:
        word_count[word] = 1

print(word_count)"""
def is_palindrome(a):
    reversed_word = a[::-1]
    if a == reversed_word
        return True
    return False
a = (input("enter name:"))
print(is_palindrome(a))