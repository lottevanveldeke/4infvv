Prijs = float(input("hoeveel euro betaalde je voor je zonnepanelen? :"))
premie = Prijs * 0.20
if premie > 600:
    premie = 600
print(f"Je krijgt een premie van {premie} euro.")