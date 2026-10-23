print("Tere, maailm!")
nimi=input("Sisesta oma nimi: ")
print(f"Tere, maailm! Tervitan sind {nimi}!")
try:
    vanus=int(input("Sisesta oma vanus: "))
    print(f"Tere, maailm! Tervitan sind {nimi}! Sa oled {vanus} aastat vana.")
except ValueError:
    print("Palun sisesta kehtiv number vanuse jaoks.")



vanus=18 #int-täisarv
eesnimi="Jaak" #str-sõne
pikkus=16.5 #float-kümnedmurd/ujukomaarv
kas_käib_koolis=True #bool-tõeväärtus