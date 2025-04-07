import pandas as pd

# Define the path to the Excel file
excel_path = r'D:\Python\广西进士\output_headers.xlsx'

# Load the existing Excel file
df = pd.read_excel(excel_path)

# Function to attempt to decode corrupted text
def fix_encoding(text):
    try:
        # Try decoding with different encodings
        return text.encode('latin1').decode('utf-8')
    except Exception as e:
        print(f"Error decoding: {e}")
        return text  # Return the original text if decoding fails

# Apply the decoding function to the DataFrame
for column in df.columns:
    df[column] = df[column].apply(lambda x: fix_encoding(str(x)))  # Convert to string and fix encoding

# Save the corrected DataFrame back to Excel
df.to_excel(excel_path, index=False)

print(f"Excel file updated and saved at {excel_path}")
