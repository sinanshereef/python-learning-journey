from os.path import split

# Question 12: Simple Linear Search
#
# Difficulty: Medium
# Problem: Write a function that searches for an element in a list and returns its index or -1 if not found.
# Input: list = [10, 20, 30], target = 20
# Output: 1

inp=input("Enter the Elements that is to be added: ")
string_lst=inp.split()
lst1=list(map(int,string_lst))
target=int(input("Enter the value to be searched: "))
for i in lst1:
    if i==target:
        print("Found")
        break
else:
    print("not Found")
