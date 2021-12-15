# Subsetting rows with values for popularity higher than 80
# Use a boolean expression to create a rule for subsetting the data
df_pop = df[df['popularity'] > 80]

# new entries are written into the new dataframe df_pop
print(df_pop.info())
