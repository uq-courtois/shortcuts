import pandas as pd # import once at the top of your script

df1 = pd.read_csv('file1.csv',sep=';') # Read file 1
df2 = pd.read_csv('file2.csv',sep=';') # Read file 2
 
print(df1.info()) # Info for df1
print(df2.info()) # Info for df2
 
df = df1.append(df2) # Adding df1 and df2 together
 
print(df.info()) # Info for df
