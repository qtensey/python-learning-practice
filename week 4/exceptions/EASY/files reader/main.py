from pathlib import Path

def read_file_safely(filepath):
    try:
        file = open(filepath, 'r', encoding='utf-8')
        file_content = file.read
    except FileNotFoundError:
        print("Error: file not found!")
    else:
        print("the file was read successfully. Content: ", )
        file.close()
    finally:
        print("block 'finally' completed. Cleaning is complete.")

read_file_safely("asdasd")