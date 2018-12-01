def print_in_accordance_of_values(english_spanish):
    sorted_eng_spa = sorted(english_spanish.items(), key=lambda x: x[1])
    a = 0
    for i in sorted_eng_spa:
        print(sorted_eng_spa[a][1], sorted_eng_spa[a][0])
        a += 1


english_spanish = {"hi": "hola", "thanks": "gracias", "yes": "si", "no": "no"}

print_in_accordance_of_values(english_spanish)