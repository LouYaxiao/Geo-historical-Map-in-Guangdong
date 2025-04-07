# File: convert_excel_to_csv.py

import pandas as pd

# Define the file paths
excel_file_path = r"D:\大三上学期课程材料\大创\广西进士\广西进士.xlsx"
csv_file_path = r"D:\大三上学期课程材料\大创\广西进士\广西进士.csv"

# Read the Excel file
try:
    # Load the Excel file into a DataFrame
    df = pd.read_excel(excel_file_path)

    # Save the DataFrame to a CSV file
    df.to_csv(csv_file_path, index=False, encoding='utf-8-sig')

    print(f"Successfully converted the Excel file to CSV at: {csv_file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
