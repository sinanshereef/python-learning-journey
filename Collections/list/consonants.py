

#Count of Consonants......

string='luminartechnolab'
vowels='aeiouAEOU'
lst=[]
for i in string:
    if i not in  vowels:
        lst.append(i)
print(lst)
print(len(lst))
