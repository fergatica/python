def main():
    user_sting = input("Enter a word: ")
    vowels= 0
    consonants = 0
    for ch in user_sting:
        if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
            vowels += 1
        else:
            consonants +=1
    print("The word " + user_sting + " contains " + str(vowels) + " vowels and " + str(consonants) + " consonants")


main()