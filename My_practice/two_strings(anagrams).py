

# 🔄 5. Check if Two Strings Are Anagrams
#
# Question:
# Two strings are anagrams if they contain the same letters in any order.
#
# Example:
# Input: "listen", "silent" → Output: True

word_1=input('Enter the 1st Word: ')
word_2=input('Enter the 2nd Word: ')
new_word1=list(word_1)
new_word1.sort()
new_word2=list(word_2)
new_word2.sort()
if new_word2==new_word1:
    print(True)
else:
    print(False)