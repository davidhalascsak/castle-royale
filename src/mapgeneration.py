from src.tile import Tile
import random

class MapGeneration:
    type1 = [[0,0,0,0,0,0,0,0,0,0],
             [0,0,0,1,1,1,1,0,0,0],
             [0,0,1,1,1,1,1,1,0,0],
             [0,1,1,1,1,1,1,1,1,0],
             [0,1,1,1,1,1,1,1,1,0],
             [0,1,1,1,1,1,1,1,1,0],
             [0,1,1,1,1,1,1,1,1,0],
             [0,0,1,1,1,1,1,1,0,0],
             [0,0,0,1,1,1,1,0,0,0],
             [0,0,0,0,0,0,0,0,0,0]]

    type2 = [[0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,1,1,1,1,0],
             [0,0,0,0,0,0,0,1,1,1,1,0],
             [0,0,0,0,0,1,1,1,1,1,1,0],
             [0,0,0,0,0,1,1,1,1,1,1,0],
             [0,0,0,1,1,1,1,1,1,0,0,0],
             [0,0,0,1,1,1,1,1,1,0,0,0],
             [0,1,1,1,1,1,1,0,0,0,0,0],
             [0,1,1,1,1,1,1,0,0,0,0,0],
             [0,1,1,1,1,0,0,0,0,0,0,0],
             [0,1,1,1,1,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0]]

    type3 = [[0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,1,1,1,1,1,1,0],
             [0,0,0,0,1,1,1,1,1,1,0],
             [0,0,0,0,1,1,1,1,1,1,0],
             [0,0,0,0,1,1,1,1,1,1,0],
             [0,0,0,1,1,1,1,1,0,0,0],
             [0,1,1,1,1,1,1,0,0,0,0],
             [0,1,1,1,1,1,1,0,0,0,0],
             [0,1,1,1,1,1,1,0,0,0,0],
             [0,1,1,1,1,1,1,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0]]

    def generate_map(map_matrix):
        return map_matrix

    def check_placement_availability(obs_matrix, x, y):
        pass

    def choose_obstacles():
        pass

    def place_obstacle(obs_matrix):
        pass