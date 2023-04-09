import pygame

# color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (11, 140, 19)
RED = (255, 0, 0)

# screen
WIDTH = 700
HEIGHT = 500

# game settings
FPS = 30
SPEED = 5
PIECE_SIZE = 15

# font
ARIAL = pygame.font.match_font('arial')
TNR = pygame.font.match_font('times new roman')

# images
snake_head_1 = pygame.image.load("Images/snake_head.png")
snake_tail_1 = pygame.image.load("Images/snake_tail.png")
snake_head_2 = pygame.image.load("Images/vader.png")
snake_tail_2 = pygame.image.load("Images/clone.png")
apple = pygame.image.load("Images/apple.png")
background_1 = pygame.image.load("Images/sand.jpg")
background_2 = pygame.image.load("Images/anime.jpg")
pause = pygame.image.load("Images/pause_button.png")
icecream = pygame.image.load("Images/icecream.png")
pizza = pygame.image.load("Images/pizza.png")
ice_background = pygame.image.load("Images/ice_bg.jpg")
pizza_background = pygame.image.load("Images/pizza_bg.jpg")
brick = pygame.image.load("Images/brick.png")
