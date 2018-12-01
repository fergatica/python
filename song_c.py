def repeat_name(name, times):
    count = 1
    while count <= times:
        if times == 3:
            print(name + ", " + name + " Bear")
            count += 1
        else:
            print(name + ", " + name, end="")
            count += 1


def verse(sentence, name):
    print(sentence)
    repeat_name(name, 1)
    print()
    print(sentence)
    repeat_name(name, 3)
    print(sentence)
    repeat_name(name, 1)
    print(" Bear")
    print()

def main():
    verse("I know someone you don't know", "Yogi")
    verse("Yogi has a best friend too", "Boo Boo")
    verse("Yogi has a sweet girlfriend", "Cindy")

main()
