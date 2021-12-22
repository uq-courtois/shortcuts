import pandas as pd # import once at the top of your script

# Replaces 'substring' in x with ''
df['x'] = df['x'].str.replace('substring', '')

# Keeps two last characters of the string values in x
df['x'] = df['x'].str[-2:]
