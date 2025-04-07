import os
import pandas as pd

# Define the paths
excel_path = r'D:\Python\广西进士\output_headers.xlsx'  # Path to the Excel file
txt_path = r'D:\Python\广西进士'  # Path where the .txt files are stored

# Load the Excel file
df = pd.read_excel(excel_path)

# Initialize a list to store new rows
new_rows = []

# Loop through all .txt files in the specified directory
for filename in os.listdir(txt_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(txt_path, filename)

        try:
            with open(file_path, 'r', encoding='gbk', errors='ignore') as file:  # Changed encoding to gbk
                content = file.readlines()

                # Prepare a row of data corresponding to the table headers
                row_data = {}

                for header in df.columns:
                    # Try to get content for the header, using the first line of the txt file as an example
                    if content:  # Check if content is available
                        # Append the line after the header (e.g., first line corresponds to the first header)
                        row_data[header] = content.pop(0).strip() if content else None
                    else:
                        row_data[header] = None

                # Add the row data to the new_rows list
                new_rows.append(row_data)

        except Exception as e:
            print(f"Error reading {filename}: {e}")

# Create a DataFrame from new rows
new_rows_df = pd.DataFrame(new_rows)

# Concatenate the new rows with the existing DataFrame
df = pd.concat([df, new_rows_df], ignore_index=True)

# Save the modified DataFrame back to the Excel file
df.to_excel(excel_path, index=False)

print(f"Contents of text files appended to {excel_path}")


