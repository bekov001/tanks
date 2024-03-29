import pygame
import webbrowser

from origin.helpers.func import load_image, load_file
from origin.helpers.variables import SURFACE, SCREEN


class Menu:
    """Меню - отсюда начинается игра"""
    def __init__(self, parameters=None):
        if parameters is None:
            parameters = [
                (120, 140, 'Start', (125, 0, 255), (255, 255, 255), 0)]
        self.parameters = parameters
        self.image = load_image('project_name.png')
        self.image = pygame.transform.scale(self.image, (700, 100))
        self.volume = 1
        self.music = {}

    def render(self, surf, font, index):
        for i in self.parameters:
            if index == i[-1]:
                surf.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                surf.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))

    def menu(self, music):
        self.music = music
        done = True
        history_image = pygame.transform.scale(load_image('history.png'),
                                               (100, 100))
        font_menu = pygame.font.Font(pygame.font.match_font('pacifico'), 100)
        index = 0
        while done:
            SURFACE.fill((16, 164, 149))
            pos = pygame.mouse.get_pos()
            for i in self.parameters:
                if i[0] < pos[0] < i[0] + 155 and i[1] < pos[1] < i[1] + 50:
                    index = i[-1]
            self.render(SURFACE, font_menu, index)
            SURFACE.blit(history_image, (5, 750))
            SURFACE.blit(self.image, (150, 50))
            SCREEN.blit(SURFACE, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT:
                        mouse_pos = pygame.mouse.get_pos()
                        if 5 <= mouse_pos[0] <= 105 and \
                                750 <= mouse_pos[1] <= 850:
                            self.show_history()
                        elif index == 0:
                            return self.volume
                        elif index == 1:
                            self.volume = self.settings()
                            for sound in music.values():
                                sound.set_volume(self.volume)
                        elif index == 2:
                            exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if index > 0:
                            index -= 1
                    if event.key == pygame.K_DOWN:
                        if index < 2:
                            index += 1
                    if event.key == pygame.K_RETURN:
                        if index == 0:
                            return self.volume
                        elif index == 1:
                            self.volume = self.settings()
                            for sound in music.values():
                                sound.set_volume(self.volume)
                        elif index == 2:
                            exit()
            pygame.display.flip()

    @staticmethod
    def show_history():
        """Показывает историю игр"""
        history = True
        SCREEN.fill((16, 164, 149))
        pos_of_results = [115, 370]
        pos_of_records = [20, 20]
        record_font = pygame.font.Font(pygame.font.match_font('pacifico'), 100)
        main_font = pygame.font.Font(pygame.font.match_font('pacifico'), 70)
        results = []
        file_of_history = open(load_file('data/history.txt'), 'r')
        back_button = pygame.transform.scale(load_image('back_button.png'), 
                                             (100, 100))
        for line in file_of_history:
            results.append(line.strip())
        if results:
            results = results[::-1]
        else:
            results = 'EMPTY'
        while history:
            SURFACE.fill((16, 164, 149))
            SURFACE.blit(main_font.render(
                f"History of your games:", True,
                'yellow'),
                (20, 300)
            )
            SURFACE.blit(back_button, (5, 750))
            for line in range(len(results)):
                SURFACE.blit(main_font.render(results[line], True, 'white'),
                             (pos_of_results[0], pos_of_results[1] + 60 * line)
                             )
            if results:
                for i in range(3):
                    record = list(
                        sorted(filter(lambda y: 'won' in y, filter(
                            lambda x: 'level ' + str(i + 1) in x, results)),
                               key=lambda x: float(x.split(' ')[-1])))
                    if record:
                        SURFACE.blit(
                            record_font.render(
                                f"Best time of {i + 1} lvl: "
                                f"{record[-1].split(' ')[-1]}", True, 'red'),
                            (pos_of_records[0], pos_of_records[1] + 75 * i)
                        )
                    else:
                        SURFACE.blit(record_font.render(
                            f"Best time of {i + 1} lvl: no data",
                            True, 'red'),
                            (pos_of_records[0], pos_of_records[1] + 75 * i)
                        )
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit(0)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT:
                        mouse_pos = pygame.mouse.get_pos()
                        if 5 <= mouse_pos[0] <= 105 and \
                                750 <= mouse_pos[1] <= 850:
                            return 
            SCREEN.blit(SURFACE, (0, 0))
            pygame.display.flip()

    def settings(self):
        """Показывает экран настроек"""
        settings = True
        main_name = pygame.font.Font(pygame.font.match_font(
            'comicsansms'), 130).render('SETTINGS', True, 'purple')
        font_menu = pygame.font.Font(pygame.font.match_font('pacifico'), 100)
        pos = [self.music['shot'].get_volume() * 390 + 300, 350]
        pos_back = [pygame.mixer.music.get_volume() * 390 + 300, 500]
        flag = False
        while settings:
            SURFACE.fill((16, 164, 149))
            SURFACE.blit(main_name, (160, 30))
            SURFACE.blit(font_menu.render(
                "Effect's volume", True, (89, 118, 10)),
                         (270, 270))
            SURFACE.blit(font_menu.render(
                'Background music', True, (89, 118, 10)),
                         (230, 410))
            SURFACE.blit(font_menu.render('NFT', True, (89, 118, 10)),
                         (450, 600))
            SURFACE.blit(font_menu.render('Back', True, (89, 118, 10)),
                         (430, 770))
            pygame.draw.line(SURFACE, 'white', (300, 370), (690, 370))
            pygame.draw.line(SURFACE, 'white', (300, 520), (690, 520))
            pygame.draw.rect(SURFACE, (89, 118, 10), (*pos, 20, 40))
            pygame.draw.rect(SURFACE, (89, 118, 10), (*pos_back, 20, 40))
            SCREEN.blit(SURFACE, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return (pos[0] - 300) / 390
                    if event.key == pygame.K_LEFT and pos[0] > 310:
                        pos[0] -= 10
                    if event.key == pygame.K_RIGHT and pos[0] < 690:
                        pos[0] += 10
                    if event.key == pygame.K_RETURN:
                        return (pos[0] - 300) / 390
                if event.type == pygame.MOUSEBUTTONDOWN and \
                        event.button == pygame.BUTTON_LEFT:
                    mouse_pos = pygame.mouse.get_pos()
                    if 300 <= mouse_pos[0] <= 710 \
                            and 350 <= mouse_pos[1] <= 390:
                        flag = True
                    elif mouse_pos[0] > 690 and 350 <= mouse_pos[1] <= 390:
                        if pos[0] < 680:
                            pos[0] += 10
                        else:
                            pos[0] = 690
                    elif mouse_pos[0] < 300 and 350 <= mouse_pos[1] <= 390:
                        if pos[0] > 310:
                            pos[0] -= 10
                        else:
                            pos[0] = 300
                    if 300 <= mouse_pos[0] <= 710 \
                            and 500 <= mouse_pos[1] <= 540:
                        flag = True
                    elif mouse_pos[0] > 690 and 500 <= mouse_pos[1] <= 540:
                        if pos_back[0] < 680:
                            pos_back[0] += 10
                        else:
                            pos_back[0] = 690
                        pygame.mixer.music.pause()
                        pygame.mixer.music.set_volume(
                            (pos_back[0] - 300) / 390)
                        pygame.mixer.music.unpause()
                    elif mouse_pos[0] < 300 and 500 <= mouse_pos[1] <= 540:
                        if pos_back[0] > 310:
                            pos_back[0] -= 10
                        else:
                            pos_back[0] = 300
                        pygame.mixer.music.pause()
                        pygame.mixer.music.set_volume(
                            (pos_back[0] - 300) / 390)
                        pygame.mixer.music.unpause()
                    if 445 <= mouse_pos[0] <= 590 and \
                            595 <= mouse_pos[1] <= 665:
                        webbrowser.open(
                            'https://opensea.io/collection/colorfultanks')
                    if 425 <= mouse_pos[0] <= 600 and \
                            765 <= mouse_pos[1] <= 835:
                        return (pos[0] - 300) / 390
                if event.type == pygame.MOUSEBUTTONUP and \
                        event.button == pygame.BUTTON_LEFT:
                    flag = False
                if event.type == pygame.MOUSEMOTION:
                    mouse_pos = pygame.mouse.get_pos()
                    if flag and 300 <= mouse_pos[0] <= 690 \
                            and 350 <= mouse_pos[1] <= 390:
                        pos[0] = mouse_pos[0]
                    if flag and 300 <= mouse_pos[0] <= 690 \
                            and 500 <= mouse_pos[1] <= 540:
                        pos_back[0] = mouse_pos[0]
                        pygame.mixer.music.pause()
                        pygame.mixer.music.set_volume(
                            (pos_back[0] - 300) / 390)
                        pygame.mixer.music.unpause()

            pygame.display.flip()


