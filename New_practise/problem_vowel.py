

# ⚙️ LEVEL 2: Basic Logic Questions
# Q4. Count Vowels in a String
#
# Logic:Loop through string → check if each character is a vowel.


wordss=input("Enter the Word: ")
vowwels='AEIOUaeiou'
count=0
for i in wordss:
    if i in vowwels:
        count+=1
print(count)