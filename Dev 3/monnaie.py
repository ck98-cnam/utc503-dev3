class monnaie:
    valeur = 0
    _paper = ('1000', '5000', '10000', '20000', '50000', '100000')
    _coin  = ('250', '500')
    def __init__(self, valeur):
        self.valeur = valeur
        print("constructor")

    def rendreMonnaie(self, value):
        ret = value / _paper[5]

mon = monnaie(5)
mon._paper