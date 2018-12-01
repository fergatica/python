file_name = input("Enter the name of the score file:")
response1 = ""
response2 = ""
response3 = ""

try:
    f = open(file_name, 'r')
    response1 = "passed"

except FileNotFoundError:
    print("There was an error in reading the file.")

if response1 == "passed":
    game_dictionary = {}

    line = f.readline()

    while line != "":
        name_and_score = line.split(' ')
        if name_and_score[0] in game_dictionary:
            try:
                new_value = name_and_score[1].strip('\n')
            except IndexError:
                response2 = "failed"
                break
            try:
                new_value = int(new_value)
            except ValueError:
                response3 = "failed"
                break

            game_dictionary[name_and_score[0]] += new_value
            line = f.readline()
        if name_and_score[0] not in game_dictionary:
            try:
                new_value = name_and_score[1].strip('\n')
            except IndexError:
                response2 = "failed"
                break
            try:
                new_value = int(new_value)
            except ValueError:
                response3 = "failed"
                break
            game_dictionary[name_and_score[0]] = new_value
            line = f.readline()

    if response3 == "failed":
        print("There was an erroneous score in the file:")
        print(new_value)
    elif response2 == "failed":
        print("There was an erroneous line in the file:")
        print(line)
    elif response2 == "" and response3 == "":
        print("Contestant score:")
        for key in sorted(game_dictionary):
            print(key, game_dictionary[key])


f.close()
