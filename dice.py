import random
random = random.SystemRandom()
def d(n):
    if n == 10:
        return random.randint(0,9)
    return random.randint(1,n)
def abil():
    r = [d(6) for i in range(4)]
    return sum(r)-min(r)
