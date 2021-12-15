import pandas as pd # import pandas module, once at the top of the script

data = pd.read_csv('https://digitalanalytics.id.au/static/files/csvtutorial.csv',sep=',') # Reading data from a URL
data = data.T.to_dict().values() # Converting dataframe into list of dictionaries
