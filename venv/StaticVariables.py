# Fields or variables that are declared within a class but outside of any method are known as static variables. We will discuss static variables with the help of an example.

class Dog:

    num_of_dogs = 0 # Since num_of_dogs is declared outside any method, it is a static variable.

    def __init__(self, name = "Unknown"):
        self.name = name
        Dog.num_of_dogs += 1

    @staticmethod
    def get_num_of_dogs():
        print("Total number of dogs = {}".format(Dog.num_of_dogs))

def main():
    Teddy = Dog("Teddy")
    Tuffy = Dog("Tuffy")
    Dog.get_num_of_dogs()

main()