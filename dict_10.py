"""user_info = {'name':'aditya', "age":20, 'fav_series':'gullak'}
for key , value in user_info.items():
    print(f"key is {key} and value is {value}")"""
"""user_info = {'name':'aditya', "age":20, 'fav_series':'gullak'}
for key  in user_info.items():
    print(f"key is {key} ")"""
# to delete key , value pairs in dictionary
"""user_info = {'name':'aditya', "age":20, 'fav_series':'gullak'}
popped_item = user_info.popitem()
print(popped_item)
print(type(popped_item))
print(user_info)"""
"""user_info = {'name':'aditya', "age":20, 'fav_series':'gullak'}
other_info = {'batch': 2020 , 'year':'2nd'}
user_info.update(other_info)
print(user_info)"""
"""def word_counter(s):
    count = {}
    for i in s:
        count[i] = s.count(i)
    return count
print(word_counter('hello world'))
"""
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( word_count('the quick brown fox jumps over the lazy dog.'))




"""def word_count(s):
    counts = dict()
    words = s.split()
    for word in counts:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( word_count('the quick brown fox jumps over the lazy dog.'))"""



"""def freq_count(l):

    word_count = {}


    for word in l:

        if word in word_count:

            current_count = word_count[word]
            new_count = current_count + 1
            word_count[word] = new_count
        else:
            word_count[word] = 1
    return word_count
print((freq_count(['apple','boy','apple','cricket','dog','cricket','cricket'])))"""
"""user_info = {}
name = input("enter your name :")
age = input("enter your age :")
fav_songs = input("enter your fav songs:").split()
fav_movies = input("enter your fav movies:").split()
user_info["name"] = name
user_info["age"]= age
user_info["fav_songs"]= fav_songs
user_info["fav_movies"]= fav_movies
for key,value in user_info.items():
    print(key,value)"""
def sq_list(l):
    list_1 = []
    for i in l:
        list_1.append(i**2)
    return list_1
print(sq_list([1,2,3,4,5,6]))



