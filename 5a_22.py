import pandas as pd # import once at the top of your script
import researchpy as rp # import once at the top of your script

# Set max of rows to show, in/decrease to needs
pd.set_option('max_rows', 9999)

# CROSSTABULATION of categorical variables x and y
table, results = rp.crosstab(
    df['x'], df['y'], prop='col', test='chi-square')

print(table)  # Prints crosstab
print()
print(results)  # Prints statistics tab
