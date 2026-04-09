import pandas as pd
import os

# 1. Path to your data folder
data_folder = "data"

# 2. List all CSV files in the data folder
csv_files = [os.path.join(data_folder, f) for f in os.listdir(data_folder) if f.endswith('.csv')]

# 3. Process each CSV
dfs = []
for file in csv_files:
    df = pd.read_csv(file)
    
    # Keep only Pink Morsels
    df = df[df['product'] == 'Pink Morsel']
    
    # Create sales column
    df['sales'] = df['quantity'] * df['price']
    
    # Keep only required columns
    df = df[['sales', 'date', 'region']]
    
    # Add processed df to the list
    dfs.append(df)

# 4. Combine all processed DataFrames
combined_df = pd.concat(dfs, ignore_index=True)

# 5. Save to output CSV
output_file = "processed_sales.csv"
combined_df.to_csv(output_file, index=False)

print(f"Processed data saved to {output_file}")