from pygame import *


def draw_brick(screen, width, height):
    for i in range(1, n + 2):
        for j in range(1, n + 1):
            if i % 2:
                draw.rect(screen, (176, 0, 0), (width * (j - 1) + (2 if j > 1 else 0), height * (i - 1) + 2 if i != 1 else 0, width, height))
                draw.line(screen, "white", (width * j, height * (i - 1) + 2 if i != 1 else 0), (width * j, height * i + 1 if i != 1 else height - 1), 2)
            else:
                draw.rect(screen, (176, 0, 0), (width * (j - 1) + (2 if j > 1 else 0) - width // 2, height * (i - 1) + 2 if i != 1 else 0, width, height))
                draw.line(screen, "white", (width * j - width // 2, height * (i - 1) + 2 if i != 1 else 0), (width * j  - width // 2, height * i + 1 if i != 1 else height - 1), 2)
        draw.line(screen, "white", (0, height * i), (width * j, height * i), 2)


if __name__ == '__main__':
        init()
        width, height = 30, 15
        n = 13
        screen = display.set_mode((300, 200))
        display.set_caption("Шахматная клетка")
        draw_brick(screen, width, height)
        display.flip()
        while event.wait().type != QUIT:
            pass
        quit()