import math
import random

side1=random.randint(1,20)
side2=random.randint(1,20)
side3=random.randint(1,20)

print("Sides are ", side1, side2, side3)

area=(side1+side2+side3)/2

print("Area of the triangle is: ", area)

sarea=(side1*side2)
print("Area of a square is ", sarea)

seed=math.seed(1,10)
print("The seed is ", seed)