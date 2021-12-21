### LIST
# Iterator value = element in list
x = [1,2,3,4]

for i in x:
	print(i)

### LIST OF DICTIONARIES
# Iterator value = element in list = dictionary

x = [
	{'Name':'Jamie','Age':19},
	{'Name':'Ella','Age':21},
]

for i in x:
	print(i)

	# We can access all values of a key:
for i in x: 
	print(i['Name'])

### DICTIONARY
# Iterator value = dictonary key
x = {'Name':'Jamie','Age':19}

for i in x:
	print(i)
	
	# We can loop through each key-value pair:
for i in x:
	print(i,x[i])

### STRING
# Iterator value = character in string
x = 'This is a sentence'

for i in x:
	print(i)

# ...
