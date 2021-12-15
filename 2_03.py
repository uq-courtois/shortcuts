import pandas as pd # import pandas module, once at the top of the script

data = pd.DataFrame(newdata) # Converting list of dictionaries into dataframe
data.to_csv('file.csv',sep=',',index=False) # Writing dataframe into file.csv
