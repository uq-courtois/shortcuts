import pandas as pd # import once at the top of your script
import researchpy as rp # import once at the top of your script
import matplotlib.pyplot as plt # import once at the top of your script

# STACKED BAR CHART for variables/columns x and y
ct = pd.crosstab(df['x'], df['y'],
                 normalize='index')  # Create PD crosstab as basis for plot
ct.plot.bar(stacked=True)  # Generate plot
plt.legend(loc='lower left', bbox_to_anchor=(0.0, 1.01),
           frameon=False)  # Tidy up legend (other)
plt.xticks(rotation="horizontal")  # Horizontal x-axis labels
plt.xlabel('Enter label for x-axis here')  # Adding label on x-axis
plt.ylabel('Enter label of y-axis here')  # Adding label on y-axis
plt.tight_layout()  # Forces tidy plot lay-out
plt.savefig('stackedbar.pdf')  # Saving figure

# Clear figure
plt.clf()
