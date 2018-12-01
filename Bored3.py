def main():
    user = input("Bored? (y/n) ")
    type(user)

    while user != "y" and user !="Y":
        while user == "n" or user == "N" or user == "y" or user == "Y":
            if user == "y" or user == "Y":
                break
            user = input("Bored? (y/n) ")
            type(user)
        else:
            print("Incorrect entry.")
            user = input("Please retry: ")
            type(user)
    else:
        print("Well, let's stop this, then.")
main()
