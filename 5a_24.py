import pandas as pd # import once at the top of your script
from scipy import stats # import once at the top of your script
import matplotlib.pyplot as  # import once at the top of your script

# BAR PLOTS OF TWO GROUPS in x FOR A VARIABLE y

# Subset two groups
group1 = df[df['x'] == 'value that identifies group 1']['y']
group2 = df[df['x'] == 'value that identifies group 2']['y']

means = (group1.mean(), group2.mean())  # Calculating means
positions = [0, 1]  # Defining positions in the graph
plt.bar(positions, means)  # Compiling the plot
plt.xticks(positions, ['Label for group 1', 'Label for group 2'],
           rotation="horizontal")  # Adding labels
plt.tight_layout()  # Forces tidy plot lay-out
plt.savefig("barmeanstd.pdf")  # Save figure
plt.clf()  # Clear figure

# Calculate and print Welch’s t-test
print(stats.ttest_ind(group1, group2, equal_var=False))
