import os
import pandas as pd

# Define the path where the .txt files are stored
txt_path = r'D:\Python\广西进士'  # Adjust this path as needed
output_excel_path = os.path.join(txt_path, 'output_headers.xlsx')  # Output Excel file path

# Initialize a list to store the headers
headers = []

# Loop through all .txt files in the specified directory
for filename in os.listdir(txt_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(txt_path, filename)

        # Try reading the file with different encoding
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                for line in file:
                    # Split the line at the colon
                    parts = line.split(':')
                    if len(parts) > 1:  # Check if there is a colon in the line
                        # Get the part before the colon
                        before_colon = parts[0].strip()
                        # Split by spaces and take the last two words
                        words = before_colon.split()
                        if len(words) >= 2:
                            header = ' '.join(words[-2:])  # Take the last two words
                            headers.append(header)
        except Exception as e:
            print(f"Error reading {filename}: {e}")

# Remove duplicates while maintaining order
headers = list(dict.fromkeys(headers))

# Create a DataFrame from the headers
df = pd.DataFrame(columns=headers)

# Save the DataFrame to an Excel file
df.to_excel(output_excel_path, index=False)

print(f"Headers extracted and saved to {output_excel_path}")

