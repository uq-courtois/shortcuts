# Narrow down soup to only h1 element html
maintitlehtml = soup.find('h1')
print(maintitlehtml)

# Extract only the text from the h1 html element
maintitle = maintitlehtml.getText()
print(maintitle)
