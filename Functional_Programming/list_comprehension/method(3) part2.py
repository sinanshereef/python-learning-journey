

# if even=print"even" else 'odd'

lst=[(i,'Even') if i%2==0 else (i,'odd') for i in range(1,21)]
print(lst)