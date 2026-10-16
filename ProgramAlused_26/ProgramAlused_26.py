print("Hello, \nWorld!") # 2 rida
print("tere tulemast\t!")

#Paremetrid sep ja end
print() #see on tühi rida
print("õpin",1,".kursusel",sep="***") #sep="" tähendab, et tühikut ei ole
print("2026", "10", "01", sep="/")
print("Sama ", end="") #end="" tähendab, et reavahetust ei ole end="\n"
print("rida")

#Muutujad
nimi = "Python" #str ehk sõne
print("tere,", nimi)
kursus=1
print("õpin",1,".kursusel")

# input() funktsioon
nimi = input("Sisesta oma nimi: ") #programm küsib ja ootab kasutaja sisestust
print("tere,", nimi)
kursus=int(input("sisesta kursuse number: ")) #teisendab sõne arvuks
print("õpin",kursus,".kursusel")
print("Järgmisel aastan õpin ",kursus+1,".kursusel")
 #kursus+1 tähedab,et kursuse number suureneb 1 võrra")

print("Lahutamine")
a =float( input("Esimene arv: "))
b =float(input("Teine arv: "))
print(a,"+",b,"=",a + b)

print("Liitmine")
a =float( input("Esimene arv: "))
b =float(input("Teine arv: "))
print(a,"-",b,"=",a - b)
# tee ka ise korrutamine ja jagamine

print("Jagamine")
a =float( input("Esimene arv: "))
b =float(input("Teine arv: "))
print(a,"/",b,"=",round(a / b,2))
print("Ümardatud arv:",round(a / b,2))

nimi = "erik"
punktid = 87
print(f"{nimi} sai {punktid} punkti.")

a =float(input("Esimene arv: "))
tehe=input("tehe: ")
b =float(input("Teine arv: "))

print(f"{a} {tehe} {b} = {eval(f'{a} {tehe} {b}')}")
import math

print("Pii väärtus:", math.pi)
print("√16 =", math.sqrt(16))
print("sin(π/2) =", math.sin(math.pi / 2))
print("sin(30°) =", round(math.sin(math.radians(30)), 2))
print("5! =", math.factorial(5))