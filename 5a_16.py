x = df.groupby(['name'], as_index=False)[['expenditure']].sum()
# x is a new dataframe with summed values for variable 'expenditure' per unique value in variable 'name'
