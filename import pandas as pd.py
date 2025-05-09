import pandas as pd
file_path = "C:/Users/Sharm/Downloads/candidate_list.csv"
df = pd.read_csv(file_path)
print("Initial Dataset Info:")
print(df.info())
df = df.apply(lambda col: col.fillna("Unknown") if col.dtype == "object" else col.fillna(col.mean()))
df = df.drop_duplicates()
print("\nCleaned Dataset Info:")
print(df.info())
cleaned_file_path = "cleaned_candidate_list.csv"
df.to_csv(cleaned_file_path, index=False)
print(f"\nCleaned dataset saved as {cleaned_file_path}")
