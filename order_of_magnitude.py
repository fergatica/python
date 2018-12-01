def is_the_list_in_order(a):
    length = len(a) - 1
    falses = 0

    for i in range(length):
        if a[i] > a[i + 1]:
            falses += 1
        i += 1

    if falses > 0:
        return False
    elif falses == 0:
        return True


def main():
    print(is_the_list_in_order([42, 43, 48, 49, 50]))
    print(is_the_list_in_order([42, 42, 42, 41]))


main()