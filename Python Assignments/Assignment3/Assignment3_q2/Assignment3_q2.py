from data_fetcher import fetch_data
from data_processor import filter_data
from reporter import display_data

def main():
    file_path = 'data.csv'
    data = fetch_data(file_path)

    if not data:
        print("No data fetched. Exiting program")
        return
    
    filtered_data = filter_data(data, key='status', value='active')

    display_data(filtered_data)
    

if __name__ == "__main__":
    main()