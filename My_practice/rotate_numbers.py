
# 🔁 7. Rotate List Elements
#
# Question:
# Rotate the list right by 2 places.
# Input: [1,2,3,4,5] → Output: [4,5,1,2,3]

nums=[1,2,3,4,5]
print(nums[3:5]+nums[0:3])