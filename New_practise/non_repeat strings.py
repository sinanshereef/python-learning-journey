

# You have a word like "programming".
# Some letters repeat.
# Your task → Print only those letters which appear exactly once.
#
# For "programming":
#
# p, o, a, i, n → These appear only once.

def non_repeat():
    str="programming"
    dic={}
    for i in str:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    new=[k for k,v in dic.items() if v<2]
    print(new)
non_repeat()