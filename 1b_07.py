x = [1,2,'Erik',3]

# Code A
for i in x:
 print(i+1)

# Code B
for i in x:
    try:
        print(i+1)
    except: # Executed when try fails
        pass
