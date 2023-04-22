import pygame
import sys
from src.Game import Game

pygame.init()
pygame.mixer.init()

game = Game()
game.play()

pygame.quit()
sys.exit()
