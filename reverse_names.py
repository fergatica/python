def reverse_name(user_input):

    if "," in user_input:
        
        our_index = user_input.index(",")
        first_name = user_input[our_index + 1:len(user_input)].strip()
        last_name = user_input[0:our_index].strip()
        correct_order = (first_name + " " + last_name)
        return correct_order

    elif user_input == ",":
        return ""
    else:
        return ""


def main():
    print(reverse_name("X,"))



main()