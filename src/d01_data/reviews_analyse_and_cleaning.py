import pandas as pd

df = pd.read_csv("../../data/01_raw/reviews.csv",  parse_dates=['date'])

#  the initial df has 1213727 rows, 6 col

# analyse types
# create 3 col with date
df['day'] = df['date'].dt.day
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year

# from a visual analyse of the df:
useless_columns = ['comments']

# drop useless columns:
df1 = df.drop(useless_columns, axis=1)

# there are 5 columns left

# no duplicate id.

# duplicate reviews? drop id to be sure there is no duplicate of the same listing
# there is 53 duplicated row to drop
df3 = df1.drop_duplicates(keep='first')

# there are 1213727 rows and 5 col staying

# there are no empty cols.

# do index with id column
df4 = df3.set_index('id')
# print(df4.head(5).to_string())


df4.to_csv('../../data/02_intermediate/clean_reviews.csv')