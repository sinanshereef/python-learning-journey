

# 8. Write a program to find the word that occurs the most in a sentence.
# Example: "this is a test and the test" → 'test' appears twice.

word="this is a test and the test"
word2=word.split()
dic={}
for i in word2:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
max_val=max(dic,key=dic.get)
print(max_val,'appears twice')