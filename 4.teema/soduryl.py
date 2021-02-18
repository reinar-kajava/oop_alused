from Sodur import Sodur
from random import randint
armee1 = []
armee2 = []
armee3 = []

for kord in range(1, 21, 1):
    armeenr = randint(1, 2)
if (armeenr == 1):
    sodur = Sodur(1)
    armee1.append(sodur)
if (armeenr == 2):
    sodur = Sodur(2)
    armee1.append(sodur)
print(armee1)
for sodur in armee1:
    sodur.info()
print("-----------------------------")
print(armee2)
for sodur in armee2:
    sodur.info()