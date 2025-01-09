import csv

def fetch_data(file_path):
    data = []
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"Error: In opening file")
    except Exception as e:
        print(f"An error occured while reading the file: {e}")
    return data

