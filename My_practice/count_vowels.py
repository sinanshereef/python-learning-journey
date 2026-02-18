
# 💬 9. Count Vowels in a String
#
# Question:
# Count how many vowels are in "Hello World".
#
# Logic:
# Iterate over each character and check if it’s in 'aeiou'.


words="Hello World"
vowels='AEIOUaeiou'
count=0
for i in words:
    if i in vowels:
        count+=1

print('vowels_count=',count)