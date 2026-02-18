from New_practise.list_second_larg import second_largest

# Q8. Find Second Largest Number in a List
#
# Logic:
# Sort the list or use logic to track largest and second largest.

lst=[10, 40, 30, 20, 40, 50]
largest=max(lst)
lst.remove(largest)
second_larg=max(lst)
print(second_larg)