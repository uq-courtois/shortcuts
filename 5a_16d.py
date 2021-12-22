import pandas as pd # import once at the top of your script

x = df.groupby(['y'], as_index=False)[['z']].std()
# x is a new dataframe with the standard deviation of the observations in z for every unique value of y
