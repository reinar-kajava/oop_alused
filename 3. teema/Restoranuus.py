class Restoranuus():
    def __init__(self, nim, soogi_tyyp):
        self.restorani_nimi = nim
        self.soogi_tyyp = soogi_tyyp
        print("Restoran nimega {} mis pakub {} on avatud!".format(self.restorani_nimi, self.soogi_tyyp))
    def restorani_kirjeldus(self):
        print("Restoranuus" + str(self.restorani_nimi) + ", söögi tüüp " + str(self.soogi_tyyp))

    def ava_restoran(self):
        print("Restoran on avatud")
