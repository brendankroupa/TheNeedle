'''
import csv
import re

def analyze_text_bias(file_path, user_text):
    # Dictionary to hold phrases and their associated bias scores
    aDict = {}

    # Step 1: Load phrases and scores from the CSV file into aDict
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if len(row) == 2:
                key = row[0].strip().lower()
                try:
                    value = int(row[1])
                    aDict[key] = value
                except ValueError:
                    print(f"Warning: Skipping non-integer value in row: {row}")

    # Step 2: Analyze the user-provided text for bias
    user_input = user_text.lower()  # Ensure text is lowercase for matching
    values = []

    # Find all phrases in the dictionary that appear in the text and count occurrences
    for phrase, score in aDict.items():
        matches = re.findall(rf'\b{re.escape(phrase)}\b', user_input)
        count = len(matches)
        values.extend([score] * count)  # Add the score for each occurrence of the phrase

    # Step 3: Determine bias percentage and leaning
    if len(values) < 3:  # Less than 3 'Catches' of political phrasing
        return "Not enough data to determine political leaning.", 0
    else:
        average = sum(values) / len(values)

        if average < 0:
            leaning = "Democratic"
            percentage = abs(average) * 5
        elif average > 0:
            leaning = "Republican"
            percentage = average * 5
        else:
            leaning = "Neutral / Centrist"
            percentage = 0

    return f"{percentage:.1f}% {leaning} leaning based on {len(values)} matching phrases", percentage
    '''
import csv
import re

def analyze_text_bias(file_path, user_text):
    # Dictionary to hold phrases and their associated bias scores
    aDict = {}

    # Step 1: Load phrases and scores from the CSV file into aDict
    try:
        with open(file_path, 'r', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                if len(row) == 2:
                    key = row[0].strip().lower()
                    try:
                        value = int(row[1])
                        aDict[key] = value
                    except ValueError:
                        print(f"Warning: Skipping non-integer value in row: {row}")
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return "Error: CSV file not found.", 0

    # Step 2: Analyze the user-provided text for bias
    user_input = user_text.lower()  # Ensure text is lowercase for matching
    values = []

    # Find all phrases in the dictionary that appear in the text and count occurrences
    for phrase, score in aDict.items():
        matches = re.findall(rf'\b{re.escape(phrase)}\b', user_input)
        count = len(matches)
        values.extend([score] * count)  # Add the score for each occurrence of the phrase

    # Step 3: Determine bias percentage and leaning
    if len(values) < 3:  # Less than 3 'Catches' of political phrasing
        return "Not enough data to determine political leaning.", 0

    average = sum(values) / len(values)

    if average < 0:
        leaning = "Democratic"
        percentage = abs(average) * 5
    elif average > 0:
        leaning = "Republican"
        percentage = average * 5
    else:
        leaning = "Neutral / Centrist"
        percentage = 0

    # Return the bias summary message and percentage
    return f"{percentage:.1f}% {leaning} leaning based on {len(values)} matching phrases", percentage
