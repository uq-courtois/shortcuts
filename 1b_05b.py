#### LIST
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

	# We can narrow down the dictionary to a value by adding a key:
for i in x: 
	print(i['Name'])

# STRING
# Iterator value = character in string
x = 'Word'

for i in x:
	print(i)

# ...
