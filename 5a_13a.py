# Grabs the fifth, fourth, third, and second last digits and saves as new variable
df['year'] = df['release_year'].str[-5:-1]
