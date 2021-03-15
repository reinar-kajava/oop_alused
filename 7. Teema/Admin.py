from Kasutajad import Kasutajad
from privileegid import Privileegid

class Admin(Kasutajad):
    def __init__(self, e, p, kn, parool):
        super().__init__(e, p, kn, parool)
        self.roll = "administraator"
        self.privileegid = Privileegid()


