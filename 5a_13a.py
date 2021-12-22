import pandas as pd # import once at the top of your script

# Grabs the fifth, fourth, third, and second last digits from each value of 'year' and saves as new variable 'release_year'
df['year'] = df['release_year'].str[-5:-1]
