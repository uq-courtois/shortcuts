# HISTOGRAM
# Render histogram (By increasing the bins number, you smoothen the graph)
plt.hist(df['x'], bins=100)

# Forces tidy plot lay-out
plt.tight_layout()
# Save figure as pdf
plt.savefig('histo_x.pdf')
# Clear figure
plt.clf()
