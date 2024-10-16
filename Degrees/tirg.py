import random
import math

angle1=random.randint(0,360)
print("The random angle is", angle1)

rads=math.radians(angle1)
print("The radian degree is: ", round(rads))

sinv=math.sin(rads)
cosv=math.cos(rads)
tanv=math.tan(rads)

print("The sine, cos, and tan values are: ", sinv, cosv, tanv)