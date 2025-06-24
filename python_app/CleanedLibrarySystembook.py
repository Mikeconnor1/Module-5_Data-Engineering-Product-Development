import pandas as pd
#import numpy as np

# Load the CSV file
df = pd.read_csv("C:/Users/Admin/Desktop/Module-5_Data-Engineering-Product-Development/python_app/03_Library Systembook.csv")

print("Original Shape:"), df.shape

#drop na
df = df.dropna(how='all')

#remove " "
df['Book checkout'] = pd.to_datetime(df['Book checkout'].str.replace('"',''), errors='coerce')

#drop duplicates
df = df.drop_duplicates()

df.reset_index(drop=True, inplace = True)

print("\n=== Cleaned Data ===")
print(df)

print("\nFinal shape:", df.shape)

#remove blank rows
#df.head
#str.replace

# Save to a new CSV
df.to_csv("Cleaned_03_Library SystemBook.csv", index=False)

print("Cleaned file saved as 'Cleaned_03_Library SystemBook.csv'")