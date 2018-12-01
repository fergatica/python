mood = input('How do you feel? (1-10) ')

mood = int(mood)

if mood <= 7 and mood >=4:
    print("A suitable smiley would be :-|")

elif mood > 7 and mood < 10:
    print("A suitable smiley would be :-)")

elif mood > 1 and mood < 4:
    print("A suitable smiley would be :-(")

elif mood == 1:
    print("A suitable smiley would be :'(")

elif mood == 10:
    print("A suitable smiley would be :-D")

else:
    print("Bad input!")