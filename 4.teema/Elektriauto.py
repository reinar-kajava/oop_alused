from Auto import Auto
class Elektriauto(Auto):
    def __init__(self, t, m, a):
        super().__init__(t, m, a)
        self.akusuurus = 50

    def aku_kirjeldus(self):
        print("Antud auto sisaldab " + (str(self.akusuurus) + "patareid"))
    def tangi(self, l):
        print("auto ei vaja tankimist")