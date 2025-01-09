import json

def load_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: The file '{file_path}' is not a valid JSON file.")
        return None

def validate_json(data, required_fields):
    missing_fields = {field for field in required_fields if field not in data}
    return missing_fields

def generate_report(data, required_fields):
    if not data:
        return

    total_entries = len(data)
    missing_fields = validate_json(data[0], required_fields)

    print(f"Total Entries: {total_entries}")
    print(f"Missing Fields: {missing_fields}")

def main():
    file_path = 'data.json'  
    required_fields = ['id', 'name', 'email']

    data = load_json(file_path)
    if data:
        generate_report(data, required_fields)

if __name__ == "__main__":
    main()
