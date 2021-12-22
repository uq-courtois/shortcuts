import pandas as pd # import once at the top of your script
import researchpy as rp # import once at the top of your script
import matplotlib.pyplot as  # import once at the top of your script
from pingouin import welch_anova # import once at the top of your script

# BAR PLOTS OF THREE GROUPS IN x FOR A VARIABLE y

# Subset three groups
group1 = df[df['x'] == 'value in x identifying group 1']['y']
group2 = df[df['x'] == 'value in x identifying group 2']['y']
group3 = df[df['x'] == 'value in x identifying group 3']['y']

means = (group1.mean(), group2.mean(), group3.mean())  # Calculating means
positions = [0, 1, 2]  # Defining positions in the graph
plt.bar(positions, means)  # Compiling the plot
plt.xticks(positions, ['label group 1', 'label group 2', 'label group 3'],
           rotation="horizontal")  # Adding labels
plt.tight_layout()  # Forces tidy plot lay-out
plt.savefig("barmeanstd3+.pdf")  # Save figure
plt.clf()  # Clear figure

# Get descriptive table by category
print(rp.summary_cont(df['y'].groupby(df['x'])))
pd.set_option('max_columns', 9999)

# Welch's ANOVA
aov = welch_anova(dv='y', between='x', data=df)
print(aov)
