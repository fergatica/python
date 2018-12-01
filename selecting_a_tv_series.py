def read_file(filename):
    contacts = {}
    f = open(filename, "r")
    line = f.readline().strip("\n")
    first_line = line.split(";")
    print(first_line)
    line = f.readline().strip("\n")

    while line != "":

        line_list = line.split(";")
        contacts[line_list[0]] = {}

        i = 1

        while i < (len(line_list)):
            contacts[line_list[0]][first_line[i]] = line_list[i]
            i += 1

        line = f.readline().strip("\n")


    return contacts
