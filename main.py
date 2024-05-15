import pandas as pd

# Load your data into a Pandas DataFrame (assuming it's in a CSV file)
data = pd.read_csv("gpt_data.csv")

# Filter for GPTs with 'English' in the description
english_gpts = data[data['GPT Description'].str.contains('English', case=False)]

# You can add more filtering criteria as needed

# Print the cleaned data
print(english_gpts)