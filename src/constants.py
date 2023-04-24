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
DEFAULT_FPS = 30
FPS = 30
SPEED = 5
PIECE_SIZE = 15
WALL_SIZE = PIECE_SIZE + 8
BONUS_SPAWN_FREQUENCY = 10
APPLE_SCORE = 1
APPLE_SPEED = 1
APPLE_LENGTH = 5
ICECREAM_SCORE = 6
ICECREAM_SPEED = 3
PIZZA_SCORE = -5
PIZZA_SPEED = -10

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
background_3 = pygame.image.load("Images/ice_bg.jpg")
background_4 = pygame.image.load("Images/city.jpg")
background_5 = pygame.image.load("Images/kita.png")
pause = pygame.image.load("Images/pause_button.png")
icecream = pygame.image.load("Images/icecream.png")
pizza = pygame.image.load("Images/pizza.png")
pizza_background = pygame.image.load("Images/pizza_bg.jpg")
brick = pygame.image.load("Images/brick.png")
wall = pygame.image.load("Images/wall.jpg")
snake_head_3 = pygame.image.load("Images/snake_head_1.png")
snake_tail_3 = pygame.image.load("Images/snake_tail_1.png")
