from src.unit import *


class Soldier(Unit):
    def __init__(self, health, damage, stamina, tile, owner, x, y):
        super().__init__(health=health, damage=damage, tile=tile, owner=owner, x=x, y=y)
        self._stamina = stamina
        self._alive = True

    def move(self, x, y):
        new_x = self._x + x1
        new_y = self._y + y1
        self._x = new_x
        self._y = new_y

    def take_damage(self, enemy):
        if enemy.health - self.damage > 0:
            enemy.change_health(self.damage)
        else:
            enemy.health = 0
            enemy.alive = False

    @property
    def stamina(self):
        return self._stamina

    @property
    def alive(self):
        return self._alive

    @alive.setter
    def alive(self, change):
        self._alive = change


class BasicSoldier(Soldier):
    price = 100
    max_health = 100

    def __init__(self, tile, owner, x, y):
        super().__init__(health=100, damage=50, stamina=100, tile=tile, owner=owner, x=x, y=y)


class Climber(Soldier):
    price = 150
    max_health = 120

    def __init__(self, tile, owner, x, y):
        super().__init__(health=120, damage=50, stamina=80, tile=tile, owner=owner, x=x, y=y)

    def move(self, x, y):
        pass


class Tank(Soldier):
    price = 150
    max_health = 200

    def __init__(self, tile, owner, x, y):
        super().__init__(health=200, damage=75, stamina=80, tile=tile, owner=owner, x=x, y=y)

    def attack(self, enemy):
        pass


class Suicide(Soldier):
    price = 200
    max_health = 500

    def __init__(self, tile, owner, x, y):
        super().__init__(health=500, damage=100, stamina=30, tile=tile, owner=owner, x=x, y=y)

    def attack(self, enemy):
        pass
