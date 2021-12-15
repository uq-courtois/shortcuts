# Set max of rows to show, in/decrease to needs
pd.set_option('max_rows', 9999)

# MEAN, STANDARD DEVIATION (std), MEDIAN (50%)
print(df['x'].describe())
