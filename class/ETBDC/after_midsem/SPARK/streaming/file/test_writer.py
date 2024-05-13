import time

# Define the file path
file_path = "./test_file.txt"

# Function to write data into the file
def write_data(file_path):
    with open(file_path, "a") as file:
        # Write current timestamp into the file
        file.write(f"{time.time()}\n")

# Run the write_data function periodically
while True:
    write_data(file_path)
    # Wait for 5 seconds before writing the next data
    time.sleep(5)

