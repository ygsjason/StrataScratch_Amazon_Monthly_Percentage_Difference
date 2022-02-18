# Import your libraries
import pandas as pd

# Start writing code
df1 = sf_transactions.drop_duplicates().sort_values (by = 'created_at', ascending = [True])
#df1['created_month'] = df1.created_at.dt.strftime("%Y-%m")
df2 = df1.assign(created_month = lambda df: df.created_at.dt.strftime('%Y-%m'))

# Groupby month, then caculate monthly total value,
df3 = df2.groupby('created_month')['value'].sum().reset_index(name = 'monthly_value')

#create the new col.: prev_monthly_value
df4 = df3.assign(prev_month_value = lambda df: df.monthly_value.shift(1))

# Create the new col.: pct_chg_rev

#df5 = df4.dropna(subset = ['prev_month_value']).assign(pct_chg_rev = lambda df: ((df.monthly_value - df.prev_month_value)/df.prev_month_value)*100)

df5 = df4.assign(pct_chg_rev = lambda df: ((df.monthly_value - df.prev_month_value)/df.prev_month_value)*100).round(2)
