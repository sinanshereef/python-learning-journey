
# 🔠 4. Check if a String is a Palindrome (Ignoring Spaces & Case)
# #
# # Question:
# # Input: "A man a plan a canal Panama" → Output: True

inp="A man a plan a canal Panama"
new=''.join(inp.lower().split())
new1=new[::-1]
if new==new1:
    print(True)
else:
    print(False)


