from New_practise.sec_lar import second_larg

# Q13. Print Names with Second Highest Marks
#
# Logic:
#
# Find all marks
#
# Find second largest mark
#
# Print all names with that mark.

students = [["Alice", 80], ["Bob", 90], ["Charlie", 85], ["David", 90]]

mark=[score for name,score in students]  #[80, 90, 85, 90]
new_mark=list(set(mark)) #[80, 90, 85]
new_mark.sort(reverse=True)
second_lar=new_mark[1]

namee=[name for name,score in students if score==second_lar]

print(f"name:{namee}")
print(f"second_largest:{second_lar}")
