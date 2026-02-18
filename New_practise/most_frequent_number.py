# 1️⃣ Find the Most Frequent Number
#
# You have a list of numbers.
# You must find which number is repeated the highest number of times.
#
# Example:
# [4, 5, 2, 5, 3, 2, 5]
# Here:
#
# 5 → appears 3 times
#
# 2 → appears 2 times
#
# 4 and 3 → appear 1 time
#
# So, the answer: 5


lst1=[4,5,2,5,3,2,5]
dic={}
for i in lst1:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for k,v in dic.items():
    print(f'{k} appears {v} times')
max_key = max(dic, key=dic.get)
print(max_key)