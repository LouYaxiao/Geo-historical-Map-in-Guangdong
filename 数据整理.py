import os
import win32com.client
import pandas as pd
import re


# Function to clean text by removing illegal characters
def clean_text(text):
    # Remove any characters that are not valid in Excel
    return re.sub(r'[\x00-\x1F\x7F]', '', text)


# Define the path where the Word documents are stored
docx_path = r'D:\Python\广西进士'

# Initialize a list to store data
data_list = []

# Initialize the Word application
word = win32com.client.Dispatch('Word.Application')
word.Visible = False  # Set to True if you want to see Word opening

# Loop through all Word documents in the specified directory
for filename in os.listdir(docx_path):
    if filename.endswith('.docx'):
        doc_path = os.path.join(docx_path, filename)

        # Open the Word document
        doc = word.Documents.Open(doc_path)

        # Iterate through paragraphs in the document
        for i in range(1, doc.Paragraphs.Count + 1):  # Use Count for safe iteration
            para = doc.Paragraphs(i)  # Access each paragraph by index
            text = para.Range.Text.strip()
            if ':' in text:
                # Split the paragraph into key and value based on the first occurrence of ':'
                key, value = text.split(':', 1)
                # Strip whitespace and clean text
                key = clean_text(key.strip())
                value = clean_text(value.strip())
                data_list.append((key, value))

        # Close the document
        doc.Close(SaveChanges=False)

# Quit the Word application
word.Quit()

# Convert the list to a pandas DataFrame
df = pd.DataFrame(data_list, columns=['Column Name', 'Content'])

# Define the output Excel file path
output_excel_path = r'D:\Python\广西进士\output.xlsx'

# Save the DataFrame to an Excel file
df.to_excel(output_excel_path, index=False)

print(f"Excel file saved at: {output_excel_path}")


