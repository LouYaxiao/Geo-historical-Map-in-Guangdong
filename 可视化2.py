# File: visualize_duplicate_counts_chinese.py

import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.sans-serif'] = ['SimHei']  # For Windows
rcParams['axes.unicode_minus'] = False

# Directory containing the output CSV files
output_directory = r"D:\大三上学期课程材料\大创\广西进士\mygeodata\output_tables3"
visualization_directory = r"D:\大三上学期课程材料\大创\广西进士\mygeodata\visualizations2"

# Ensure visualization directory exists
os.makedirs(visualization_directory, exist_ok=True)

# Iterate through the CSV files in the output directory
try:
    for file_name in os.listdir(output_directory):
        if file_name.endswith("_duplicates.csv"):
            file_path = os.path.join(output_directory, file_name)

            # Read the CSV file with proper encoding for Chinese characters
            df = pd.read_csv(file_path, encoding='utf-8-sig')

            # Extract the column name from the file name
            column_name = file_name.replace("_duplicates.csv", "")

            # Visualize the data as a bar chart
            plt.figure(figsize=(10, 6))
            plt.bar(df[column_name], df['Count'], color='skyblue')
            plt.title(f"Duplicate Counts for Column: {column_name}", fontsize=16)
            plt.xlabel(column_name, fontsize=12)
            plt.ylabel("Count", fontsize=12)
            plt.xticks(rotation=45, ha="right", fontsize=10)
            plt.tight_layout()

            # Save the bar chart
            visualization_path = os.path.join(visualization_directory, f"{column_name}_chart.png")
            plt.savefig(visualization_path, dpi=300)
            plt.close()

            print(f"Visualization saved for column '{column_name}' at: {visualization_path}")

except Exception as e:
    print(f"An error occurred: {e}")

