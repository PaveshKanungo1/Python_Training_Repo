import os

def merge_files(file_list, output_file, remove_duplicates=False):
    lines = set() if remove_duplicates else []

    for file_path in file_list:
        if not os.path.exists(file_path):
            print(f"Warning: '{file_path}' does not exist and will be skipped.")
            continue
        if not os.access(file_path, os.R_OK):
            print(f"Warning: '{file_path}' is not readable and will be skipped.")
            continue

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    lines.add(line) if remove_duplicates else lines.append(line)
        except Exception as e:
            print(f"Error reading '{file_path}': {e}")
    
    try:
        with open(output_file, 'w', encoding='utf-8') as output:
            if remove_duplicates:
                output.writelines(sorted(lines))
            else:
                output.writelines(lines)
        print(f"Files merged successfully into '{output_file}'.")
    except Exception as e:
        print(f"Error writing to '{output_file}': {e}")

files_to_merge = ['file1.txt', 'file2.txt', 'file3.txt']
output_file = 'merged_output.txt'
merge_files(files_to_merge, output_file, remove_duplicates=True)