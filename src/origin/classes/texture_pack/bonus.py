import pygame as pg


from ..texture import Texture
from origin.helpers.func import load_image
from origin.helpers.variables import CELL_SIZE, STRIKE_GROUP, SCREEN, \
    HEAL_BONUS_GROUP, ALL_SPRITES, TANK_GROUP, ENEMY_TANK_GROUP, \
    COOLDOWN_BONUS_GROUP


class Heal(Texture):
    """Класс кирпичей"""
    heal_points = 40

    def __init__(self, *args):
        super().__init__(*args)
        self.add(HEAL_BONUS_GROUP)
        self.frames = []
        self.cut_sheet(pg.transform.scale(load_image(
            r'texture_pack/bonus_anim.png'), (6 * CELL_SIZE, CELL_SIZE)), 6, 1)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.collision = False

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pg.Rect(*self.pos, sheet.get_width() // columns,
                            sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pg.Rect(
                    frame_location, self.rect.size)))

    def check_collision(self):
        for group in [TANK_GROUP, ENEMY_TANK_GROUP, STRIKE_GROUP]:
            if pg.sprite.spritecollideany(self, group):
                if group == STRIKE_GROUP:
                    self.music['break'].play()
                self.collision = True

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
        if self.collision:
            self.kill()


class CoolDown(Texture):
    """Класс кирпичей"""
    cooldown_time = 1

    def __init__(self, *args):
        super().__init__(*args)
        self.add(COOLDOWN_BONUS_GROUP)
        self.frames = []
        self.cut_sheet(pg.transform.scale(load_image(
            r'texture_pack/bonus_anim.png'), (6 * CELL_SIZE, CELL_SIZE)), 6, 1)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]

        self.collision = False

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pg.Rect(*self.pos, sheet.get_width() // columns,
                            sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pg.Rect(
                    frame_location, self.rect.size)))

    def check_collision(self):
        for group in [TANK_GROUP, ENEMY_TANK_GROUP, STRIKE_GROUP]:
            if pg.sprite.spritecollideany(self, group):
                if group == STRIKE_GROUP:
                    self.music['break'].play()
                self.collision = True

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
        if self.collision:
            self.kill()

