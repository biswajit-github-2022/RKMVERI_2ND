import time
import uuid
import os

# Base directory where new files will be created
base_dir = "./data/"
# Ensure the base directory exists or create it
os.makedirs(base_dir, exist_ok=True)

def append_data():
    while True:
        file_path = f"{base_dir}{uuid.uuid4()}.txt"
        with open(file_path, 'w') as file:
            file.write("Elephant\n")  # Write "abcd" to a new file
        time.sleep(10)  # Wait for 10 seconds before creating a new file

# Call the function to append data
append_data()

