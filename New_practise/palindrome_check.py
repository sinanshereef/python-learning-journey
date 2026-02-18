# Q9. Check Palindrome String
# #
# # Logic:
# # String is palindrome if reversed string is same as original.


new_string=input("Enter the String: ")
rev=new_string[::-1]
if new_string==rev:
    print(f"{new_string} is a Palindrome")
else:
    print(f"{new_string} is not a palindrome")