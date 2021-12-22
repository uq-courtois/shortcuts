import pandas as pd # import once at the top of your script

x = df.groupby(['y'], as_index=False)[['z']].min()
# x is a new dataframe with the minimum value of z per unique value of y
