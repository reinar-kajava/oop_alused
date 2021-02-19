from kuju import Kuju
from ruut import Ruut
from kolmnurk import Kolmnurk

from ring import ring


kuju = Kuju()

ruut = Ruut( 2)

kolmnurk = Kolmnurk ( 4, 2)

ring = ring( 5)


print("Kuju pindala" + str(kuju.pindala))

print ("Ruudu pindala" + str(ruut.pindala()))
print("Kolmnurga pindala" + str(kolmnurk.pindala()))
print("Ringi pindala" + str(ring.pindala()))


print(kuju)
print(ring)
print(kolmnurk)
