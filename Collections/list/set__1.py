

st={10,30,50,70,90}

# sum
# max
# min
# len

print(sum(st))
print(max(st))
print(min(st))
print(len(st))

# add() is used to add an element in the Set

st.add(75)
print(st)

# update() is used to add Multiple elements in the Set

st.update([100,200,300])
print(st)
print(sum(st))
st.remove(100)
print(st)

#Discard()...which is samew like Remove() but does not returns any errors

st.discard(30)
print(st)