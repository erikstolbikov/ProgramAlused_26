from random import *  #randint
from math import *
#Ülesanne 1
print("Tere, maailm!")
nimi=input("Sisesta oma nimi: ")
print(f"Tere, maailm! Tervitan sind {nimi}!")
try:
    vanus=int(input("Sisesta oma vanus: "))
    print(f"Tere, maailm! Tervitan sind {nimi}! Sa oled {vanus} aastat vana.")
except ValueError:
    print("Palun sisesta kehtiv number vanuse jaoks.")


#Ülesanne 2
vanus=18 #int-täisarv
eesnimi="Jaak" #str-sõne
pikkus=16.5 #float-kümnedmurd/ujukomaarv
kas_käib_koolis=True #bool-tõeväärtus
print(f"Vanus:{vanus}, tüüp:{type(vanus)}")
print(f"Eesnimi:{eesnimi}, tüüp:{type(eesnimi)}")
print(f"Pikkus:{pikkus}, tüüp:{type(pikkus)}")
print(f"käib koolis:{kas_käib_koolis}, tüüp:{type(kas_käib_kooli)}")

#Ülesanne 3
kommide_arv=randint(1,100)  #int(input("Kommide arv: "))
print(f"Laual on {kommide_arv} kommi.")
kommid=int(input("Mitu kommi soovid ära võtta? "))
kommide_arv -= kommid
print(f"Laual on nüüd {kommide_arv} kommi.")