#task1
import math
def degtorad(deg):
    rad=(deg*math.pi)/180
    return round(rad,6)
deg=int(input("Input degree: "))
print("Output radian:",degtorad(deg))

#task2
def area(h,a,b):
    area=0.5*(a+b)*h
    return float(area)
h=int(input("Height: "))
a=int(input("Base, first value: "))
b=int(input("Base, second value: "))
print("Expected Output:",area(h,a,b))

#task3
def areapoly(numside,lenside):
    area=0.25*(lenside**2)*numside
    return int(area)


numside=int(input("Input number of sides: "))
lenside=int(input("Input the length of a side: "))
print("The area of the polygon is:",areapoly(numside,lenside))

#task4
def areaparallelogram(lengthbase,heightside):
    area=lengthbase*heightside
    return float(area)
lengthbase=int(input("Length of base: "))
heightside=int(input("Height of parallelogram: "))
print("Expected Output:",areaparallelogram(lengthbase,heightside))
