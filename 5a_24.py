from scipy import stats
# BAR PLOTS OF TWO GROUPS FOR A VARIABLE

# Subset two groups
group1 = df[df['sfxgenre'] == 'lower sfx']['rating']
group2 = df[df['sfxgenre'] == 'higher sfx']['rating']

means = (group1.mean(), group2.mean())  # Calculating means
positions = [0, 1]  # Defining positions in the graph
plt.bar(positions, means)  # Compiling the plot
plt.xticks(positions, ['Low SFX', 'High SFX'],
           rotation="horizontal")  # Adding labels
plt.tight_layout()  # Forces tidy plot lay-out
plt.savefig("barmeanstd.pdf")  # Save figure
plt.clf()  # Clear figure

# Calculate and print Welch’s t-test
print(stats.ttest_ind(group1, group2, equal_var=False))
