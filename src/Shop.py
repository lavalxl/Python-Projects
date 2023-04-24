import pygame
import src.constants as const


class Shop:
    def __init__(self):
        self.current_skin = 0
        self.snake_skins = []
        self.snake_skins.append([const.snake_head_1, const.snake_tail_1])
        self.snake_skins.append([const.snake_head_2, const.snake_tail_2])
        self.snake_skins.append([const.snake_head_3, const.snake_tail_3])

        self.current_background = 0
        self.backgrounds = []
        self.backgrounds.append(pygame.transform.scale(const.background_1, (const.WIDTH, const.HEIGHT)))
        self.backgrounds.append(pygame.transform.scale(const.background_2, (const.WIDTH, const.HEIGHT)))
        self.backgrounds.append(pygame.transform.scale(const.background_3, (const.WIDTH, const.HEIGHT)))
        self.backgrounds.append(pygame.transform.scale(const.background_4, (const.WIDTH, const.HEIGHT)))
        self.backgrounds.append(const.background_5)
