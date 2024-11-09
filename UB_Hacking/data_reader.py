import csv

def read_data():
    with open("C:\\Users\\shoem\\Desktop\\UB_Hacking\\bias_weights.csv", newline="") as csvfile:
        data = csv.reader(csvfile, delimiter=" ")
        data_dict = {row[0]: row[1] for row in data}
        return data_dict


test_data = read_data()
for word in test_data.keys:
    print(f"{key}: {test_data[key]}")
