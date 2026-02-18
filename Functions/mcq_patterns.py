
# def patterns():
# #     i=int(input("Enter the Range: "))
# #     for i in range(1,5):
# #         for j in range(1,i+1):
# #             print(j,end=" ")
# #         print()
# # patterns()


# def patterns():
#     i=int(input("Enter the Range: "))
#     for i in reversed(range(4)):
#         for j in range(i+1):
#             print("*",end=" ")
#         print()
#
# patterns()


def diamond(mid):
    # Upper half: 1 .. mid
    for i in range(1, mid + 1):
        spaces = mid - i
        print(" " * spaces + ("* " * i).rstrip())

    # Lower half: mid-1 .. 1
    for i in range(mid - 1, 0, -1):
        spaces = mid - i
        print(" " * spaces + ("* " * i).rstrip())

# Example
diamond(3)   # prints the pattern in the image
