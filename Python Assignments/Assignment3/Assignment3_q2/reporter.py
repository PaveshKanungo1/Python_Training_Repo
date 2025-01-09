def display_data(data):
    if not data:
        print("No data is here.")
        return
    
    for record in data:
        print(record)