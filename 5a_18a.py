import matplotlib.pyplot as plt # import once at the top of your script

# This snippet assumes you already have a variable catsum, 
# contains the description of the categorical variable/column x
# e.g.,
catsum = rp.summary_cat(df['x'])

# BART CHART- absolute values
plt.bar(catsum['Outcome'], catsum['Count'])
# x-labels based on outcome strings of catsum
# bar height based on count figures of catsum

# Forces tidy plot lay-out
plt.tight_layout()
# Saving the image to a file
plt.savefig('productionlocation-absolute-barchart.pdf')
# Clear figure
plt.clf()
