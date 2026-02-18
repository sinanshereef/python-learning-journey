
# Find Top 3 Highest Values in a Dictionary
#
# Input:
# marks = {'John':88, 'Sara':95, 'Bob':72, 'Emma':90}
# Output:
# Sara:95, Emma:90, John:88

marks={'John':88,'Sara':95,'Bob':72,'Emma':90}
new=sorted(marks.items(),key=lambda x:x[1],reverse=True)[:3]
for k,v in new:
    print(k,v,end=",")