import pandas as pd

# Load the CSV file
df = pd.read_csv("C:/Users\Admin/Desktop/Module-5_Data-Engineering-Product-Development/python_app/03_Library SystemCustomers.csv")

print(df)

#print("Original Shape:"), df.shape

df = df.drop_duplicates()

df = df.dropna(how='all')

df.reset_index(drop=True, inplace=True)

print("\n=== Cleaned Data ===")
print(df)
print("Cleaned shape:", df.shape)


# Save to a new CSV
df.to_csv("Cleaned_03_Library SystemCustomer.csv", index=False)

print("Cleaned file saved as 'Cleaned_03_Library SystemCustomer.csv'")