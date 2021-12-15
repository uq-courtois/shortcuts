for sec_title in soup.find_all('h2'):
	# Print each h2 html element
	print(sec_title)

	# Extract only the text from the h1 html element
	print(sec_title.getText())
