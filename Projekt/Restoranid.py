"""Fail, mis sisaldab klasse mida kasutatakse peafailis"""
class Restoran():
    def __init__(self, n, t):
        self.restorani_nimi = n
        self.soogi_tyyp = t
    # meetodid
    def restorani_kirjeldus(self):
        print("Restoran nimega " + str(self.restorani_nimi) + ", mis pakub " + str(self.soogi_tyyp))


    def ava_restoran(self):
        print("Restoran on avatud!")

class Kiosk():
    def __init__(self, n, t):
        self.kioski_nimi = n
        self.jaatise_tyyp = t
    def kioski_kirjeldus(self):
        print("Jäätisekiosk nimega " + str(self.kioski_nimi) + ", mis pakub järgnevaid jäätisetüüpe " + str(self.jaatise_tyyp))


    def ava_kiosk(self):
        print("Kiosk on avatud")



