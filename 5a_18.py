import researchpy as rp # import once at the top of your script

# c contains the description of the categorical variable/column x
c = rp.summary_cat(df['x'])
print(c)
