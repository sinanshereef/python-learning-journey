

# 4️⃣ Find All Pairs With a Given Sum
#
# You have numbers and a target total.
# Find all pairs of numbers that add up to that total.
#
# Example:
# List: [2, 4, 3, 5, 7, 8, -1], target = 7
# Pairs:
#
# 2 + 5 = 7
#
# 4 + 3 = 7
#
# 8 + (-1) = 7


lst=[2,4,3,5,7,8,-1]
target=7
for i in range (len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i]+lst[j]==target:
            print(lst[i],lst[j])