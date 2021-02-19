from kuju import Kuju


class Ruut(Kuju):
    def __init__(self, kp):
        self.kyljepikkus = kp
    def pindala(self):
        return self.kyljepikkus * self.kyljepikkus

