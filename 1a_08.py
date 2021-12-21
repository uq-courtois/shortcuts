x = {1,2,3}
y = [1,1,2,2,3,3] # y is a list

print(type(x))

y = set(y) # convert list into a set
print(y)

y = list(y) # convert set back into a list
print(y)

# Or shorter (all in once):
y = list(set(x))
print(y)
