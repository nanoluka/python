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
##Primjer 9 od 10: blink.py
##
##Kod preuzet sa: https://realpython.com/arduino-python/
##pa tamo mozete vidjeti sve pratece detalje. U sustini,
##nakon sto spojite Arduino, treba da ,,spustite" StandardPyfirmata
##dostupan u File -> Examples -> Firmata -> StandardFirmata. 
##Kada se tako programira arduino, ovaj kod nize izvrsavate u IDLE,
##samo ne zaboravite da prilagodite port, po potrebi (COM3)
##
##See LICENSE.txt for license details.

import pyfirmata
import time

board = pyfirmata.Arduino('COM3')

while True:
    board.digital[13].write(1)
    time.sleep(2)
    board.digital[13].write(0)
    time.sleep(0.5)
