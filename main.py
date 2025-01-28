
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

# Example alias
import random as rn
atsitiktinis_skaicius = rn.randint(1,10)
print(f'Atsitiktinis nuo 1 iki 10: {atsitiktinis_skaicius}')