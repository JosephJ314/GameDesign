abils = ["wisdom","intelligence","charisma","strength","constitution","dexterity"]
import dice
class race:
    bonus = {abil:0 for abil in abils}
    def __new__(cls,player):
        player.abils = {abil:dice.abil()+cls.bonus[abil] for abil in abils}
        return super().__new__(cls)
class elf(race):
    bonus = {abil:0 for abil in abils}
    bonus["intelligence"]+=2
class dwarf(race):
    bonus = {abil:0 for abil in abils}
class dragonborn(race):
    bonus = {abil:0 for abil in abils}
class gnome(race):
    bonus = {abil:0 for abil in abils}
class human(race):
    bonus = {abil:0 for abil in abils}
class tiefling(race):
    bonus = {abil:0 for abil in abils}
class half_elf(race):
    bonus = {abil:0 for abil in abils}
class high(elf):
    bonus = {abil:0 for abil in abils}
class wood(elf):
    bonus = {abil:0 for abil in abils}
class drow(elf):
    bonus = {abil:0 for abil in abils}
class forest(gnome):
    bonus = {abil:0 for abil in abils}
class rock(gnome):
    bonus = {abil:0 for abil in abils}
class hill(dwarf):
    bonus = {abil:0 for abil in abils}
class mountain(dwarf):
    bonus = {abil:0 for abil in abils}