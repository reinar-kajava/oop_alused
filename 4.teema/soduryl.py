from Sodur import Sodur
from random import randint
armee1 = []
armee2 = []
armee3 = []

for kord in range(1, 21, 1):
    armee_nr = randint(1, 2)
    if(armee_nr == 1):
        sodur = Sodur(1)
        armee1.append(sodur)
    if (armee_nr == 2):
        sodur = Sodur(2)
        armee2.append(sodur)
# väljastame armeede sisu
print("Armee 1")
for sodur in armee1:
    sodur.info()
print("-------------------------")
print("Armee 2")
for sodur in armee2:
    sodur.info()
