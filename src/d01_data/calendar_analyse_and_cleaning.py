import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../../data/01_raw/calendar.csv", parse_dates=['date'])

#  the initial df has 23610091 rows, 7 col

# analyse types
# create 3 col with date
df['day'] = df['date'].dt.day
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year


# transform price and adjusted_price
df[df.columns[3:5]] = df[df.columns[3:5]].replace('[\$,]', '', regex=True).astype(float)

# from a visual analyse of the df: no useless columns

# no duplicate id.

# no duplicate calendar.

# there are no empty cols.

# missing values
# but a reservation with no price neither adjusted_price is useless
df1 = df.dropna(subset=['price', 'adjusted_price'], how='all')
# but a reservation with no minimum_nights neither maximum_nights is useless
df2 = df1.dropna(subset=['minimum_nights', 'maximum_nights'], how='all')

#  the initial df has 23605167 rows, 10 col

# print(df1.head(5).to_string())

df1.to_csv('../../data/02_intermediate/clean_calendar.csv')