from kasutaja import Kasutajad
class Admin(Kasutajad):
    def __init__(self, e, p, kn, parool):
        super().__init__(e, p, kn, parool)
        self.roll = "admin"
        self.privileegid = Privileegid()

class Privileegid():
    def __init__(self):
        self.privileegid = ["Kasutajate lisamine", "Kasutajate eemaldamine", "Kasutajate blokeering"]

    def naita_privileegid(self):
        print("Admini privileegid")
        for privileeg in self.privileegid:
            print(privileeg)