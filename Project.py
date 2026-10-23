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
