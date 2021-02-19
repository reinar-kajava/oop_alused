from kuju import Kuju
class Kolmnurk(Kuju):
    def __init__(self, ap, h):
        self.aluspikkus = ap
        self.kyrgus = h

    def pindala(self):
        return 0.5 * self.aluspikkus * self.kyrgus
