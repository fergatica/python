def are_all_members_same(a):
    length = len(a) - 1
    falses = 0

    for i in range(length):
        if a[i] != a[i + 1]:
            falses += 1
        i += 1

    if falses > 0:
        return False
    elif falses == 0:
        return True


def main():
    print(are_all_members_same([42, 42, 42, 43, 42]))
    print(are_all_members_same([42, 42, 42, 42]))


main()