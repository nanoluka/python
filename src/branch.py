##Prakticni primjeri uz predavanje
##
##Uvod u programski jezik Python kroz prakticne primjere
##
##autora Aleksandar Pajkanovic, nanoluka.org
##
##licenciran je pod 
##Creative Commons Attribution-ShareAlike 4.0 International License.
##
##Ovaj i ostale kodove mozete koristiti (mijenjati i dalje
##upotrebljavati - cak i komercijalno) pod uslovom da
##ovaj tekst zaglavlja ostane nepromijenjen i da tako nastali
##materijal objavite pod istom licencom.
##
##Za detalje o licenci procitajte LICENSE.txt, a ako niste 
##dobili tu datoteku, onda pogledajte na veb stranici:
##  http://creativecommons.org/licenses/by-sa/4.0/
##
##Prateca prezentacija i ostali primjeri su dostupni na:
##  github.com/nanoluka/python
##
##Kontakt:
##  nanolukaorg [at] gmail [dot] znatevec
##
##Primjer 5 od 10: branch.py
##
##See LICENSE.txt for license details.

x = input("prvi broj: ")
r = input("radnja: ")
y = input("drugi broj: ")
x = int(x)
y = int(y)
if r == "+":
    print("sabiram...")
    print("zbir: " + str(x+y))
elif r == "-":
    print("oduzimam...")
    print("razlika: " + str(x-y))
elif r == "*": print("proizvod: " + str(x*y))
elif r == ":": print("kolicnik: " + str(x/y))
else:
    print("Neispravna radnja!")

