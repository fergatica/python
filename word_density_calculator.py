def main():
    word_count = {}
    print("Enter rows of text for word counting. Empty row to quit.")
    user_input = input().lower()
    user_input = user_input.split()

    while True:
        if user_input == []:
            break
        for word in user_input:
            if word in word_count:
                word_count[word] += 1
            if word not in word_count:
                word_count[word] = 1
        user_input = input().lower()
        user_input = user_input.split()

    for key in sorted(word_count):
        print(key, ":", word_count[key], "times")


main()
