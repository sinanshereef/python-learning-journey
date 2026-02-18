
# Remove consecutive duplicates
# Convert [1,1,2,2,3,3,3,2] into [1,2,3,2].

# lst=[1,1,2,2,3,3,3,2]
# lst1=set(lst)
# print(list(lst1))

word = ["flower", "flow", "flight"]
prefix = word[0]            # flower
for i in word[1:]:          # flow, flight
    while not i.startswith(prefix):
        prefix = prefix[:-1]
print(prefix)