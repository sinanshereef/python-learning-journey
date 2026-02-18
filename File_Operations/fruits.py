

#fruits without apple

f=open('fruits','r')
f1=open('fruit1','w')
for i in f:
    if i!='apple\n':
        f1.write(i)
    else:
        continue
        