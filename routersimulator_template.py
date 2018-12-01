"""how the data in the routing tables of routers change when the device 
communicate with each other. """


class Router:
    def __init__(self, name):
        """
        Constructor. Checks that the name is of
        correct type and initialize it.
        :param name: the routers name as a string parameter
        """
        if not isinstance(name, str):
            raise TypeError

        self.__name = name
        self.__n = []
        self.__r = []

    def print_router(self):
        """
        :param: none
        Prints the N and R of the object
        """
        string_of_n = ', '.join(sorted(self.__n))
        string_of_r = ", ".join(sorted(self.__r))
        print(" ", self.__name)
        print(" ", " ", "N: ",  string_of_n)
        print(" ", " ", "R: ", string_of_r)

    def return_n_list(self):
        """
        :param: none
        :return: n list
        """
        return self.__n

    def return_r_list(self):
        """
        :param: none
        :return: n list
        """
        return self.__r

    def add_neighbor(self, other):
        """ The function checks the function has already added the neighbor
        if not, then it adds each other to the n list
        :param: other object
        :return: none
        """
        if other.__name not in self.__n and other.__name != "":
            self.__n.append(other.__name)
        if self.__name not in other.__n and self.__name != "":
            other.__n.append(self.__name)

    def add_network(self, address, distance):
        """ The function checks the address has been passed as string
        and distance as int.
        Then the function adds both factors to the r list as string
        :param: address and distance
        :return: none
        """
        if not isinstance(address, str):
            raise TypeError
        if not isinstance(distance, int):
            raise TypeError

        self.__r.append(address + ":" + str(distance))

    def print_all(self, router_dictionary):
        """ The function iterates through the object dictionary
        for each ithem, it calls the print function
        :param: router_dictionary
        :return: none
        """
        for item in router_dictionary:
            item.print_router()

    def receive_routing_table(self, other):
        """When the command "S" is executed,
        this method is to be called for the router's neighbours.
        If you want R1 to send its routing table to R2, you will call the method receive_routing_table of the object R2 and give the the object R1 as a parameter.
        This means R2 receives the routing table when R1 sends it. """

        num = 0
        print(other.__r)
        for other_item in other.__r:
            print(other_item)
            parts = other_item.split(":")  # splits the list of the address and distaNce
            print(parts)

            other_address = parts[0]

            other_distance = int(parts[1]) + 1  # makes distance to int, and adds 1

            parts = other_address + ":" + str(other_distance)

            num += 1

            '''for my_item in self.__r:
                my_parts = my_item.split[":"]
                my_address = my_parts[0]
                my_distance = int(my_parts[1])'''



            #if my_address != other_address:
            if parts not in self.__r: #and my_address != other_address:
                self.__r.append(parts)  # appends the new address to the receiver router




def readfile(routerfile, router_dictionary):
    file = ""
    try:
        f = open(routerfile, "r")
        file = "is_open"

    except FileNotFoundError:
        print("Error: the file could not be read or there is something wrong with it.")

    if file == "is_open":
        line = f.readline().strip("\n")
        while line != "":
            values = line.split("!")    # splits line into list
            router_name = values[0]     # takes first value and assigns as name
            router_friends_as_list = values[1].split(";")   #splits second value to list of connected routers
            router_address_and_distance = values[2].split(":")  #splits the address and distance into a list

            new_router = Router(router_name) #initializes the object based on line owner
            router_dictionary[router_name] = new_router #adds it to the dictionary with name as key and object as value

            for item in router_friends_as_list: #iterates through the connected devices of the router of this line
                if item not in router_dictionary and item != "":    #if the item is not in the dictionary
                    new_router = Router(item)                       #it initializes it
                    router_dictionary[item] = new_router            # it stores it to the dict
                    router_dictionary[router_name].add_neighbor(router_dictionary[item]) #it takes the line router, and adds the item from the router list as a neighbor
                elif item in router_dictionary and item != "":      #if the item is in the dictionary
                    router_dictionary[router_name].add_neighbor(    # it takes the line router, and adds the item from the router lister as a neighbor
                        router_dictionary[item])

            if len(router_address_and_distance) == 2:
                router_address = router_address_and_distance[0]
                router_distance = int(router_address_and_distance[1])
                router_dictionary[router_name].add_network(router_address, router_distance)

            line = f.readline().strip("\n")


def main():

    router_dictionary = {}
    routerfile = input("Network file: ")

    if routerfile != "":
        readfile(routerfile, router_dictionary)

    while True:
        command = input("> ")
        command = command.upper()

        if command == "P":
            name_to_print = input("Enter router name: ")

            if name_to_print not in router_dictionary:
                print("Router was not found. ")
            else:
                print(router_dictionary[name_to_print].print_router())
        
        elif command == "PA":
            for item in router_dictionary:
                router_dictionary[item].print_router()

        elif command == "S":
            sending_router = input("Sending router: ")
            sending_router = sending_router.upper()
            neighbor_list = router_dictionary[sending_router].return_n_list()
            #senders_address_and_distance = router_dictionary[sending_router].return_r_list()

            for item in neighbor_list: #for each item on the neighbor list
                router_dictionary[item].receive_routing_table(router_dictionary[sending_router])

        elif command == "C":
            router_1 = input("Enter 1st router: ")
            router_2 = input("Enter 2nd router: ")
            router_1 = router_1.upper()
            router_2 = router_2.upper()
            router_dictionary[router_1].add_neighbor(
                router_dictionary[router_2])

        elif command == "RR":
            pass

        elif command == "NR":
            new_name = input("Enter a new name: ")
            if new_name in router_dictionary:
                print("Name is taken.")
            else:
                new_router = Router(new_name)
                router_dictionary[new_name] = new_router

        elif command == "NN":
            router_name = input("Enter router name: ")
            network = input("Enter network: ")
            distance = int(input("Enter distance: "))
            router_dictionary[router_name].add_network(network, distance)

        elif command == "Q":
            print("Simulator closes.")
            return

        else:
            print("Erroneous command!")
            print("Enter one of these commands:")
            print("NR (new router)")
            print("P (print)")  
            print("C (connect)")
            print("NN (new network)")
            print("PA (print all)")
            print("S (send routing tables)")
            print("RR (route request)")
            print("Q (quit)")

main()
