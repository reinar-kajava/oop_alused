class Kasutajad():
    def __init__(self, e, n, kn, p):
        self.eesnimi = e
        self.perenimi = n
        self.kasutajanim = kn
        self.parool = p
        self.roll = "tavakasutaja"

    def kasutaja_kirjeldus(self):
        print("Eesnimi: " + str(self.eesnimi))
        print("Perekonnanimi: " + str(self.perenimi))
        print("Kasutajanimi:" + (self.kasutajanim))
        print("Parool: " + str(self.parool))
        print("Kasutaja roll on " + str(self.roll))



    def kasutaja_tervitus(self):
        print("Tervist, " + str(self.kasutajanim) + " teie roll on " + str(self.roll))
