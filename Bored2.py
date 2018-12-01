def main():
    user = input("Answer Y or N: ")
    type(user)

    while user != "y" and user != "Y" and user != "N" and user != "n":
        print("Incorrect entry.")
        user = input("Please retry: ")
        type(user)
    else:
        print("You answered", user)

main()