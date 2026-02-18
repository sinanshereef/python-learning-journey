

str='In 1984 there was a 13 instance of protest with over 1000 people'
data=str.split(' ')
lst=[i for i in data if not i.isalpha()]
print(lst)