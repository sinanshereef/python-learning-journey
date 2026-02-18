from unittest import expectedFailure

# 🧮 6. Find Missing Number in a Sequence
# #
# # Question:
# # Find the missing number in [1, 2, 3, 5, 6].
# #
# # Logic:
# # Use the formula n*(n+1)/2.

num=[1,2,3,5,6,7,8]
n=num[-1]
actual_sum=sum(num)
expected_sum=n*(n+1)/2
missing_number=expected_sum-actual_sum
print(int(missing_number))