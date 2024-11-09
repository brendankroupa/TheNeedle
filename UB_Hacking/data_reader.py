import csv

def read_data():
    with open("C:\\Users\\4051c\\code\\python\\the-needle\\ub-hacking-create-your-repo-here-theneedle-main\\UB_Hacking\\bias_weights.csv", newline="") as csvfile:
        data = csv.reader(csvfile, delimiter=",")
        data_dict = {row[0]: row[1] for row in data}
        return data_dict
