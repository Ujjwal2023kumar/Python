import datetime
import random
import math

def Hello():
    print("Hello")
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b
a = lambda b: b * 5
Hello()
print(add(10, 5))
print(sub(10, 5))
print(mul(10, 5))
print(div(10, 5))
print(a(4))

x = datetime.datetime.now()
print(x)

y = datetime.datetime(2005,6,14)
print(y.strftime("%a"))

l = ["heads", "tails"]
print(random.randint(1,10))
print(random.choice(l))
print(max(1,2,3))
print(min(1,2,3))
print(pow(2,3))
print(abs(-12))
print(math.floor(12.2))
print(math.ceil(12.2))
print(math.sqrt(36))
