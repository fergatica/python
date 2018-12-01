file_name = input("Enter the name of the file: ")
counter = 1
control = "not passed"
try:
    f = open(file_name)
    control = "passed"

except FileNotFoundError:
    print("There was an error in reading the file.")


if control == "passed":
    line = f.readline()

    while line:
        print(counter, line)
        line = f.readline()
        counter += 1
        f.close()
