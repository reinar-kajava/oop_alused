class Koer():
    def __init__(self, hyydnim, vanus = 0):
        self.hyydnimi = hyydnim
        self.vanus = vanus
        self.saba = True
        self.jalad = True
        #print("Koer nimega" + self.hyydnimi + "on" + str.(self.vanus))
        print("Koer nimega {} on {} aastat vana".format(self.hyydnimi, self.vanus, self.jalad))

    def __del__(self):
        if(self.vanus > 16):
            print("Kahjuks koera pole enam")

