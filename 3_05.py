for atag in soup.find_all('a'):
	link = atag['href']
	linktext = atag.getText()
	print(link,linktext)
