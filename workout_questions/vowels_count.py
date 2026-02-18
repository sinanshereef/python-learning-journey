

words=input("Enter the word: ")
vowels='AEIOUaeiou'
count=0
for i in words:
    if i in vowels:
        count+=1
    else:
        pass
print(count)
