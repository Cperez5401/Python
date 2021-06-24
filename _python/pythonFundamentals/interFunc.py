import random
def randInt(min=0, max= 100):
    num = random.randint(min, max)
    return num
print(randInt(max = 50))
print(randInt(min = 40, max = 60))