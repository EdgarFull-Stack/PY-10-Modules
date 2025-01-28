# 1 Task
import random

random_number = random.randint(1,100)
print(f'Random number from 1 to 100 is: {random_number}')

#  2 Task
random_number1 = random.uniform(1,50)
print(f'Random uniform number from 1 to 50 is: {random_number1}')

#  3 Task
#1.
from random import randint, choice

random_number = randint(1,10)
print(random_number)

#2.
random_fruit = choice(['obuolys','bananas','kriaušė','vyšnia'])
print(random_fruit)

#  4 Task
import datetime as dt
current_time = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(current_time)

#  5 Task
from math import sqrt as sq
print(sq(625))

#  6 Task
from math import *
print(sin(radians(90)))
# 1. Naudojant 'from math import *', importuojamos visos modulio funkcijos ir konstantos,
#    kas gali sukelti vardų konfliktus dideliuose projektuose, ypac jei naudojami keli moduliai.
# 2. Sunku suprasti, kurios funkcijos priklauso moduliui, nes nera aiskaus rysio (pvz., 'math.sin').








