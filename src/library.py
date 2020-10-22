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
##Primjer 7 od 10: library.py
##
##See LICENSE.txt for license details.

import random

broj = input("Koliko kockica?\n")
brStrana = input("Koliko strana?\n")
broj = int(broj)
brStrana = int(brStrana)

ponovo = "d"
while ponovo == "d" or ponovo == "D":
    print("Bacam kockicu...")
    for i in range(broj):
        print("Kockica " + str(i+1) + ": " + str(random.randint(1,brStrana)))
    ponovo = input("Ponovo?\n")
