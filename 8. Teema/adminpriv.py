from kasutaja import Kasutajad
class Admin(Kasutajad):
    def __init__(self, e, n, kn, p):
        super().__init__(e, n, kn, p)

class Privileegid():
    def __init__(self):
        self.privileegid = ["Kasutajate lisamine", "Kasutajate eemaldamine", "Kasutajate blokeerimine"]
