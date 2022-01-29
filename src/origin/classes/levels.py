import pygame_gui as gui
from ..helpers import *


class Levels:
    def __init__(self):
        self.manager = gui.UIManager(SIZE, load_file("data/levels.json"))
        self.intro_text = ["УРОВНИ", "",
                      "Правила игры",
                      "Если в правилах несколько строк,",
                      "приходится выводить их построчно"]
        for index, name in enumerate(["first_lvl", "second_lvl", "third_lvl"], 1):
            setattr(self, name, gui.elements.UIButton(
                relative_rect=pygame.Rect((200 + (index - 1) * 230, HEIGHT // 2 - 100), (200, 100)),
                text=str(index),
                manager=self.manager))
        self.second_lvl.disable()
        self.third_lvl.disable()

    def render(self):
        intro_text = self.intro_text
        fon = pygame.Surface((WIDTH, WIDTH))
        fon.fill("blue")
        SCREEN.blit(fon, (0, 0))
        font = pygame.font.Font(None, 30)
        text_coord = 50

        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            SCREEN.blit(string_rendered, intro_rect)

    def start_screen(self):
        self.render()

        while True:
            # time_delta = CLOCK.tick(60) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "CLOSE"
                if event.type == gui.UI_BUTTON_PRESSED:
                    for index, name in\
                            enumerate(["first_lvl", "second_lvl", "third_lvl"], 1):
                        if event.ui_element == getattr(self, name):
                            return f'map{index}.txt'
                # elif event.type == pygame.KEYDOWN or \
                #         event.type == pygame.MOUSEBUTTONDOWN:
                #     pass
                self.manager.process_events(event)
            self.manager.update(1000)
            self.manager.draw_ui(SCREEN)
            pygame.display.flip()