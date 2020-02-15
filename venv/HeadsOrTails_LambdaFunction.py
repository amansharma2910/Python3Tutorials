import random

coinTossList = [random.choice(['T','H']) for i in range(100)]
Tcounter = lambda list: list.count('T')
Hcounter = lambda list: list.count('H')
print("Heads : {}\nTails : {}".format(Hcounter(coinTossList), Tcounter(coinTossList)))
