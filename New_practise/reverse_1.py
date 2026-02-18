
# A sentence has many words.
# You must reverse each word, but keep the word positions the same.
#
# Example:
# Input: "hello world"
# Words: "hello" and "world"
# Reverse them → "olleh dlrow"
# But "olleh" should still come before "dlrow".

inp="hello world"
new=inp.split()
for i in new:
    print(i[::-1],end=' ')