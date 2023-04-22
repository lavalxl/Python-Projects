import pygame
import src.constants as const


class Snake(pygame.sprite.Sprite):

    def __init__(self, head_img, tail_img):
        pygame.sprite.Sprite.__init__(self)
        self.snake_head_img = head_img
        self.snake_tail_img = tail_img
        self.image = pygame.transform.scale(self.snake_head_img, (const.PIECE_SIZE, const.PIECE_SIZE))
        self.rect = self.image.get_rect()
        self.rect.center = [const.WIDTH / 2, const.HEIGHT / 2]
        self.pieces = []
        self.length = 1
        self.speedx = 0
        self.speedy = 0
        self.score = 0
        self.direction = None

    def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT] or keystate[pygame.K_a]:
            self.speedx = -const.SPEED
            self.speedy = 0
            self.image = pygame.transform.rotate(self.snake_head_img, 90)
            self.direction = "L"
        elif keystate[pygame.K_RIGHT] or keystate[pygame.K_d]:
            self.speedx = const.SPEED
            self.speedy = 0
            self.image = pygame.transform.rotate(self.snake_head_img, 270)
            self.direction = "R"
        elif keystate[pygame.K_UP] or keystate[pygame.K_w]:
            self.speedy = -const.SPEED
            self.speedx = 0
            self.image = pygame.transform.rotate(self.snake_head_img, 360)
            self.direction = "U"
        elif keystate[pygame.K_DOWN] or keystate[pygame.K_s]:
            self.speedy = const.SPEED
            self.speedx = 0
            self.image = pygame.transform.rotate(self.snake_head_img, 180)
            self.direction = "D"

        self.rect.x += self.speedx
        self.rect.y += self.speedy

    def draw(self, window):
        for i in self.pieces[:-2]:
            if self.direction == "L":
                window.blit(pygame.transform.rotate(self.snake_tail_img, 270), [i[0], i[1]])
            if self.direction == "R":
                window.blit(pygame.transform.rotate(self.snake_tail_img, 90), [i[0], i[1]])
            if self.direction == "U":
                window.blit(pygame.transform.rotate(self.snake_tail_img, 180), [i[0], i[1]])
            if self.direction == "D":
                window.blit(pygame.transform.rotate(self.snake_tail_img, 360), [i[0], i[1]])

    def collision(self, col_type):
        if col_type == 'score':
            self.length += 5
            self.score += 1
            const.FPS += 1
        elif col_type == 'acc':
            self.score += 6
            const.FPS += 3
        else:
            self.score = max(0, self.score - 5)
            const.FPS = max(30, const.FPS - 10)

    def boarder_collisions(self):
        if self.rect.right > const.WIDTH or self.rect.left < 0 or self.rect.top < 0 or self.rect.bottom > const.HEIGHT:
            return True
        return False
