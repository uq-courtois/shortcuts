# Set max of rows to show, in/decrease to needs
pd.set_option('max_rows', 9999)

# CROSSTABULATION
table, results = rp.crosstab(
    df['sfxgenre'], df['productionlocation'], prop='col', test='chi-square')

print(table)  # Prints crosstab
print()
print(results)  # Prints statistics tab
