import csv
'''
def read_data(csv):
    with open(csv, newline="") as csvfile:
        data = csv.reader(csvfile, delimiter=",")
        data_dict = {row[0].lower(): int(row[1]) for row in data}
        return data_dict
'''
def read_data(file_path):
    data_dict = {}
    
    try:
        with open(file_path, newline="", encoding="utf-8") as csvfile:
            data = csv.reader(csvfile, delimiter=",")
            for row in data:
                if len(row) == 2:  # Ensure each row has exactly two values
                    try:
                        data_dict[row[0].lower()] = int(row[1])  # Add key-value pair to dictionary
                    except ValueError:
                        print(f"Warning: Skipping non-integer value in row: {row}")
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return data_dict