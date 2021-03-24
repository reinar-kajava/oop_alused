#Ülesande teemaks on restoranid nende nimed ja menüüd.Autoriteks on Reinar Kajava ja Sirli Anier.
#Programm peab väljastama siis kas ainult restorani või jäätisekioski nimed ja menüü või mõlemate menüüd ja kirjeldused
#Korraga.
#Reaalelus saaksid seda programmi kasutada turistid, et teada mida pakutakse restoranides vms



#Impordib failist 'Restoranid' kõik selle sees olevad klassid.
from Restoranid import *
#Funktsioon mida kasutab menüü, et väljastada valikud mida kasutaja saab programmiga teha.
def menuu():
    print("1 Väljasta restorani nimed ja menüüd")
    print("2 Väljasta jäätisekioski nimed ja menüüd")
    print("3 Väljasta mõlemate nimed ja menüüd")
    valik = int(input("Vali sobilik tegevus: "))
    return valik


#Programmi osa, kus asuvad restoranide ja kioskite nimed mida väljastadakse

restoran1 = Restoran("McDonalds", "kiirtoitu")
restoran2 = Restoran("Pepe´s Bistro", "Itaaliapärast toitu")



kiosk1 = Kiosk("Karelia", "Mustika, Maasika, Vaarika")

#Menüü osa, kus väljastadakse kasutaja poolt valitud asjad. Kasutaja saab valida sobiliku tegevuse
#üleval asuva funktsiooni abil.
while(True):
    valik = menuu()
    if(valik == 1):
        print("--------------------------------")
        restoran1.restorani_kirjeldus()
        restoran1.ava_restoran()
        print("------------------------------")
        restoran2.restorani_kirjeldus()
        restoran2.ava_restoran()
        print("-------------------------------")
    if (valik == 2):
        print("--------------------------------")
        kiosk1.kioski_kirjeldus()
        kiosk1.ava_kiosk()
        print("--------------------------------")
    if (valik == 3):
        print("------Restoranid-------")
        restoran1.restorani_kirjeldus()
        restoran1.ava_restoran()
        restoran2.restorani_kirjeldus()
        restoran2.ava_restoran()
        print("------Jäätisekioskid------")
        kiosk1.kioski_kirjeldus()
        kiosk1.ava_kiosk()
        print("----------------------------")



    if (valik > 3 or valik < 1):
        break


