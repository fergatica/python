# TIE-02100 Johdatus ohjelmointiin
def dictionary_contents(english_spanish):
    print("Dictionary contents:")
    comma = ", "
    dict_list = []
    for key in sorted(english_spanish):
        dict_list.append(key)
    print(comma.join(dict_list))


def spanish_eng_dict(english_spanish):
    spanish_english = {}
    for key in english_spanish:
        spanish_english[english_spanish[key]] = key
    return spanish_english


def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}
    dictionary_contents(english_spanish)

    while True:
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":
            word = input("Enter the word to be translated: ")
            if word in english_spanish:
                translation = english_spanish[word]
                print(word, "in Spanish is", translation)
            elif word not in english_spanish:
                print("The word", word,
                      "could not be found from the dictionary.")

        elif command == "A":
            new_word = input("Give the word to be added in English: ")
            new_value = input("Give the word to be added in Spanish: ")
            english_spanish[new_word] = new_value
            dictionary_contents(english_spanish)

        elif command == "R":
            remove_word = input("Give the word to be removed: ")
            if remove_word in english_spanish:
                del english_spanish[remove_word]
            elif remove_word not in english_spanish:
                print("The word", remove_word,
                      "could not be found from the dictionary.")

        elif command == "P":
            spanish_english = spanish_eng_dict(english_spanish)
            print()
            print("English-Spanish")
            for key in sorted(english_spanish):
                print(key, english_spanish[key])
            print()
            print("Spanish-English")
            for key in sorted(spanish_english):
                print(key, spanish_english[key])
            print()

        elif command == "T":
            sentence = input("Enter the text to be translated into Spanish: ")
            sentence = sentence.split()
            translation = ""

            for word in sentence:
                if word in english_spanish:
                    translation += english_spanish[word] + " "
                elif word not in english_spanish:
                    translation += word + " "
            print("The text, translated by the dictionary:")
            print(translation)

        elif command == "Q":
            print("Adios!")
            return

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")


main()
