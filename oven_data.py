import csv


def main():

    file_name = input("Enter the name of the file to be read: ")

    try:
        f = open(file_name, "r")
        file = "is_open"

    except FileNotFoundError:
        print("Error in reading the file!")



    if file == "is_open":
        new_file_name = input("Enter the name of the file to be written: ")
        test_file = open(new_file_name, "w")
        line1 = f.readline()
        test_file.write(line1)
        for row in f:
            row = row.split(";")
            untouched_data = row[1:]
            row = row[0].split(":")
            hours = int(row[0])
            minutes = int(row[1])
            seconds = int(row[2])
            total_time = (hours * 3600) + (minutes * 60) + seconds
            data_strings = ";".join(untouched_data)
            row_string = str(total_time) + ";" + data_strings
            test_file.write(row_string)
        f.close()
        test_file.close()
        print("Information saved successfully.")


main()