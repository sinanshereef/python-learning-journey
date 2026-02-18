
# 🔄 6. Sort Dictionary by Values (Descending Order)
#
# Input: {'A':10, 'B':5, 'C':20}
# Output: [('C',20), ('A',10), ('B',5)]

inp={'A':10,'B':5,'C':20}
new=sorted(inp.items(),key=lambda x:x[1],reverse=True)
print(new)
