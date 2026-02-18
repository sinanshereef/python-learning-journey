
#Simple Logic..............


lst=[1,3,5,4,3,5,6,7,8,9,7,5,4,6,9,10,12,10,9,8,5,8,9,10]

#Output should be= new_list=[1,5,3,9,4,12,5]
new_lst=[]
directions=0
for i in range(0,len(lst)):
    if lst[i]>lst[i-1]:
        new_dir=1
    elif lst[i]<lst[i-1]:
        new_dir=-1
    else:
        new_dir=directions

    if directions != 0 and new_dir != directions:
        new_lst.append(lst[i - 1])
    directions=new_dir

print(new_lst)
