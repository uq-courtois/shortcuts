import matplotlib.pyplot as  # import once at the top of your script
import pandas as pd # import once at the top of your script

# SCATTERPLOT for variables x and y
plt.scatter(df['x'], df['y'])  # Build plot
plt.xlabel('Enter label of x-axis here')  # x-axis label
plt.ylabel('Enter label of y-axis here')  # y-axis label
plt.tight_layout()  # Forces tidy plot lay-out
plt.savefig('scatterplot.pdf')  # Save figure
plt.clf()  # Clear figure
