def sort_neglecting_case(vehicles):
    return sorted(vehicles, key=lambda x: x.lower())


vehicles = ["Mercedes", "BMW", "Lada", "car", "Audi", "automobile"]
sort_neglecting_case(vehicles)
