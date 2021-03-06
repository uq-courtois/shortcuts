import pandas as pd # import once at the top of your script

# Loop through all columns and show number of unique values:
for c in df.columns.values.tolist():
    print('\n', len(df[c]), 'unique values in variable:', c)

# Get unique values for one particular variable
# You just need to replace the column name in the ''
print(df['recommended_artist'].unique())
