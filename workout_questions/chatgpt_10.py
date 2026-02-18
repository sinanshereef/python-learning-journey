

# 1
# 23
# 456
# 78910

count=1 #2
for i in range(4):  #0 #1
    for j in range(i+1): #0+1=1 #2
        print(count,end=' ')
        count+=1
    print()
