class Ristkylik():
    def __init__(self, l, k, s):
        self.laius = int(l)
        self.korgus = int(k)
        self.symbol = str(s)
    def __str__(self):
        ruut = []
        for i in range (self.korgus):
            ruut.append(self.symbol * self.laius)
        ruut = '\n'.join (ruut)
        return ruut
    def __add__(self, teineristkylik):
        uuslaius = self.laius + teineristkylik.laius
        uuskorgus = self.korgus + teineristkylik.korgus
        uussymbol = self.symbol
        return Ristkylik(uuslaius, uuskorgus, uussymbol)