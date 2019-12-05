 # Generally, floating point values are not accurate. Therefore, we use decimal function imported from the decimal module for precision handling in python.

 # You can either import the entire decimal module, or you can jus imprt the Dicimal function from the decimal module using— from decimal inport Decimal
 # To import the entire module, use— imprt decimal
 # Another method to import all the functions within the decimal module is— from decimal import *

 # The following is the example on how we use the decimal function.
 # Instead of writing the name of a function again and again, we can provide it with an easy to use alias. However, this might not be a very good approach if you are working on a shared project because it might reduce the understandability of the code. On the other hand, for individual projects, where you dont require anyoone else to read your code, you can provide as much aliases as you want ot the function used within the code, as long as you can understand them as well. Here's an example to provide alias to a function— from decimal import Decimal as D

from decimal import Decimal

num= Decimal(0)
num+= Decimal("0.000000000111111000")
num+= Decimal("1.000012034000000000")
print("Value after summation = {}".format(num))
num-= Decimal("1.000012034111111")
print("Value after subtraction = {}".format(num))
