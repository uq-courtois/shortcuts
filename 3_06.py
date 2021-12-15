# Find and loop through all the img elements
for i in soup.find_all('img',class_='decoration'):

	# Get the img url from the img source attribute
	imgurl = i['src']
	print(imgurl)

	# Isolate file name, using the text right after the last / in the url
	filename = imgurl.split('/')[-1]

	# Create a new, empty picture file in project
	imgfile = open(filename,'wb')

	# Write picture information into empty file
	imgfile.write(urlopen(imgurl).read())

	# Close file
	imgfile.close() 
