import pandas as pd

input_file = 'data/listings.csv'
output_file = 'data/listings_clean.csv'

fieldnames = [
    'id',
    'name',
    'host_id',
    'host_name',
    'host_is_superhost',
    'host_total_listings_count',
    'neighbourhood_cleansed',
    'beds',
    'price',
    'review_scores_rating',
]

file = pd.read_csv(input_file)
file_filtered = file[fieldnames]
file_filtered.to_csv(output_file, index=False)
