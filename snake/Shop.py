import pygame
import constants as const


class Shop:
    def __init__(self):
        self.current_skin = 0
        self.snake_skins = []
        self.snake_skins.append([const.snake_head_1, const.snake_tail_1])
        self.snake_skins.append([const.snake_head_2, const.snake_tail_2])

        self.current_background = 0
        self.backgrounds = []
        self.background_img = pygame.image.load("Images/sand.jpg")
        self.backgrounds.append(self.background_img)
        self.background_img = pygame.image.load("Images/anime.jpg")
        self.backgrounds.append(self.background_img)
