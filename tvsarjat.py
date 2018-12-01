# TIE-02100 Johdatus ohjelmointiin
# Read genres and tv-series from a file into a dict.
# Print a list of the genres in alphabetical order
# and list tv-series by given genre on user's command.


def read_file(filename):
    # reads and saves the series and their genres from the file

    # TODO initialize a new data structure
    tv_genres = {}

    try:
        file = open(filename, "r")
        for row in file:
            name, genres = row.rstrip().split(";")
            genres = genres.split(",")
            for item in genres:
                if item not in tv_genres:
                    tv_genres[item] = []
            for item in genres:
                if name not in tv_genres[item]:
                    tv_genres[item].append(name)

            # TODO add the info to the data structure

        file.close()
        return tv_genres

    except ValueError:
        print("Error: rows were not in the format name;genres.")
        return None

    except IOError:
        print("Error: the file could not be read.")
        return None


def main():

    filename = input("Enter the name of the file: ")
    TODO = read_file(filename)
    list_of_genres = []

    # TODO print the genres
    for key in sorted(TODO):
        list_of_genres.append(key)

    list_of_genres = str(", ".join(list_of_genres))
    print("Available genres are:", list_of_genres)

    while True:
        genre = input("> ")


        if genre == "exit":
            return
        else:
            try:
                for item in sorted(TODO[genre]):
                    print(item)
            except KeyError:
                continue

main()
