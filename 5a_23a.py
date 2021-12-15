# SCATTERPLOT
plt.scatter(df['agefilm'], df['rating'])  # Build plot
plt.xlabel('Age of Movie')  # x-axis label
plt.ylabel('IMDB user rating')  # y-axis label
plt.tight_layout()  # Forces tidy plot lay-out
plt.savefig('scatterplot.pdf')  # Save figure
plt.clf()  # Clear figure
