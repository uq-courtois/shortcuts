import researchpy as rp # import once at the top of your script

# CORRELATION between numeric variables.columns x and y
print(rp.correlation.corr_pair(df[['x', 'y']]))

# The r-value is the magnitude of the correlation
# p-value expresses statistical significance level
# N reports number of cases the analysis is based on
