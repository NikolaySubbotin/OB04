from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        return "Удар мечом"

class Bow(Weapon):
    def attack(self):
        return "Выстрел из лука"

class Fighter():
    def __init__(self, name):
        self.name = name


    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {self.weapon.attack()}")

    def attack(self):
        print(f"{self.name} наносит урон с помощью {self.weapon.attack()}")

class Monstr():
    def __init__(self, name):
        self.name = name

    def take_damage(self):
        print(f"{self.name} получил урон")

def fight(fighter: Fighter, monster: Monstr):
    fighter.attack()
    monster.take_damage()

fighter = Fighter("Боец")
monster = Monstr("Монстр")

sword = Sword()
bow = Bow()

fighter.change_weapon(sword)
fight(fighter, monster)

fighter.change_weapon(bow)
fight(fighter, monster)








