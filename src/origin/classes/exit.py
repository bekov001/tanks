# import pygame
#
# from src.origin.helpers import load_image, SURFACE, SCREEN
#
#
# class Settings:
#     def __init__(self, parameters=None):
#         if parameters is None:
#             parameters = [
#                 (120, 140, 'Start', (125, 0, 255), (255, 255, 255), 0)]
#         self.parameters = parameters
#         self.image = load_image('project_name.png')
#         self.image = pygame.transform.scale(self.image, (700, 100))
#
#     def render(self, surf, font, index):
#         for i in self.parameters:
#             if index == i[-1]:
#                 surf.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
#             else:
#                 surf.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))
#
#     def menu(self):
#         done = True
#         font_menu = pygame.font.Font(pygame.font.match_font('pacifico'), 100)
#         index = 0
#         while done:
#             SURFACE.fill((16, 164, 149))
#             pos = pygame.mouse.get_pos()
#             for i in self.parameters:
#                 if i[0] < pos[0] < i[0] + 155 and i[1] < pos[1] < i[1] + 50:
#                     index = i[-1]
#             self.render(SURFACE, font_menu, index)
#             SURFACE.blit(self.image, (150, 50))
#             SCREEN.blit(SURFACE, (0, 0))
#             # pygame.draw.line(screen, (255, 0, 0), (500, 0), (500, 890))
#             pygame.display.flip()
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     exit()
#                 if event.type == pygame.MOUSEBUTTONDOWN:
#                     if index == 0:
#                         print(1)
#                     elif index == 2:
#                         exit()


import pygame
import pygame_gui as gui
from ..helpers import *


class Settings:
    def __init__(self):
        self.manager = gui.UIManager(SIZE, load_file("data/settings.json"))
        btn_size = (200, 120)
        for index, (name, variable) in enumerate(zip(("RETURN", "QUIT"), ["return_btn",
                                                              "exit_btn"]), 1):
            setattr(self, variable, gui.elements.UIButton(
                relative_rect=pygame.Rect((WIDTH // 2 - btn_size[1], HEIGHT // 2 + (index - 1) * (btn_size[1] + 10)),btn_size),
                text=name,
                manager=self.manager))

    def start_screen(self):
        fon = pygame.Surface((WIDTH, WIDTH))
        fon.fill("red")
        SCREEN.blit(fon, (0, 0))

        while True:
            time_delta = CLOCK.tick(60) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "CLOSE"
                if event.type == gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.return_btn:
                        return 0
                    if event.ui_element == self.exit_btn:
                        return "EXIT"
                # elif event.type == pygame.KEYDOWN or \
                #         event.type == pygame.MOUSEBUTTONDOWN:
                #     pass
                self.manager.process_events(event)
            self.manager.update(time_delta)
            self.manager.draw_ui(SCREEN)
            pygame.display.flip()