import pygame

from origin.helpers.func import load_image
from origin.helpers.variables import SURFACE, SCREEN


class Menu:
    """Меню - отсюда начинается игра"""
    def __init__(self, parameters=None):
        if parameters is None:
            parameters = [
                (120, 140, 'Start', (125, 0, 255), (255, 255, 255), 0)]
        # self.func = func
        self.parameters = parameters
        self.image = load_image('project_name.png')
        self.image = pygame.transform.scale(self.image, (700, 100))
        self.volume = 1

    def render(self, surf, font, index):
        for i in self.parameters:
            if index == i[-1]:
                surf.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                surf.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))

    def menu(self):
        done = True
        font_menu = pygame.font.Font(pygame.font.match_font('pacifico'), 100)
        index = 0
        while done:
            SURFACE.fill((16, 164, 149))
            pos = pygame.mouse.get_pos()
            for i in self.parameters:
                if i[0] < pos[0] < i[0] + 155 and i[1] < pos[1] < i[1] + 50:
                    index = i[-1]
            self.render(SURFACE, font_menu, index)
            SURFACE.blit(self.image, (150, 50))
            SCREEN.blit(SURFACE, (0, 0))
            # pygame.draw.line(screen, (255, 0, 0), (500, 0), (500, 890))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if index == 0:
                        # self.func()
                        return 0
                    elif index == 1:
                        self.settings()
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
                            # self.func()
                            return self.volume
                        elif index == 1:
                            self.volume = self.settings()
                        elif index == 2:
                            exit()
            pygame.display.flip()

    def settings(self):
        settings = True
        main_name = pygame.font.Font(pygame.font.match_font('comicsansms'), 130).render('SETTINGS', True, 'purple')
        font_menu = pygame.font.Font(pygame.font.match_font('pacifico'), 100)
        pos = [700, 350]
        while settings:
            SURFACE.fill((16, 164, 149))
            SURFACE.blit(main_name, (160, 30))
            SURFACE.blit(font_menu.render('Volume', True, (89, 118, 10)), 
                         (390, 270))
            SURFACE.blit(font_menu.render('NFT', True, (89, 118, 10)),
                         (450, 430))
            SURFACE.blit(font_menu.render('Back', True, (89, 118, 10)),
                         (430, 600))
            pygame.draw.line(SURFACE, 'white', (300, 370), (710, 370))
            pygame.draw.rect(SURFACE, (89, 118, 10), (*pos, 20, 40))
            SCREEN.blit(SURFACE, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return ((pos[0] - 400) / 200) * 100
                    if event.key == pygame.K_LEFT and pos[0] > 310:
                        pos[0] -= 10
                    if event.key == pygame.K_RIGHT and pos[0] < 690:
                        pos[0] += 10
                    if event.key == pygame.K_RETURN:
                        return (pos[0] - 400) / 200
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if 300 <= mouse_pos[0] <= 700 \
                            and 350 <= mouse_pos[1] <= 390:
                        pos[0] = mouse_pos[0]
                    elif mouse_pos[0] > 700 and 350 <= mouse_pos[1] <= 390 \
                            and pos[0] < 690:
                        pos[0] += 10
                    elif mouse_pos[0] < 300 and 350 <= mouse_pos[1] <= 390 \
                            and pos[0] > 310:
                        pos[0] -= 10
            pygame.display.flip()


