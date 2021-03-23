from Restoranuus import Restoraan
from Jaatisekiosk import Kiosk
restoran1 = Restoraan("McDonalds", "kiirtoitu")
restoran1.restoraani_kirjeldus()
restoran1.ava_restoraan()


kiosk = Kiosk("Karila", "Jäätis")
jaatise_valik = ["vanilla", "mustika", "maasika"]
kiosk.restoraani_kirjeldus()
kiosk.ava_restoraan()
kiosk.lisaJaatisValikusse("vanilla")
kiosk.lisaJaatisValikusse("Maasika")
kiosk.lisaJaatisValikusse("Mustika")