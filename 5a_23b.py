import pandas as pd # import once at the top of your script
import matplotlib.pyplot as  # import once at the top of your script

# Displaying time series

# Calculate mean, minimum, and maximum ratings per year (groupby)
# Here, 4 aggregates are created, meant to draw 4 plot lines
# Each aggregate is a different statistic: mean, median, min, max
ymean = df.groupby('year', as_index=False)['rating'].mean()
ymdn = df.groupby('year', as_index=False)['rating'].median()
ymin = df.groupby('year', as_index=False)['rating'].min()
ymax = df.groupby('year', as_index=False)['rating'].max()

# Plot these variables together
# Here,the 4 plot lines are added
plt.plot(ymin['year'], ymin['rating'], label="Minimum rating")
plt.plot(ymean['year'], ymean['rating'], label="Average rating")
plt.plot(ymdn['year'], ymdn['rating'], label="Median rating")
plt.plot(ymax['year'], ymax['rating'], label="Maximum rating")

# Add a legend
plt.legend()

# Forces tidy plot lay-out
plt.tight_layout()

# Save the figure
plt.savefig('timeseries.pdf')
