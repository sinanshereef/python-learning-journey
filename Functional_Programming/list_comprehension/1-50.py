
#1-50 range

#1-15===small
# 16-35==medium
# above 35==large

lst=[(i,'small') if i<=15 else (i,'large') if i>35 else (i,'medium') for i in range(1,50) ]
print(lst)