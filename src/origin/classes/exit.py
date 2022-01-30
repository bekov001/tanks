import pygame
import pygame_gui as gui
from ..helpers import *


class Settings:
    def __init__(self, music):
        self.manager = gui.UIManager(SIZE, load_file("data/settings.json"))
        btn_size = (200, 120)
        self.music = music
        for index, (name, variable) in enumerate(zip(("RETURN", "QUIT"),
                                                     ["return_btn",
                                                      "exit_btn"]), 1):
            setattr(self, variable, gui.elements.UIButton(
                relative_rect=pygame.Rect((WIDTH // 2 - btn_size[1],
                                           HEIGHT // 2 + (index - 1) *
                                           (btn_size[1] + 10)), btn_size),
                text=name,
                manager=self.manager))

    def start_screen(self):
        fon = pygame.Surface((WIDTH, WIDTH))
        fon.fill("red")
        SCREEN.blit(fon, (0, 0))
        font_menu = pygame.font.Font(pygame.font.match_font('pacifico'), 100)
        pos = [self.music['shot'].get_volume() * 390 + 300, 150]
        pos_back = [pygame.mixer.music.get_volume() * 390 + 300, 300]
        flag = False
        while True:
            time_delta = CLOCK.tick(60) / 1000.0
            SCREEN.fill('red')
            SCREEN.blit(font_menu.render(
                "Effect's volume", True, (89, 118, 10)),
                (270, 70))
            SCREEN.blit(font_menu.render(
                'Background music', True, (89, 118, 10)),
                (230, 210))
            pygame.draw.line(SCREEN, 'white', (300, 170), (690, 170))
            pygame.draw.line(SCREEN, 'white', (300, 320), (690, 320))
            pygame.draw.rect(SCREEN, (89, 118, 10), (*pos, 20, 40))
            pygame.draw.rect(SCREEN, (89, 118, 10), (*pos_back, 20, 40))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "CLOSE"
                if event.type == gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.return_btn:
                        return 0
                    if event.ui_element == self.exit_btn:
                        return "EXIT"
                if event.type == pygame.MOUSEBUTTONDOWN and \
                        event.button == pygame.BUTTON_LEFT:
                    mouse_pos = pygame.mouse.get_pos()
                    if 300 <= mouse_pos[0] <= 710 \
                            and 150 <= mouse_pos[1] <= 190:
                        flag = True
                    elif mouse_pos[0] > 690 and 150 <= mouse_pos[1] <= 190:
                        if pos[0] < 680:
                            pos[0] += 10
                        else:
                            pos[0] = 690
                        for sound in self.music.values():
                            sound.set_volume((pos[0] - 300) / 390)
                    elif mouse_pos[0] < 300 and 150 <= mouse_pos[1] <= 190:
                        if pos[0] > 310:
                            pos[0] -= 10
                        else:
                            pos[0] = 300
                        for sound in self.music.values():
                            sound.set_volume((pos[0] - 300) / 390)
                    if 300 <= mouse_pos[0] <= 710 \
                            and 300 <= mouse_pos[1] <= 340:
                        flag = True
                    elif mouse_pos[0] > 690 and 300 <= mouse_pos[1] <= 340:
                        if pos_back[0] < 680:
                            pos_back[0] += 10
                        else:
                            pos_back[0] = 690
                        pygame.mixer.music.pause()
                        pygame.mixer.music.set_volume(
                            (pos_back[0] - 300) / 390)
                        pygame.mixer.music.unpause()
                    elif mouse_pos[0] < 300 and 300 <= mouse_pos[1] <= 340:
                        if pos_back[0] > 310:
                            pos_back[0] -= 10
                        else:
                            pos_back[0] = 300
                        pygame.mixer.music.pause()
                        pygame.mixer.music.set_volume(
                            (pos_back[0] - 300) / 390)
                        pygame.mixer.music.unpause()
                if event.type == pygame.MOUSEBUTTONUP and \
                        event.button == pygame.BUTTON_LEFT:
                    flag = False
                if event.type == pygame.MOUSEMOTION:
                    mouse_pos = pygame.mouse.get_pos()
                    if flag and 300 <= mouse_pos[0] <= 690 \
                            and 150 <= mouse_pos[1] <= 190:
                        pos[0] = mouse_pos[0]
                        for sound in self.music.values():
                            sound.set_volume((pos[0] - 300) / 390)
                    if flag and 300 <= mouse_pos[0] <= 690 \
                            and 300 <= mouse_pos[1] <= 340:
                        pos_back[0] = mouse_pos[0]
                        pygame.mixer.music.pause()
                        pygame.mixer.music.set_volume(
                            (pos_back[0] - 300) / 390)
                        pygame.mixer.music.unpause()
                self.manager.process_events(event)
            self.manager.update(time_delta)
            self.manager.draw_ui(SCREEN)
            pygame.display.flip()