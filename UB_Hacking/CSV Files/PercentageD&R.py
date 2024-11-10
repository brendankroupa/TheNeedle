import csv
import re

# Load the CSV data into a dictionary with lowercase keys
file = "D&RTest3.csv"
aDict = {}

with open(file, 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        if len(row) == 2:
            key = row[0].strip().lower()
            try:
                value = int(row[1])
                aDict[key] = value
            except ValueError:
                print(f"Warning: Skipping non-integer value in row: {row}")

# Input: block of text
user_input = input("Enter a block of text: ").lower()

# Initialize total score and count for occurrences
total_score = 0
total_count = 0

# Find all phrases in the dictionary that appear in the text and count occurrences
for phrase, score in aDict.items():
    matches = re.findall(rf'\b{re.escape(phrase)}\b', user_input)
    count = len(matches)  # Count the occurrences of the phrase

    if count > 0:
        total_score += score * count  # Add the score multiplied by occurrences
        total_count += count  # Add the count to the total

# Calculate the average based on detected phrases
if total_count > 0:
    average = total_score / total_count
    
    if average < 0:
        leaning = "Democratic"
        percentage = abs(average) * 10  # Convert to percentage
    elif average > 0:
        leaning = "Republican"
        percentage = average * 10  # Convert to percentage
    else:
        leaning = "Neutral / Centrist"
        percentage = 0
    
    print(f"{percentage:.1f}% {leaning} leaning based on {total_count} matching phrases")
else:
    print("No partisan lean.")

