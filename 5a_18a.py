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
