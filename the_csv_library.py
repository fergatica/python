'''
program that asks the user for the names of the input and output files 
and their dialects, after which the program reads all the inputfiles, 
and writes its content in the output file in a desired format. 
'''

import csv

def main():
    '''Enter the name of the input file: lecturepoints.csv
and its dialect: comma
Enter the name of the output file: lecturepoints_converted.csv
and its dialect: unix

'''

    file_name = input("Enter the name of the input file: ")
    dialect = input("and its dialect: ")
    new_file_name = input("Enter the name of the output file: ")
    new_dialect = input("and its dialect: ")

    try:
        with open(file_name, newline='') as csvfile:
            try:
                data_reader = csv.reader(csvfile, dialect=dialect)


                with open(new_file_name, 'w', newline='') as csvfile:
                    data_writer = csv.writer(csvfile, dialect=new_dialect)
                    for row in data_reader:
                        data_writer.writerow(row)
                print()
                print(f"File {file_name} has been converted into {new_dialect}.")

            except csv.Error:
                print()
                print("The given dialect is wrong.")
    except FileNotFoundError:
        print()
        print("There was an error in handling the file.")




main()