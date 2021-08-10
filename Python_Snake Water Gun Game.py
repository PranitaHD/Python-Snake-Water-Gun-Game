"""
Snake Vs Water = Snake wins as Snake drinks Water
Water Vs Gun = Water wins as Gun will drown in Water
Gun Vs Snake = Gun wins as Gun will shoot the Snake
"""

import random

i = 1
Cpoint = 0
Hpoint = 0
Tie = 0

while i<=5 :
    List1 = ["s" , "w" , "g" ]
    Computer = random.choice(List1)
    Human = input("\nChoose 's' for Snake or 'w' for Water or 'g' for Gun : ")

    if Computer == Human :
         print("--> It,s Tie , 0 points to each... ")
         Tie = Tie + 1
         print(f"POINTS : Computer = {Cpoint}  ,  You = {Hpoint}  &  Tie = {Tie}")

    elif (Computer == 's' and Human == 'w') :
        print(f"CHOICES : Computer - {Computer}  &  You - {Human}")
        print("--> Computer wins 1 point")
        Cpoint = Cpoint + 1
        print(f"POINTS : Computer = {Cpoint}  ,  You = {Hpoint}  &  Tie = {Tie}")

    elif (Computer == 'w' and Human == 's') :
        print(f"CHOICES : Computer - {Computer}  &  You - {Human}")
        print("--> You wins 1 point")
        Hpoint = Hpoint + 1
        print(f"POINTS : Computer = {Cpoint}  ,  You = {Hpoint}  &  Tie = {Tie}")

    elif (Computer == 'w' and Human == 'g') :
        print(f"CHOICES : Computer - {Computer}  &  You - {Human}")
        print("--> Computer wins 1 point")
        Cpoint = Cpoint + 1
        print(f"POINTS : Computer = {Cpoint}  ,  You = {Hpoint}  &  Tie = {Tie}")

    elif (Computer == 'g' and Human == 'w') :
        print(f"CHOICES : Computer - {Computer}  &  You - {Human}")
        print("--> You wins 1 point")
        Hpoint = Hpoint + 1
        print(f"POINTS : Computer = {Cpoint}  ,  You = {Hpoint}  &  Tie = {Tie}")

    elif (Computer == 'g' and Human == 's') :
        print(f"CHOICES : Computer - {Computer}  &  You - {Human}")
        print("--> Computer wins 1 point")
        Cpoint = Cpoint + 1
        print(f"POINTS : Computer = {Cpoint}  ,  You = {Hpoint}  &  Tie = {Tie}")

    elif (Computer == 's' and Human == 'g') :
        print(f"CHOICES : Computer - {Computer}  &  You - {Human}")
        print("--> You wins 1 point")
        Hpoint = Hpoint + 1
        print(f"POINTS : Computer = {Cpoint}  ,  You = {Hpoint}  &  Tie = {Tie}")

    else :
        print("--> Invalid Input..!")

    i = i + 1

print("\n* * * * * * * * * * *  Game  Over  * * * * * * * * * * *\n")
if Cpoint == Hpoint :
    print("\t               It's a tie")
elif Cpoint > Hpoint :
    print("\t      Computer wins and You loose")
else :
    print("\t      You win and Computer loose")
print(f"  TOTAL POINTS : Computer = {Cpoint}  ,  You = {Hpoint}  &  Tie = {Tie}\n")
print("\n* * * * * * * * *  Thanks For Playing  * * * * * * * * *\n")