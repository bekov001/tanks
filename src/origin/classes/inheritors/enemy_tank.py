from src.origin.helpers.variables import *
from src.origin.helpers.func import load_image

from src.origin.classes.strike import Strike
from src.origin.classes.tank import Tank


class EnemyTank(Tank):
    """Вражеский танк"""
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.transform.scale(load_image("enemy_tank.png"),
                                            (CELL_SIZE, CELL_SIZE))

        self.current_angle = 0

    # def strike(self, event):
    #     if event.type == pygame.MOUSEBUTTONDOWN:
    #         Strike((self.rect.x, self.rect.y), event.pos)

    def get_muzzle(self):
        """Функция для получения дула танка"""

    def update(self):
        """Обновление спрайта"""
        pass
