class Test():
    loendur = 0
    def __init__(self):
        Test.loendur += 1
    def __del__(self):
        Test.loendur -= 1

a = Test()
b = Test()
print("Kokku on objekte " +  str(Test.loendur))

del a
print("kokku on objekte "  + str(Test.loendur))