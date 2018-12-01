file_name = input("Enter the name of the file: ")
file_is_open = ""
expense_dictionary = {}
name = ""
expense = ""

try:
    f = open(file_name, 'r')
    file_is_open = "yes"
except FileNotFoundError:
    print("Error: file", file_name, "cannot be read.")

erroneous_line = False
if file_is_open == "yes":
    line = f.readline()
    while line != "":
        line = line.strip()
        line = line.strip("\n")
        name_and_expense = line.split(':')

        if len(name_and_expense) == 2:
            if name_and_expense[0] not in expense_dictionary:
                expense_dictionary[name_and_expense[0]] = []
                try:
                    expense_dictionary[name_and_expense[0]].append(float(name_and_expense[1]))
                    line = f.readline()
                except ValueError:
                    print("Error: there was an erroneous line in the file.")
                    erroneous_line = True
                    break

            elif name_and_expense[0] in expense_dictionary:
                try:
                    expense_dictionary[name_and_expense[0]].append(float(name_and_expense[1]))
                    line = f.readline()
                except ValueError:
                    print("Error: there was an erroneous line in the file.")
                    erroneous_line = True
                    break
        else:
            print("Error: there was an erroneous line in the file.")
            erroneous_line = True
            break

    if erroneous_line == False:
        divisor = len(expense_dictionary)
        total_costs = 0
        person_paid_total = 0

        for key in expense_dictionary:
            for i in expense_dictionary[key]:
                i = float(i)
                total_costs += i
        print(f"Total costs: {total_costs:.2f}e")
        print()

        person_cost = total_costs / divisor

        for key in sorted(expense_dictionary):
            person_paid_total = 0
            for i in expense_dictionary[key]:
                i = float(i)
                person_paid_total += i

            person_paid_amounts = ", ".join(str(f"{i:.2f}") for i in expense_dictionary[key])
            print(
                    f"{key} has paid {person_paid_total:.2f} "
                    f"in the following amounts: {person_paid_amounts}")

            if (person_cost - person_paid_total) < 0.05 \
                    and person_cost - person_paid_total > (-0.05) \
                    or (person_paid_total - person_cost) < 0.05 \
                    and person_paid_total - person_cost > (-0.05):
                print("No transfers needed.")
                print()
            elif person_cost > person_paid_total:
                print(f"{key} needs to pay {person_cost-person_paid_total:.2f}e.")
                print()
            elif person_cost < person_paid_total:
                print(f"{key} needs to receive {person_paid_total-person_cost:.2f}e.")
                print()
            f.close()
