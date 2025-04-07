import os
import win32com.client

# Define the path where the Word documents are stored
docx_path = r'D:\Python\广西进士'

# Initialize the Word application
word = win32com.client.Dispatch('Word.Application')
word.Visible = False  # Set to True if you want to see Word opening

# Define the constant for text format
wdFormatText = 2  # wdFormatText constant is typically 2

# Loop through all Word documents in the specified directory
for filename in os.listdir(docx_path):
    if filename.endswith('.docx') and not filename.startswith('~$'):  # Skip temporary files
        doc_path = os.path.join(docx_path, filename)

        try:
            # Open the Word document
            doc = word.Documents.Open(doc_path)

            # Define the output text file path
            txt_filename = filename.replace('.docx', '.txt')
            txt_path = os.path.join(docx_path, txt_filename)

            # Save the document as a text file
            doc.SaveAs(txt_path, FileFormat=wdFormatText)

            # Close the document
            doc.Close(SaveChanges=False)

        except Exception as e:
            print(f"Failed to process {filename}: {e}")

# Quit the Word application
word.Quit()

print(f"All valid .docx files in {docx_path} have been converted to .txt files.")


