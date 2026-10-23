# kirjuta enda esimene programm, mis väljastab käsureale teksti:
#     "tere, maailm!"
# küsi kasutaja nimi ja muuda tekst, et ta näeks väalja nii:
#     "Tere, maailm! tervitan sind mati", kui kasutaja nimi on mati.
# küsi kasutajalt sisend tema vanuse kohta ning väaljasta see ekraanile:
# "Tere, maailm! tervetan sind mäati! sa oled N aastat vana."
#Ülesanne1
print("tere, maalm!")
nimi=input("sisesta ome nimi: ")
print(f"Tere, maailm! Tervitan sind {nimi}!")
try:
    vanus=int(input("sisesta oma vanus: "))
    print(f"Tere, maailm! Tervitan sind {nimi}! sa oled {vanus} aastat vana.")
except ValueError:
    print("Palun sisesta kehtiv number vanuse jaoks.")

    #ülesanne 2
# on järnevad muutujad:
#a) vanus = 18
#b) eesnimi = "jaak"
#c) pikkus = 16.5
#d) kas_käib_koolis = True
# mis võimalus veel peale True oleks viimast muutujat väärtustada?
# kuidas võiks nende muutujate vääartusi koodis kontrollida?
# kirjuta kood tüüpide kontrollimiseks.
vanus=18 #int-täisarv
eesnimi="jaak" #str-sõne
pikkus=16.5 #float-kümnendaurd!
kas_käib_koolis=True #bool-töeväärtus
print(f"Vanus:{vanus}, tüüp:{type(vanus)}")
print(f"Eesnim:{eesnimi}tüüp:{type(eesnimi)}")
print(f"Pikkus: {pikkus}, tüüp:{type(pikkus)}")
print(f"Käib koolis:{kas_käib_koolis}, tüüp:{type(kas_käib_koolis)}")

#Ülesanne 3
import math
# Kirjuta enda koodis laual olevate kommide arv muutujasse
# (kommide arv on juhuslik).
# Seejärel kuva muutujas olev kommide arv ekraanile kasutades print()
# Küsi kasutajalt sisendit, mitu kommi ta soovib laualt ära võtta.
# Eemalda soovitud kommide arv laual olevate kommide arvust
# ja kuva ekraanile.
# kui palju komme laual nüüd on.
from random import * #randit
kommide_arv=randint(1, 100) #int(input("kommide arv: "))
kommide_arv=int(input("Kommide arv: "))
print(f"Laud on {kommide_arv} kommi.")
kommid=int(input("Mitu kommi soovid ära võtta? "))
kommide_arv -= kommid
print(f"Laid on nüüd {kommide_arv} kommi.")

#Ülesanne 4
#Puu läbimõõdu arvutamine
# kirjuta programm, mis küsib kasutaja käest puu ümbermõõdu
# ning teatab selle peale puu läbimõõdu.
ümbermõõt=float(input("Sisesta puu ümbermõõt: "))
läbimõõt=ümbermõõt/math.pi
print(f"Puu läbimõõt on {läbimõõt}.")

#Ülesanne 5
#Arvutage Pythoni käsureal, kui pikk on ristkülikukujulise
#maatüki diagonaal,
#mille mõõtmed on Nm x Mm. N ja M küsi kasutajalt.
N=float(input("Sisesta ristküliku esimene külg (N): "))
M=float(input("Sisesta ristküliku teine külg (M): "))

diagonaal=round(math.sqrt(N**2 + M**2), 1) # sqrt() math moodulist
print(f"Ristküliku diagonaal on {diagonaal}.")
except ValueError:
print("Palun sisesta kehtiv number.")

#Ülesanne 7
#Koostada programm, mis arvutab aritmeetilise keskmise
# suvalisest etteantud 5 täis arvust.
#Leia nende arvude summa, jagatuna kasutaja poolt sisestatud arvuga,
#täisarvuline osa ja jääk.
arv1=randint(1, 100)
arv2=randint(1, 100)
arv3=randint(1, 100)
arv4=randint(1, 100)
arv5=randint(1, 100)
summa=arv1+arv2+arv3+arv4+arv5
keskmine=summa/5
print(f"summa: {summa}, Keskmine: {keskmine}")
try:
    Jagaja=int(input("Sisesta arv, millega jagada: "))
    tulemus=sumna/jagaja
    print("Tulenus:", tulemus) #tulemus=3.75
    print("Taisarvuline osa:", Int(tulemus))
    #int(3.75)=3 teine variant täisosa leidmiseks on kasutada // jagam print(®Jääk:", sunma % jagaja)
except ValueError:
    print("Palun sisesta kehtiv number.")