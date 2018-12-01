def count_abbas(sentence):
    counter = 0

    x = 0

    while x < len(sentence):

        if "abba" in sentence[x:x + 4]:
            counter += 1

        x += 1

    return counter