from src.player import Player
from src.tile import Tile
import random


class Game:
    def __init__(self):
        self._player_1 = None
        self._player_2 = None
        self._map = []
        self._current_player = None

    def new_game(self, start_gold, name_1, name_2):
        # Configure Players
        self._player_1 = Player(name_1)
        self._player_2 = Player(name_2)

        self._player_1.gold = start_gold
        self._player_2.gold = start_gold

        # Determine Starting Player
        self._current_player = random.sample({self._player_1, self._player_2}, 1)[0]

        # Generate Map
        for x in range(0, 26):
            self._map.append([])
            for y in range(0, 14):
                self._map[len(self._map) - 1].append(Tile(x, y))

    def load_game(self):
        pass

    def save_game(self):
        pass

    def next_round(self):
        if self._current_player == self._player_1:
            self._current_player = self._player_2
        else:
            self._current_player = self._player_1

        self._player_1.gold = (self._player_1.gold + self._player_1.calculate_gold_bonus())
        self._player_2.gold = (self._player_2.gold + self._player_2.calculate_gold_bonus())

    @property
    def map(self):
        return self._map

    @property
    def player_1(self):
        return self._player_1

    @property
    def player_2(self):
        return self._player_2

    @property
    def current_player(self):
        return self._current_player





