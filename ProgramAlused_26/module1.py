nimi = input("Sisesta eesnimi: ")

if nimi.lower() == "juku":
    print("Lähme Jukuga kinno!")

    if nimi.isupper():
        print("Ära karju, Juku!")

    vanus_tekst = input("Sisesta Juku vanus: ")

    if vanus_tekst.isdigit():
        vanus = int(vanus_tekst)

        if vanus > 100:
            print("Viga andmetes!")
        elif vanus < 6:
            print("Pilet: tasuta")
        elif vanus <= 14:
            print("Pilet: lastepilet")
        elif vanus <= 65:
            print("Pilet: täispilet")
        else:
            print("Pilet: sooduspilet")

    elif vanus_tekst.startswith("-") and vanus_tekst[1:].isdigit():
        print("Viga andmetes!")
    else:
        print("Viga: vanus peab olema täisarv!")

else:
    print("Täna kinno ei minda.")


nimi1 = input("Esimese inimese nimi: ").capitalize()
nimi2 = input("Teise inimese nimi: ").capitalize()

if nimi1.isalpha() and nimi2.isalpha():
    if nimi1[0] == nimi2[0]:
        print("Nad on täna pinginaabrid!")
    else:
        print("Nad ei ole täna pinginaabrid.")
else:
    print("Viga: nimed võivad sisaldada ainult tähti!")


pikkus = float(input("Toa pikkus: "))
laius = float(input("Toa laius: "))

if pikkus <= 0 or laius <= 0:
    print("Vigased mõõdud!")
else:
    pindala = pikkus * laius
    print("Pindala:", round(pindala, 2), "m²")

    vastus = input("Kas soovid remonti teha? ").lower()

    if vastus == "jah":
        hind = float(input("Materjali hind m² kohta: "))
        kokku = pindala * hind

        tegija = input("Ise või professionaal? ").lower()

        if tegija == "professionaal":
            too = float(input("Töö hind m² kohta: "))
            kokku = kokku + pindala * too
            print("Koguhind:", round(kokku, 2), "€")

        elif tegija == "ise":
            print("Koguhind:", round(kokku, 2), "€")
        else:
            print("Vigane vastus!")


hind = float(input("Sisesta alghind: "))

if hind > 700:
    hind = hind * 0.70

print(f"Lõplik hind: {hind:.2f} €")


try:
    temperatuur = float(input("Sisesta temperatuur: ").replace(",", "."))

    if temperatuur > 18:
        print("Temperatuur on üle 18 kraadi.")
    else:
        print("Temperatuur ei ole üle 18 kraadi.")

except ValueError:
    print("Viga: sisesta arv!")


# Alla 165 cm: lühike
# 165-185 cm: keskmine
# Üle 185 cm: pikk

pikkus = float(input("Sisesta pikkus cm: "))

if pikkus <= 0:
    print("Vigane pikkus!")
elif pikkus < 165:
    print("Lühike")
elif pikkus <= 185:
    print("Keskmise pikkusega")
else:
    print("Pikk")


# Mehed: alla 170 lühike, 170-185 keskmine, üle 185 pikk
# Naised: alla 160 lühike, 160-175 keskmine, üle 175 pikk

pikkus = float(input("Sisesta pikkus cm: "))
sugu = input("Sisesta sugu: ").lower()

if pikkus <= 0:
    print("Vigane pikkus!")

elif sugu == "m" or sugu == "mees":
    if pikkus < 170:
        print("Lühike")
    elif pikkus <= 185:
        print("Keskmise pikkusega")
    else:
        print("Pikk")

elif sugu == "n" or sugu == "naine":
    if pikkus < 160:
        print("Lühike")
    elif pikkus <= 175:
        print("Keskmise pikkusega")
    else:
        print("Pikk")

else:
    print("Viga: tundmatu sugu!")


import random

tooted = ["piim", "sai", "leib", "juust", "õunad"]
ostud = []
kogusumma = 0

for toode in tooted:
    hind = round(random.uniform(0.5, 3), 2)
    print(toode, "-", hind, "€")

    vastus = input("Kas soovid osta? ").lower()

    if vastus == "jah":
        kogus_tekst = input("Mitu tükki? ")

        if kogus_tekst.isdigit() and int(kogus_tekst) > 0:
            kogus = int(kogus_tekst)
            summa = kogus * hind

            ostud.append([toode, kogus, hind, summa])
            kogusumma = kogusumma + summa
        else:
            print("Vigane kogus!")


print("\n--- TÐEKK ---")

for ost in ostud:
    nimi, kogus, hind, summa = ost
    print(f"{nimi}: {kogus} x {hind:.2f} € = {summa:.2f} €")

print(f"KOKKU: {kogusumma:.2f} €")


a = float(input("Esimene külg: "))
b = float(input("Teine külg: "))
c = float(input("Kolmas külg: "))
d = float(input("Neljas külg: "))

if a <= 0 or b <= 0 or c <= 0 or d <= 0:
    print("Viga: küljed peavad olema positiivsed!")
elif a == b == c == d:
    print("See saab olla ruut!")
else:
    print("See ei saa olla ruut.")


a = float(input("Esimene arv: "))
b = float(input("Teine arv: "))
tehe = input("Vali tehe (+, -, *, /): ")

if tehe == "+":
    print("Tulemus:", a + b)

elif tehe == "-":
    print("Tulemus:", a - b)

elif tehe == "*":
    print("Tulemus:", a * b)

elif tehe == "/":
    if b == 0:
        print("Nulliga ei saa jagada!")
    else:
        print("Tulemus:", a / b)

else:
    print("Viga: tundmatu tehtemärk!")


from datetime import date

sunniaasta = int(input("Sisesta sünniaasta: "))
aasta = date.today().year

vanus = aasta - sunniaasta

if vanus < 0:
    print("Vigane sünniaasta!")
else:
    print("Sel aastal saad", vanus, "aastaseks.")

    if vanus % 10 == 0:
        print("See on juubel!")
    else:
        oodata = 10 - vanus % 10
        print("Järgmise juubelini on", oodata, "aastat.")


hind = float(input("Sisesta hind: "))

if hind < 0:
    print("Vigane hind!")
elif hind <= 10:
    hind = hind * 0.90
    print(f"Lõplik hind: {hind:.2f} €")
else:
    hind = hind * 0.80
    print(f"Lõplik hind: {hind:.2f} €")


sugu = input("Sisesta sugu: ").lower()

if sugu == "naine" or sugu == "n":
    print("Sa ei sobi meeskonda.")

elif sugu == "mees" or sugu == "m":
    vanus = int(input("Sisesta vanus: "))

    if 16 <= vanus <= 18:
        print("Sa sobid meeskonda!")
    else:
        print("Sa ei sobi meeskonda.")

else:
    print("Viga: tundmatu sugu!")


inimesed_tekst = input("Mitu inimest? ")
kohad_tekst = input("Mitu kohta bussis? ")

if inimesed_tekst.isdigit() and kohad_tekst.isdigit():
    inimesed = int(inimesed_tekst)
    kohad = int(kohad_tekst)

    if inimesed > 0 and kohad > 0:
        busse = inimesed // kohad
        viimases = inimesed % kohad

        if viimases > 0:
            busse = busse + 1
        else:
            viimases = kohad

        print("Vaja on", busse, "bussi.")
        print("Viimases bussis on", viimases, "inimest.")

    else:
        print("Arvud peavad olema positiivsed!")

else:
    print("Viga: sisesta täisarvud!")