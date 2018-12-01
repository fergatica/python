file_name = input("Enter the name of the file: ")

try:
    my_file = open(file_name, 'w')
    print("Enter rows of text. Quit by entering an empty row.")
    user_input = input()
    my_file.write(user_input)
    while True:
        user_input = input()
        my_file.write(user_input)
        if user_input == "":
            break

    my_file.close()
    print("File " + file_name + " has been written.")

except IOError:
    print("Writing the file", file_name, "was not successful.")

