import pygame

from src.button import Button
from src.game import Game
from src.contextmenu import Context
from src.soldier import *
from src.tower import *

pygame.init()

SCREEN_WIDTH = 1248 # 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Castle Royale')


clock = pygame.time.Clock()
FPS = 60

hamburger = Context()
current_tile = None

# 1 - Menu
# 2 - New Game
# 3 - Load Game
# 4 - In Game

game_state = 4

# tile1 = tile.Tile()

btn_quit = Button((255, 0, 0), 10, 676, 235, 40, "QUIT")
btn_build = Button((255, 0, 0), 260, 676, 235, 40, "BUILD")
btn_train = Button((255, 0, 0), 510, 676, 235, 40, "TRAIN")
btn_move = Button((255, 0, 0), 760, 676, 235, 40, "MOVE")
btn_continue = Button((255, 0, 0), 1010, 676, 235, 40, "CONTINUE")

game = Game()
game.new_game(1000, "Player1", "Player2")

# TODO: kastély látszon
# TODO: gombok az egységekhez

#Test
'''
game._map[1][1]._units.append(Basic_Soldier(game._map[0], game._player_2, 0, 0))
game._map[1][1]._units.append(Climber(game._map[0], game._player_2, 0, 0))
game._map[1][1]._units.append(Tank(game._map[0], game._player_2, 0, 0))
game._map[1][1]._units.append(Suicide(game._map[0], game._player_2, 0, 0))
game._map[4][4]._units.append(Basic_Tower(game._map[0], game._player_2, 0, 0))
game._map[2][2]._units.append(Splash(game._map[0], game._player_2, 0, 0))
game._map[3][3]._units.append(Slow(game._map[0], game._player_2, 0, 0))

game._map[2][1]._units.append(Basic_Soldier(game._map[0], game._player_1, 0, 0))
game._map[2][1]._units.append(Climber(game._map[0], game._player_1, 0, 0))
game._map[2][1]._units.append(Tank(game._map[0], game._player_1, 0, 0))
game._map[2][1]._units.append(Suicide(game._map[0], game._player_1, 0, 0))
game._map[5][4]._units.append(Basic_Tower(game._map[0], game._player_1, 0, 0))
game._map[3][2]._units.append(Splash(game._map[0], game._player_1, 0, 0))
game._map[4][3]._units.append(Slow(game._map[0], game._player_1, 0, 0))
game._player_1.add(Climber(game._map[0], game._player_1, 0, 0))
game._player_1.add(Slow(game._map[0], game._player_1, 0, 0))
'''
font = pygame.font.SysFont('comicsans', 20)


# Change name color based on round
name_color = (0, 0, 0)
name_color_now_playing = (255, 0, 0)


def get_name_color(player):
    if game.current_player == player:
        return name_color_now_playing
    return name_color


run = True
while run:
    clock.tick(FPS)
    # Background color for testing
    screen.fill((54, 71, 101))
    # Draw update function
    if game_state == 1:
        pass
        # draw
    elif game_state == 2:
        pass
        # draw
    elif game_state == 3:
        pass
        # draw
    elif game_state == 4:
        # Draw Tiles

        for row in game.map:
            for tile in row:
                tile.draw(screen)

        # Draw Player Information
        player1_name = font.render(str(game.player_1.name), True, get_name_color(game.player_1))
        player1_money = font.render(str(game.player_1.gold), True, get_name_color(game.player_1))

        screen.blit(player1_name, (10, 10))
        screen.blit(player1_money, (10, 35))

        player2_name = font.render(str(game.player_2.name), True, get_name_color(game.player_2))
        player2_money = font.render(str(game.player_2.gold), True, get_name_color(game.player_2))

        screen.blit(player2_name, (SCREEN_WIDTH - max(player2_money.get_width(), player2_name.get_width()) - 10, 10))
        screen.blit(player2_money, (SCREEN_WIDTH - max(player2_money.get_width(), player2_name.get_width()) - 10, 35))

        current_player_state = font.render(str(game.current_player.state), True, (0, 0, 0))
        screen.blit(current_player_state, ((SCREEN_WIDTH / 2) - (current_player_state.get_width() / 2), 10))
        # button1.draw(screen)

        if not hamburger.opened:
            btn_quit.is_over(pygame.mouse.get_pos())
            btn_build.is_over(pygame.mouse.get_pos())
            btn_train.is_over(pygame.mouse.get_pos())
            btn_move.is_over(pygame.mouse.get_pos())
            btn_continue.is_over(pygame.mouse.get_pos())

        btn_quit.draw(screen)
        btn_build.draw(screen)
        btn_train.draw(screen)
        btn_move.draw(screen)
        btn_continue.draw(screen)


        # Draw Context Menu

        hamburger.draw(screen)
        hamburger.is_over(pygame.mouse.get_pos())
    # Keyboard input update function
    for event in pygame.event.get():
        if game_state == 1:
            pass
            # keyboard input
        elif game_state == 2:
            pass
            # keyboard input
        elif game_state == 3:
            pass
            # keyboard input
        elif game_state == 4:
            if hamburger.opened:
                if event.type == pygame.MOUSEBUTTONUP:
                    # if hamburger.is_outside(pygame.mouse.get_pos()):
                    content = hamburger.is_over(pygame.mouse.get_pos())
                    # print(content)
                    for item in content:
                        if item[2] and item[1] == "Basic":
                            print("basic")
                            current_tile.build(game.current_player, "Basic_Tower")
                        if item[2] and item[1] == "Slow":
                            print("slow")
                            current_tile.build(game.current_player, "Slow")
                        if item[2] and item[1] == "Splash":
                            print("splash")
                            current_tile.build(game.current_player, "Splash")
                        if item[2] and item[1] == "Barracks":
                            print("barracks")
                        if item[2] and item[1] == "Soldier":
                            print("Soldier")
                        if item[2] and item[1] == "Climber":
                            print("Climber")
                        if item[2] and item[1] == "Suicide":
                            print("Suicide")
                        if item[2] and item[1] == "Tank":
                            print("Tank")
                            # current_tile.build(game.current_player, item[1])
                        hamburger.opened = False
            else:
                for row in game.map:
                    for tile in row:
                        if tile.is_over(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONUP:
                            if game.current_player.state == "BUILD":
                                mouse_cords = pygame.mouse.get_pos()
                                print("BUILD")
                                hamburger.change_content(["Basic", "Slow", "Splash", "Barracks"])
                                hamburger.open(mouse_cords[0], mouse_cords[1])

                            elif game.current_player.state == "TRAIN":
                                mouse_cords = pygame.mouse.get_pos()
                                print("TRAIN")
                                hamburger.change_content(["Soldier", "Climber", "Suicide", "Tank"])
                                hamburger.open(mouse_cords[0], mouse_cords[1])
                            elif game.current_player.state == "MOVE":
                                print("MOVE")
                            print("Tile Cords: {}, {}".format(tile.x, tile.y))
                            current_tile = tile
                if event.type == pygame.MOUSEBUTTONUP:
                    if btn_continue.is_over(pygame.mouse.get_pos()):
                        game.next_round()
                    elif btn_quit.is_over(pygame.mouse.get_pos()):
                        run = False
                    elif btn_build.is_over(pygame.mouse.get_pos()):
                        game.current_player.state = "BUILD"
                        # print(game.current_player.state)
                    elif btn_train.is_over(pygame.mouse.get_pos()):
                        game.current_player.state = "TRAIN"
                        # print(game.current_player.state)
                    elif btn_move.is_over(pygame.mouse.get_pos()):
                        game.current_player.state = "MOVE"
                        # print(game.current_player.state)

        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()


