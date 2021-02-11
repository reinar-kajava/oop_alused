import random

from Sodur import Sodur

sodur1 = Sodur()
sodur2 = Sodur()
# Valjastame iga soduri tervise vaartuse
print("1. sõduri tervis =" + str(sodur1.tervis))
print("2. sõduri tervis =" + str(sodur2.tervis))
# Võistluse osa
while (sodur1.tervis != 0 or sodur2.tervis != 0):
    soduri_nr = random.randint(1, 2)
    if (soduri_nr == 1):
        print("Esimene lööb teist")
        sodur2.tervis -= 20
    else:
        print("Teine lööb esimest")
        sodur1.tervis -= 20
        print("1. sõduri tervis =" + str(sodur1.tervis))
        if(sodur1.tervis == 0 or sodur2.tervis == 0):
            break
if(sodur1.tervis == 0):
    print("Sõdur 2 on võitnud")
else:
    print("Sõdur 1 on võitnud")
if (sodur1.tervis == 0 and sodur2.tervis == 0):
    print("Keegi ei võitnud")
