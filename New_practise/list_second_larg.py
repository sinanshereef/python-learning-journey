

fruits = ['apple', 'orange', 'pineapple', 'grapes', 'banana']
max_word=max(fruits,key=len)
fruits.remove(max_word)
second_largest=max(fruits,key=len)
print(second_largest)

