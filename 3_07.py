for d in soup.find_all('div',class_='location'):
  title = d.find('h2').getText()
  text = d.find('p').getText()
  print(title,'-',text)
