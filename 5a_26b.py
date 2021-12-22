import pandas as pd # import once at the top of your script

df1 = pd.read_csv('file1.csv',sep=',')
df2 = pd.read_csv('file2.csv',sep=',')
 
print(df1.info()) # Inspect variables df1
print(df2.info()) # Inspect variables df2
 
# Integration of files based on values of x (other variables can be added)
# Cases in df1 take priority, we want to enrich them with data from df2
# That is why we merge 'left', so based on df1
df = pd.merge(df1, df2, how="left", on=['x'])
 
# Inspect variables df
print(df.info()) 
print(df)
