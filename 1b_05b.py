# A list 
# Iterator value = element in list
x = [1,2,3,4]

for i in x:
	print(i)

# A list of dictionaries
# Iterator value = element in list = dictionary

x = [
	{'Name':'Jamie','Age':19},
	{'Name':'Ella','Age':21},
]

for i in x:
	print(i)
	
	# We can access a value by adding a key:
	print(i['Name'])

# A dictionary
# Iterator value = dictonary key
x = {'Name':'Jamie','Age':19}

for i in x:
	print(i)
	
	#We can even access each value:
	print(x[i])

# A string
# Iterator value = character in string
x = 'This is a sentence'

for i in x:
	print(i)

# ...
