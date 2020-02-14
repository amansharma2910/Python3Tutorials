# In this example, let us discuss how to create custom exceptions. For this, first we need to create a class with the name of our exception. Since this is going to be an exception, we will be inheriting from the Exception class.

class PetNameError(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

try:
    petName = input("Enter your pet's name: ")
    if any(char.isdigit() for char in petName):
        raise PetNameError
except PetNameError:
    print("Your pet's name can't contain digits. Try again.")