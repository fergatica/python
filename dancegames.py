# TIE-02100 Johdatus ohjelmointiin 
# Dancing Queen


def read_file(filename):
    
    # reads the played songs and their scores from the file

    try:
        fileobject = open(filename, "r")
        
        players = {}

        # loop over fileobject row by row
        for row in fileobject:
            parts = row.strip().split(";")
            player = parts[0]  # name of the player
            songs = parts[1:]  # songs

            # TODO: make a data structure for this single
            #       player that includes his/her songs and scores
            players[player] = {}

            # loop over this player's songs
            for song in songs:

                parts = song.split(":")
                results = parts[1].split(",")
                name = parts[0]  # name of the song

                # list of presses, all integer
                results = [int(luku) for luku in results]

                players[player][name] = results
                # TODO: connect these results to the song
            
            # TODO: add this player's data structure into the 
            #       main data structure
            
        return players

    except IOError:
        print("Error! The file could not be read.")
        return None


def calculate_percentage(values, coefficient):
    counter = 0
    player_score = 0
    max_score = 0

    #loop for player score
    for i in values:
        player_score += (i * coefficient[counter])
        counter += 1

    #loop for max score
    for i in values:
        max_score += i

    max_score = max_score * 5
    percentage = (100/max_score) * player_score

    return percentage

def main():

    coefficients = [5, 4, 2, 0, -6, -12]
    filename = input("Enter the name of the file: ")
    player_dict = read_file(filename)
    # TODO : print ...



    for key1 in sorted(player_dict):
        print(f"{key1}:")
        for key in sorted(player_dict[key1]):
            percentage = calculate_percentage(player_dict[key1][key], coefficients)
            print(f"- {key}: {percentage:.2f}%")


main()
