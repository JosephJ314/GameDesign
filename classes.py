class Cclass:
    def __new__(cls,name,race):
        self = super().__new__(cls,name,race)
        self.name = name
        self.race = race(self)
        return cls.__init__(self)
class Cleric(Cclass):
    def __init__(self):
        pass
class Bard(Cclass):
    def __init__(self):
        pass
class Sorcerer(Cclass):
    def __init__(self):
        pass
class Wizard(Cclass):
    def __init__(self):
        pass
class Paladin(Cclass):
    def __init__(self):
        pass
class Rogue(Cclass):
    def __init__(self):
        pass
class Fighter(Cclass):
    def __init__(self):
        pass
class Druid(Cclass):
    def __init__(self):
        pass
classes = {
    "cleric":Cleric,
    "bard":Bard,
    "sorcerer":Sorcerer,
    "wizard":Wizard,
    "paladin":Paladin,
    "rogue":Rogue,
    "fighter":Fighter,
    "druid":Druid
    }
def select(clsnm):
    return classes[clsnm.lower()]