def filter_data(data, key, value):
    return [record for record in data if record.get(key) == value]

