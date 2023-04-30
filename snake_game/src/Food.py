import pygame
import random
import src.constants as const


class Food(pygame.sprite.Sprite):

    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(image, (const.PIECE_SIZE + 8, const.PIECE_SIZE + 8))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(30, const.WIDTH - 30, const.PIECE_SIZE - 10)
        self.rect.y = random.randrange(30, const.HEIGHT - 30, const.PIECE_SIZE - 10)


class ScoreFood(Food):
    def __init__(self):
        super().__init__(const.apple)


class Acceleration(Food):
    def __init__(self):
        super().__init__(const.icecream)
        self.id = 'acc'


class Deceleration(Food):
    def __init__(self):
        super().__init__(const.pizza)
        self.id = 'dec'


def generation(food_type, walls):
    foods = pygame.sprite.Group()
    food = None
    bonus = random.choice(['acc', 'dec'])
    if food_type == 'score_food':
        food = ScoreFood()
    elif food_type == 'bonus':
        if bonus == 'acc':
            food = Acceleration()
        else:
            food = Deceleration()
    while pygame.sprite.spritecollide(food, walls, False):
        if food_type == 'score_food':
            food = ScoreFood()
        elif food_type == 'bonus':
            if bonus == 'acc':
                food = Acceleration()
            else:
                food = Deceleration()
    foods.add(food)
    return foods
