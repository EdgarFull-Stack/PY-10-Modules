# 1
import moduliai.aritmetika
print(moduliai.aritmetika.atimtis(20,5))
print(moduliai.aritmetika.dalyba(20,5))
# 2
from moduliai.aritmetika import atimtis, dalyba
print(atimtis(50,25))
print(dalyba(100,4))
# 3
import moduliai.aritmetika as ar
print(ar.atimtis(30,10))
print(ar.dalyba(50,5))
# 4
import moduliai
moduliai.aritmetika.atimtis(15, 5)