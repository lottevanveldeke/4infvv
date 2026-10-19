getal1 = float(input("geef een eerste getal : ")) #Float maakt het een kommagetal
getal2 = float(input("geef een tweede getal : "))
bewerking = input("welke bewerking wil je uitvoeren? (+,-,/,*,** 2): ")

if bewerking == "+": #== : is gelijk aan ; <= : kleiner dan en gelijk aan ; < : kleiner dan; != : Niet gelijk aan 
    print(f"{getal1} + {getal2} = {getal1+getal2}.")

if bewerking == "-":
    print(f"{getal1} - {getal2} = {getal1-getal2}.")

if bewerking == "/":
    print(f"{getal1} / {getal2} = {getal1/getal2}.")

if bewerking == "*":
    print(f"{getal1} * {getal2} = {getal1*getal2}.")

if bewerking == "**":
    print(f"{getal1} ** {getal2} = {getal1**getal2}.")