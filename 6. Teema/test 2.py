class Password():
    def __init__(self, vaartus):
        self.omadus1 = vaartus
    def __setattr__(self, attribuut, vaartus):
        if attribuut == "omadus1":
            self.__dict__[attribuut] = vaartus
        else:
            raise AttributeError
a = Password(10)
a.omadus2 = 30
print(a.omadus1, a.omadus2)