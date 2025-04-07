import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the sentiment analysis results with a specified encoding
file_path = r"D:\大三上学期课程材料\大创\广西进士\vater\sentiment_analysis_output4(USnewstest).csv"
try:
    results_df = pd.read_csv(file_path, encoding='utf-8')  # Try UTF-8 first
except UnicodeDecodeError:
    results_df = pd.read_csv(file_path, encoding='ISO-8859-1')  # Fallback to ISO-8859-1

# Print column names to verify if the expected columns exist
print("Columns in the dataset:", results_df.columns)

# Check if the required sentiment columns exist in the DataFrame
required_columns = ['Negative', 'Neutral', 'Positive']
missing_columns = [col for col in required_columns if col not in results_df.columns]

if missing_columns:
    print(f"Error: Missing columns in the dataset: {missing_columns}")
else:
    # Calculate the total counts of each sentiment
    sentiment_counts = results_df[required_columns].sum()

    # Calculate the percentage of each sentiment
    sentiment_percentage = (sentiment_counts / sentiment_counts.sum()) * 100
    sentiment_percentage = sentiment_percentage.sort_index()  # Sort by index for better visualization

    # Plotting the distribution of sentiment percentages
    plt.figure(figsize=(8, 5))
    sns.barplot(x=sentiment_percentage.index, y=sentiment_percentage.values, palette='viridis')
    plt.title('Percentage Distribution of Sentiment')
    plt.xlabel('Sentiment')
    plt.ylabel('Percentage (%)')
    plt.xticks(rotation=0)  # Rotate x labels if necessary
    plt.ylim(0, 100)  # Set y-axis limit from 0 to 100
    plt.grid(axis='y')

    # Show percentage values on the bars
    for index, value in enumerate(sentiment_percentage.values):
        plt.text(index, value + 1, f'{value:.2f}%', ha='center')

    plt.tight_layout()
    plt.show()



