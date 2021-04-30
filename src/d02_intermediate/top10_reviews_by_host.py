import pandas as pd
import numpy as np

df_listing = pd.read_csv('../../data/02_intermediate/clean_listing.csv')

# ####################################################################""
# goal: top 10  of reviews by host


df1 = df_listing[['host_id', 'host_name', "review_scores_value"]]

# print(df1[df1['host_id'] == 291007369])


# calculate mean review by host
df2 = df1.groupby(by='host_id').agg({'host_name' : 'first', 'review_scores_value' : np.mean})

# print(df2[df2.index == 291007369])

df2.to_csv('../../data/03_processed/top10_reviews.csv', index=False)
print(df2.head(15).to_string())
print('ok')
