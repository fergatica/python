import math

purchasePrice = input('Purchase price: ')
paidAmount = input('Paid amount of money: ')

purchasePrice = int(purchasePrice)
paidAmount = int(paidAmount)

change = paidAmount - purchasePrice

if change == 0 or purchasePrice > paidAmount:
    print("No change")

if change >= 1 and purchasePrice < paidAmount:
    print("Offer change:")

if change >= 10:
    tenEuros = math.floor(change/10)
    change = change - (tenEuros*10)
    print(tenEuros, "ten-euro notes")

if change >= 5:
    fiveEuros = math.floor(change/5)
    change = change - (fiveEuros*5)
    print(fiveEuros, "five-euro notes")

if change >= 2:
    twoEuros = math.floor(change/2)
    change = change - (twoEuros*2)
    print(twoEuros, "two-euro coins")

if change >= 1:
    oneEuros = math.floor(change/1)
    change = change - (oneEuros*1)
    print(oneEuros, "one-euro coins")