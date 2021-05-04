import pandas as pd
import numpy as np

df = pd.read_csv("../../data/01_raw/listings_bordeaux.csv")



#  the initial df has 64690 rows, 74 col

# from a visual analyse of the df:
useless_columns = [
    "listing_url", "scrape_id", "last_scraped", "description", "neighborhood_overview", "picture_url", "host_url",
    "host_thumbnail_url", "host_picture_url", "host_since", "host_location", "host_about", "host_neighbourhood",
    "host_verifications", "minimum_nights", "maximum_nights", "maximum_minimum_nights", "minimum_maximum_nights",
    "calendar_updated", "has_availability", "availability_30", "availability_60", "availability_90",
    "availability_365", "calendar_last_scraped", "number_of_reviews_ltm", "number_of_reviews_l30d", "first_review",
    "last_review", "license", "reviews_per_month"]

df1 = df.drop(useless_columns, axis=1)
# there are 43 columns left

# analyse types
# type of column price is object
df1[df1.columns[25:26]] = df1[df1.columns[25:26]].replace('[\$,]', '', regex=True).astype(float)

# no duplicate id.

# duplicate listing? drop id to be sure there is no duplicate of the same listing
df2 = df1.drop('id', axis=1)
# there is 4 duplicated row to drop
df3 = df1.drop_duplicates(keep='first')


# drop empty cols?
# bathrooms and neighbourhood_group_cleansed are 100% empty so drop it
df4 = df3.drop(['bathrooms', 'neighbourhood_group_cleansed'], axis=1)
# host_response_time and host_response_rate are 64% empty so drop it
df5 = df4.drop(['host_response_time', 'host_response_rate'], axis=1)


# all the nan in strings columns are replace by "unknown"
obj_col = df5.select_dtypes(include=['object'])
df5[obj_col.columns] = df5[obj_col.columns].replace(np.nan, 'unknown', regex=True)


# all the nan in numbers columns are not replaced because nan is not 0


# do index with id column
df6 = df5.set_index('id')

df7 = df6[df6['review_scores_value'].notna()]


print(df7['review_scores_value'].unique())
df7.to_csv('../../data/02_intermediate/clean_listings_b.csv')
