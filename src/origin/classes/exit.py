import pygame
import pygame_gui as gui
from helpers import load_image, WIDTH, SIZE, FPS


def start_screen():
    intro_text = ["ЗАСТАВКА", "",
                  "Правила игры",
                  "Если в правилах несколько строк,",
                  "приходится выводить их построчно"]
    fon = pygame.Surface((WIDTH, WIDTH))
    fon.fill("red")
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50

    manager = gui.UIManager(SIZE)
    exit_button = gui.elements.UIButton(
        relative_rect=pygame.Rect((WIDTH - 105, 5), (90, 50)),
        text='ВЫЙТИ',
        manager=manager)
    return_btn = gui.elements.UIButton(
        relative_rect=pygame.Rect((WIDTH - 205, 5), (90, 50)),
        text='ВЕРНУТЬСЯ',
        manager=manager)

    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == gui.UI_BUTTON_PRESSED:
                if event.ui_element == return_btn:
                    return 0
                if event.ui_element == exit_button:
                    print('Hello World!')
                    start_screen()
                    active = False
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                pass # начинаем игру
            manager.process_events(event)
        manager.update(FPS)
        manager.draw_ui(screen)
        pygame.display.flip()
        clock.tick(FPS)


screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()