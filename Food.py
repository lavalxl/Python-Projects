import pygame
import constants as const


class Food(pygame.sprite.Sprite):

    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(image, (const.PIECE_SIZE + 8, const.PIECE_SIZE + 8))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class ScoreFood(Food):
    def __init__(self, x, y):
        self.apple_img = const.apple.convert_alpha()
        super().__init__(self.apple_img, x, y)
