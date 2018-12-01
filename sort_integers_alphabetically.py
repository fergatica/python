def sort_integers_alphabetically(vehicles):
    return sorted(vehicles, key=lambda x: str(x))


integers = [10, 1, 101, 2, 111, 212, 100000, 22, 222, 112, 10101, 1100, 11, 0]
sort_integers_alphabetically(integers)
