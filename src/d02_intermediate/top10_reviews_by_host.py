import pandas as pd

df_reviews = pd.read_csv('../../data/02_intermediate/clean_reviews.csv')



# ####################################################################""
# goal: display a plot of "number of listings by host"

# print(df_listing.columns)
# df1 = df_listing[['host_name', 'id']]
# df2 = pd.DataFrame(df1['host_name'].value_counts().sort_values(ascending=False).reset_index())
# df2.columns = ['host_name', 'nb_listing']
# df2.to_csv('../../data/03_processed/listings_per_hosts.csv', index=False)
#
# print(df2.head(15).to_string())
# print('ok')
#
