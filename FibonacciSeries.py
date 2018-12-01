length = input("How many Fibonacci numbers do you want? ")
length = int(length) + 1
n1 = 0
n2 = 1
print("1. " + str(n2))

for i in range(2, length):
    n3 = n1+n2
    print(str(i) + ". " + str(n3))
    n1 = n2
    n2 = n3






