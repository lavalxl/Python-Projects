import pygame
import sys
from Game import Game

pygame.init()
pygame.mixer.init()

game = Game()
game.play()

pygame.quit()
sys.exit()
