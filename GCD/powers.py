import random
import math

num1=random.randint(1,50)
num2=random.randint(1,50)

print("The random numbers are", num1, "and", num2)

gret=math.gcd(num1, num2)

print("The greatest common divisor is", gret)

pwr=math.pow(gret, 2)
print("The GCD of the power value is", pwr)