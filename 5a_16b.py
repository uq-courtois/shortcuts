import pandas as pd # import once at the top of your script

x = df.groupby(['y'], as_index=False)[['z']].max()
# x is a new dataframe with the maximum value of z per unique value of y
