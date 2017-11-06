from math import floor
from dice import d
spells = [[] for i in range(0,10)]
def level(n):
    def dec(spl):
        spl.level = n
        return spl
    return dec
class spell:
    def __init__(self,func):
        self.func = func
        self.__name__ = " ".join(self.func.__name__.split("_")).title()
        spells[func.level].append(self)
    def __call__(self,*a,**kw):
        self.func(*a,**kw)





@spell
@level(9)
def power_word_kill(caster,target):
    assert caster.slots[9]>0
    if target.HP<100:
        target.die()
        caster.slots[9]-=1

@spell
@level(0)
def poison_spray(caster,target):
    target.HP -= d(10)
    target.poisoned = True

@spell
@level(1)
def magic_missile(caster,slot,*targets):
    assert caster.slots[slot]>0
    assert len(targets)<=slot+2
    assert slot>0
    for target in targets:
        target.HP-=d(4)+1
    caster.slots[slot]-=1

@spell
@level(1)
def false_life(caster,slot):
    assert caster.slots[slot]>0
    assert slot>0
    caster.THP += d(4)+4 + 5*(slot-1)

@spell
@level(0)
def fire_bolt(caster,target):
    target.HP -= sum(d(10) for i in range(floor(caster.level/5)+1))

@spell
@level(2)
def scorching_ray(caster,slot,*targets):
    assert slot>1
    assert caster.slots[slot]>0
    assert len(targets)<=slot+1
    for target in targets:
        target.HP-= d(6)+d(6)
    caster.slots[slot]-=1

@spell
@level(0)
def ray_of_frost(caster,target):
    if d(20)+caster.spellattack>=target.AC:
        target.HP-=d(8)
        target.speed -=10

@spell
@level(1)
def burning_hands(caster,slot):
    assert caster.slots[slot]>0