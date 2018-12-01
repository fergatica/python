import json
import csv


#read from json
#to csv stop_ID;stop_name



def main():
    input_name = input("Enter the name of the input file: ")
    output_name = input("Enter the name of the output file: ")
    is_open = False

    try:
        f = open(input_name)
        is_open = True
    except FileNotFoundError:
        print("There was an error in handling the file.")

    if is_open:
        new_file = open(output_name, "w")

        data = json.load(f)

        for item in data:
            for i in item:
                if i == "stationId":
                    station_id = str(item[i])
                elif i == "name":
                    station_name = str(item[i])
                    new_file.write(station_id + ";" + station_name + "\n")


        print("Conversion succeeded.")
        f.close()
main()