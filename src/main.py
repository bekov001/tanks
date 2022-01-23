import time

import pygame
import sys
import pygame_gui as gui

# from origin.classes.exit import start_screen
from origin.helpers.func import load_image
from origin.classes.player_tank import PlayerTank
from origin.classes.tank import Tank
from origin.classes.enemy_tank import EnemyTank
from origin.classes.field import Field
from origin.helpers.variables import *
from origin.classes.exit import start_screen
from origin.classes.menu import Menu


def menu(self):
    done = True
    font_menu = pygame.font.Font(pygame.font.match_font('pacifico'), 100)
    index = 0
    while done:
        surface.fill((16, 164, 149))
        pos = pygame.mouse.get_pos()
        for i in self.parameters:
            if i[0] < pos[0] < i[0] + 155 and i[1] < pos[1] < i[1] + 50:
                index = i[-1]
        self.render(surface, font_menu, index)
        surface.blit(self.image, (150, 50))
        screen.blit(surface, (0, 0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if index == 0:
                    main()
                elif index == 2:
                    sys.exit()

class Game:
    """Класс игры, здесь происходит сама игра, а также загружается карта"""
    def __init__(self):
        self.board = Field(N - 2, N)

    def main(self):
        """Главная функция игры"""
        running = True
        timing = time.time()
        step_timing = time.time()
        seconds = 0.1
        player = PlayerTank(60, 60)
        enemy = EnemyTank(885, 775, player)
        self.board.render(screen)
        manager = gui.UIManager(SIZE)
        hello_button = gui.elements.UIButton(
            relative_rect=pygame.Rect((WIDTH - 105, 5), (90, 50)),
            text='SETTINGS',
            manager=manager)
        clock = pygame.time.Clock()
        btn_click = False
        while running:
            time_delta = clock.tick(60) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                manager.process_events(event)
                if event.type == gui.UI_BUTTON_PRESSED:
                    if event.ui_element == hello_button:
                        res = start_screen()
                        if res == "EXIT":
                            running = False
                        timing = time.time()
                        btn_click = True
                elif not btn_click:
                    player.update(event, self.board)
                else:
                    btn_click = False

                player.update(event, self.board)
                manager.process_events(event)

            if time.time() - step_timing > 0.3:
                for enemy in ENEMY_TANK_GROUP:
                    enemy.update(self.board)
                step_timing = time.time()
            if time.time() - timing > seconds:
                timing = time.time()
                screen.fill("black")
                ALL_SPRITES.draw(screen)
                for sprite in ALL_SPRITES.sprites():
                    sprite.check_collision()
                ALL_SPRITES.update()
                manager.update(time_delta)
                manager.draw_ui(screen)
                pygame.display.flip()

    def stop_game(self):
        pass


cell_size = 55
screen = pygame.display.set_mode(SIZE)
surface = pygame.Surface(SIZE)
fps = 120
clock = pygame.time.Clock()
board = Field(N - 2, N)
board.set_view(5, 5, cell_size)
screen.fill((0, 0, 0))
board.render(screen)

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Tanks')
    menu = Menu(PARAMETERS)
    menu.menu()
    done = True
    while done:
        res = menu.menu()
        if res == 0:
            game = Game()
            game.main()
        elif res == 2:
            done = False
            sys.exit()
    pygame.quit()
