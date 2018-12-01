def calculate_dose(weight, time, total_doze_24):
    if time < 6:
        return 0
    elif time == 24 :
        dose_in_mg = ((weight * 15 * 4) - total_doze_24) / 4
        return dose_in_mg
    else:
        dose_in_mg = ((weight * 15 * 4) - total_doze_24) / 3
        return dose_in_mg


def main():
    weight = input("Patient's weight (kg): ")
    last_dose_time = input(
        "How much time has passed from the previous dose (full hours): ")
    last_total_dose = input("The total dose for the last 24 hours (mg): ")

    weight = int(weight)
    last_dose_time = int(last_dose_time)
    last_total_dose = int(last_total_dose)

    print("The amount of Medicine to give to the patient: ", end="")
    dose = calculate_dose(weight, last_dose_time, last_total_dose)
    print("{:.0f}".format(dose))


main()


