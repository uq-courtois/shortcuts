import pandas as pd # import pandas module, once at the top of the script

data = pd.read_csv('filename.csv',sep=',') # Reading data from a file
data = data.T.to_dict().values() # Converting dataframe into list of dictionaries
