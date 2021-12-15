name = 'Waldo'

if name == 'Waldo': # Only execute nested code when True
    print('Found',name)

names = 'Lisa and Waldo'

if 'Waldo' in names or 'Wanda' in names: # double condition (or, could also be and/not)
    print('Found',name)
else: # Executed when conditional is False
    print('No one found...')
