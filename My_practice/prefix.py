
# Given a list of strings, find the longest common prefix shared by all strings.

# If there’s no common prefix, return an empty string "".
#
# 📘 Example 1
#
# Input:
#
# words = ["flower", "flow", "flight"]


# Output:
#
# "fl"
#
# 📘 Example 2
#
# Input:
#
# words = ["dog", "racecar", "car"]
#
#
# Output:
#
# ""
#
#
# (No common prefix)

# words = ["flower", "flow", "flight"]
# words.sort()
# fst_wrd = words[0]
# lst_wrd = words[-1]
# i = 0
# while i < len(fst_wrd) and i < len(lst_wrd) and fst_wrd[i] == lst_wrd[i]:
#     i += 1
# results = fst_wrd[:i]
# print(results)


# word="a3b2c1"
# lst_1=list(word)
# word_lst=[]
# num_lst=[]
# for i in range(len(lst_1)):
#     if i%2==0:
#         word_lst.append(lst_1[i])
#     else:
#         num_lst.append(lst_1[i])
# print(word_lst[0],'appears',num_lst[0],'times')
# print(word_lst[1],'appears',num_lst[1],'times')
# print(word_lst[2],'appears',num_lst[2],'times')

# lst = [1,1,2,2,3,3,3,2]
# lst1 = []
# for i in lst:
#     if i not in lst1 or lst1[-1] != i:
#         lst1.append(i)
# print(lst1)

# words = ["flower", "flow", "flight"]
# words.sort()
# fst_wrd = words[0]
# lst_wrd = words[-1]
# i = 0
# while i < len(fst_wrd) and i < len(lst_wrd) and fst_wrd[i] == lst_wrd[i]:
#     i += 1
# results = fst_wrd[:i]
# print(results)


# word=["flower","flow","flight"]
# prefix=word[0] #flower
# for i in word[1:]: #flow,flight
#     while not i.startswith(prefix):
#         prefix=prefix[:-1]
# print(prefix)


word="banana"
word=word.replace("a","o")
print(word)