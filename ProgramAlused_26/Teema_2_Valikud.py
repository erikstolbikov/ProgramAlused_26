# Lihtne 1t

x = -5  # testimiseks kirjuta siia mõni arv

try:
    x = int(input("Sisesta täisarv: "))

    if x > 0:
        print("Positiivne arv")
        print("See rida on ka if-i sees")

    print("See rida täidetakse alati")

except ValueError:
    print("Palun sisesta kehtiv täisarv.")


# if-else

x = int(input("Sisesta arv: "))

if x == 1:
    print("Õige")
else:
    print("Vale")


vastus = input("Kas soovid jätkata? (jah/ei) ")

if vastus.lower() == "jah":
    print("Jätkame!")
elif vastus.lower() == "ei":
    print("Head aega!")
else:
    print("Palun sisesta 'jah' või 'ei'.")


# if..... elif..... else

try:
    x = int(input("Sisesta arv -5 kuni 5: "))

    if x < -5:
        print("Vähe")
    elif -5 <= x <= 5:
        print("OK")
    else:
        print("Palju")

except ValueError:
    print("Palun sisesta kehtiv täisarv.")

# if on if´i sees

try:
    vanus = int(input("Vanus: "))
    if vanus >= 18:
        juhiluba = input("Kas sul on juhiluba? (jah/ei) ")

        if juhiluba.lower() == "jah":
            print("Võid autot juhtida.")
        else:
            print("Kõigepealt tee juhiload.")
    else:
        print("Oled autojuhtimiseks liiga noor.")

except ValueError:
    print("Palun sisesta kehtiv täisarv.")