import pygame

from origin.helpers import load_image, SURFACE, SCREEN


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
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if index == 0:
                        # self.func()
                        return 0
                    elif index == 2:
                        exit()
