
import random
# Example
atsitiktinis_skaicius = random.randint(1,10)
print(f'Atsitiktinis nuo 1 iki 10: {atsitiktinis_skaicius}')

# while True:
#     skaicius = int(input('Ar galite atspeti skaiciu? (veskite kol neatspesite) :'))
#     if skaicius == random.randint(1,10):
#         break

# Example spec functions
from random import randint, choice

random_number = randint(1,10)
print(random_number)

random_month = choice(['sausis','vasaris','kovas'])
print(random_month)

# Example
import random as rn
atsitiktinis_skaicius = rn.randint(1,10)
print(f'Atsitiktinis nuo 1 iki 10: {atsitiktinis_skaicius}')

# Example alias
from random import  randint as rnt
random_number = rnt(1,10)
print(random_number)

# Example that is not recommended to use
from random import*
parinktis = sample(['sausis','vasaris','kovas'], k=3)
print(parinktis)

# Example from our created modules (aritmetikosmodulis.py)
import aritmetikosmodulis as am

res = am.dalink(9, 3)
print(res)

res = am.daugink(9, 3)
print(res)

res = am.atimk(9, 3)
print(res)

res = am.sumuok(9, 3)
print(res)

