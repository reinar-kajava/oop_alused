class Kasutaja():
    # contruct
    def __init__(self, passwd, kn):
        self.__password = passwd
        self.kasutajanimi = kn
    # getter
    def saadapasswd(self):
        return self.__password
    # setter
    def maarapasswd(self, salason):
        self.__password = salason


kasutajapass = Kasutaja("qwerty", "user")
print(kasutajapass.saadapasswd())
# yhendusWEBmasinaga.__ip = "192.168.23.12" - ei tööta, valesti
kasutajapass.maarapasswd("qwerty") # õige, töötab
print(kasutajapass.saadapasswd())