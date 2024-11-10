import csv

# Load the CSV data into a dictionary with lowercase keys
file = "D&R.csv"
aDict = {}

with open(file, 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        if len(row) == 2:
            key = row[0].lower() 
            value = int(row[1])
            aDict[key] = value

# Prompt the user for input and convert each word to lowercase
user_input = input("Enter words separated by commas: ")
words = [word.strip().lower() for word in user_input.split(',')]

# Calculate the sum and average
values = [aDict[word] for word in words if word in aDict]

if values:
    total = sum(values)
    average = total / len(values)
    
    # Determine the leaning as Liberal or Conservative
    if average < 0:
        leaning = "Liberal"
        percentage = abs(average) * 10  # Convert to percentage
    elif average > 0:
        leaning = "Conservative"
        percentage = average * 10  # Convert to percentage
    else:
        leaning = "Neutral / Centrist"
        percentage = 0
    
    print(f"{percentage:.1f}% {leaning} leaning")
    
else:
    #No matches in the CSV
    print("No clear partisan lean")
