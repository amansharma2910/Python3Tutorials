class Animal:
    def __init__(self, birth_type = "unknown", appearance = "unknown", blood_type = "unknown"):
        self.birth_type = birth_type
        self.appearance = appearance
        self.blood_type = blood_type

    @property
    def birth_type(self):
        return self.__birth_type

    @birth_type.setter
    def birth_type(self, birth_type):
        self.__birth_type = birth_type

    @property
    def appearance(self):
        return self.__appearance

    @appearance.setter
    def appearance(self, appearance):
        self.__appearance = appearance

    @property
    def blood_type(self):
        return self.__blood_type

    @blood_type.setter
    def blood_type(self, blood_type):
        self.__blood_type = blood_type

    def __str__(self):
        return "A {} is {} and it looks {} and has {} blood type.".format(type(self).__name__, self.birth_type, self.appearance, self.blood_type)


class Mammal(Animal):

    def __init__(self, birth_type = "born alive", appearance = "furry", blood_type = "warm", nurse_young = True):
        Animal.__init__(self, birth_type, appearance, blood_type)
        self.nurse_young = nurse_young

    @property
    def nurse_young(self):
        return self.__nurse_young

    @nurse_young.setter
    def nurse_young(self, nurse_young):
        self.__nurse_young = nurse_young

    def __str__(self):
        return super().__str__() + " and it is {} they nurse their young.".format(self.nurse_young)


class Reptile(Animal):

    def __init__(self, birth_type="born from egg", appearance="scaly", blood_type="cold", nurse_young=False):
        Animal.__init__(self, birth_type, appearance, blood_type)
        self.nurse_young = nurse_young

    @property
    def nurse_young(self):
        return self.__nurse_young

    @nurse_young.setter
    def nurse_young(self, nurse_young):
        self.__nurse_young = nurse_young

    def __str__(self):
        return super().__str__() + " and it is {} they nurse their young.".format(self.nurse_young)

def main():

    crocodile = Reptile()
    print(crocodile)

main()