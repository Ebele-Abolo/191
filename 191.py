sorted_df = df.sort_values(by=[ ‘column_name’])
lowest_cases = sorted_df[‘column_name’].head(5)
highest_cases = sorted_df[‘column_name’].tail(5