
# Q12. Find Common Elements Between Two Lists
#
# Logic:
# Convert to sets and find intersection.

a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7]
c=set(a)&set(b)
print(list(c))