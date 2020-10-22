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
##Primjer 6 od 10: loop.py
##
##See LICENSE.txt for license details.

while 1:
    print("добродошли у програм")
    x = input("prvi broj: ")
    o = input("radnja: ")
    y = input("drugi broj: ")
    print("\n\ntreba da izracunamo: " + x + o + y )
    x=int(x)
    y=int(y)
    if o == "+":
        print("zbir: " + str(x+y))
    elif o == "-": print("razlika: " + str(x-y))
    elif o == "*": print("proizvod: " + str(x*y))
    elif o == ":": print("kolicnik: " + str(x/y))
    else: print("Neispravna radnja!")
    izlaz = input("Kraj?\t")
    if izlaz == "d" or izlaz == "D":
        print("\n=============================")
        break
