file_name = input("Enter the name of the file: ")

f = open(file_name)
line = f.readline()
counter = 1
while line:
    print(counter, line)
    line = f.readline()
    counter += 1

f.close()