import matplotlib.pyplot as plt # import once at the top of your script

# HISTOGRAM
# Render histogram of numeric variable/column x
# (By increasing the bins number, you smoothen/add detail to the graph)
plt.hist(df['x'], bins=100)

# Forces tidy plot lay-out
plt.tight_layout()
# Save figure as pdf
plt.savefig('histo_x.pdf')
# Clear figure
plt.clf()
