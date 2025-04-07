import pandas as pd

# Define the file path
file_path = r"C:\Users\Lou13\Desktop\广西进士_带坐标_去重.csv"

# Read the CSV file
df = pd.read_csv(file_path)

# Check if '坐标' column exists
if '坐标' in df.columns:
    # Split the '坐标' column into 'longitude' and 'latitude'
    df[['longitude', 'latitude']] = df['坐标'].str.split(',', expand=True)

    # Optionally, convert the new columns to float
    df['longitude'] = df['longitude'].astype(float)
    df['latitude'] = df['latitude'].astype(float)

    # Save the updated DataFrame to a new CSV file
    new_file_path = r"C:\Users\Lou13\Desktop\广西进士_带坐标_去重_updated.csv"
    df.to_csv(new_file_path, index=False)
    print(f"Updated file saved as: {new_file_path}")
else:
    print("Column '坐标' does not exist in the file.")
