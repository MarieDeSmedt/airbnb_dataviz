import pandas as pd

df_listing = pd.read_csv('../../data/02_intermediate/clean_listings_b.csv')



# ####################################################################""
# goal: display the top10 of host by nb of listing"

# print(df_listing.columns)
df1 = df_listing[['host_name', 'id']]
df2 = pd.DataFrame(df1['host_name'].value_counts().sort_values(ascending=False).reset_index())
df2.columns = ['host_name', 'nb_listing']
df2.to_csv('../../data/03_processed/top10_bordeaux_hosts.csv', index=False)

print(df2.head(15).to_string())
print('ok')

