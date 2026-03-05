# Read file and write content in uppercase

source = input("Enter source file name: ")
destination = input("Enter destination file name: ")

with open(source, "r") as f:
    data = f.read()

upper_data = data.upper()

with open(destination, "w") as f:
    f.write(upper_data)

print("Content copied in uppercase successfully.")
