from New_practise.list_second_larg import second_largest
from New_practise.sec_lar import largest

# 📅 4. Find the Second Largest Element
#
# Question:
# Find the second largest number in a list.
#
# Example:
# Input: [10, 20, 4, 45, 99]
# Output: 45


lst=[10,20,4,45,99]
lst.sort(reverse=True)
largest_element=lst[0]
lst.remove(largest_element)
second=lst[0]
print(second)


