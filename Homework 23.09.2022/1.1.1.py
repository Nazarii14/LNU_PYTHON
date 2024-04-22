import random
import math

a = random.uniform(10, 100)
b = random.uniform(10, 100)
c = random.uniform(10, 100)
d = random.uniform(10, 100)
hx = random.uniform(10, 100)
hy = random.uniform(10, 100)

x = a*hx*b
y = c*hy*d

def func1(x, y):
    return (math.sin(x+y)+2*math.cos(x+y))/(x+y) if x+y != 0 else math.exp(x/2) + math.exp(y)

def func2(x, y):
    return (math.pow((x+y), 2) + 5*(x-y) + math.pow(x, 3))/(x-y) if x > y else (2*math.pow((x+y), 2) + math.exp(x-y))/(math.exp(2*x+7*y))

def func3(x, y):
    return (math.sin(x+y) + math.cos(x+y))/(2*x+2*y) if x+y != 0 else math.exp(x/2) + math.exp(y/2)

print(func1(x, y))
print(func2(x, y))
print(func3(x, y))