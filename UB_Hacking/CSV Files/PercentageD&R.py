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

#SWAP THIS OUT FOR CSV FILE IN FINAL!!!
user_input = input("Enter words separated by commas: ")
words = [word.strip().lower() for word in user_input.split(',')]

# Calculate the sum and average
values = [aDict[word] for word in words if word in aDict]

if values:
    total = sum(values)
    average = total / len(values)
    
    if average < 0:
        leaning = "Democrat"
        percentage = abs(average) * 10  # Convert to percentage
    elif average > 0:
        leaning = "Republican"
        percentage = average * 10  # Convert to percentage
    else:
        leaning = "Neutral / Centrist"
        percentage = 0
    
    print(f"{percentage:.1f}% {leaning} leaning")
    
else:
    #Nothing matches the CSV
    print("No clear partisan lean")
