import pygame as pg

from src.origin.classes.texture import Texture
from src.origin.helpers import CELL_SIZE, SCREEN, STRIKE_GROUP, load_image


class Brick(Texture):
    """Класс кирпичей"""
    def __init__(self, *args):
        super().__init__(*args)
        self.image = load_image(r"texture_pack\good_brick.png")
        self.hp = 3

    def check_collision(self):
        if pg.sprite.spritecollideany(self, STRIKE_GROUP):
            self.hp -= 1

    def show_xp(self):
        xp = self.hp / 3
        pg.draw.rect(SCREEN, "green", (self.rect.x, self.rect.y - 10, CELL_SIZE * xp, 5))
        pg.draw.rect(SCREEN, "red",
                         (self.rect.x + CELL_SIZE * xp, self.rect.y - 10, CELL_SIZE - CELL_SIZE * xp, 5))

    def update(self, *args):
        if not self.hp:
            self.board.set_empty(self.pos)
            self.kill()
        elif self.hp <= 2:
            self.show_xp()