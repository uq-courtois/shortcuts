import pandas as pd # import once at the top of your script

# DF before
print('\nBefore', df)

def age_cal(date_of_birth):
    age = 2022 - date_of_birth
    return age

df['age'] = df['date_of_birth'].apply(lambda x: age_cal(x))

# The result
print('\nAfter', df)
