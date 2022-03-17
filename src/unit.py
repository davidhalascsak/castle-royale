class Unit:

    def __init__(self, health, damage, x, y, tile, owner):
        self._health = health
        self._damage = damage
        self._x = x
        self._y = y
        self._tile = tile
        self._owner = owner

    def change_health(self, damage):
        new = self._health - damage
        self.health = new

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, change):
        self._health = change

    @property
    def damage(self):
        return self._damage

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, change):
        self._x = change

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, change):
        self._y = change

