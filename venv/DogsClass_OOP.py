class Dogs:
    def __init__(self, name = "", height = 0, weight = 0):
        self.name = name
        self.height = height
        self.weight = weight

    def bark(self):
        print("{} the dog barks.".format(self.name))

    def eat(self):
        print("{} the dog eats.".format(self.name))

    def sleep(self):
        print("{} the dog sleeps.".format(self.name))

def main():
    dog1 = Dogs("Teddy", 100, 30)
    dog1.bark()
    dog1.eat()
    dog1.sleep()

main()