from kuju import Kuju
class ring(Kuju):
    def __init__(self, r):
        self.raadius = r
        self.pi = 3.14

    def pindala(self):
        return  self.raadius * self.raadius * self.pi
