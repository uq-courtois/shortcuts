# BART CHART- percent
plt.bar(catsum['Outcome'], catsum['Percent'])
# x-labels based on outcome strings of catsum
# bar height based on percentage figures of catsum

# Forces tidy plot lay-out
plt.tight_layout()
# Saving the image to a file
plt.savefig('productionlocation-relative-barchart.pdf')
# Clear figure
plt.clf()
