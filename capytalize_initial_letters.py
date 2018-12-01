def capitalize_initial_letters(sentence):

    word_list = sentence.split()  # list with the words

    words_to_return = []

    counter = 0

    while counter < len(word_list):
        first = word_list[counter]
        word = first.capitalize()
        counter += 1
        words_to_return.append(word)

    words_to_return = " ".join(words_to_return)

    return words_to_return