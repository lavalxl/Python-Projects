import pygame
import src.constants as const


class Background:
    def __init__(self):
        self.image = pygame.transform.scale(const.background_1, (const.WIDTH, const.HEIGHT))

    def draw(self, window):
        window.blit(self.image, (0, 0))


class MovingBackground(Background):
    def __init__(self, speed):
        super().__init__()
        self.speed = speed
        self._offset = (0, 0)
        self._window_size = (const.WIDTH, const.HEIGHT)

    def draw(self, window):
        window.fill((0, 0, 0))
        window.blit(self.image, self._offset)
        window.blit(self.image, (self._offset[0] - self._window_size[0], self._offset[1]))
        window.blit(self.image, (self._offset[0], self._offset[1] - self._window_size[1]))
        window.blit(self.image, (self._offset[0] - self._window_size[0], self._offset[1] - self._window_size[1]))

        self._offset = (self._offset[0] + self.speed[0], self._offset[1] + self.speed[1])
        if self._offset[0] >= self._window_size[0]:
            self._offset = self._offset[0] - self._window_size[0], self._offset[1]
        if self._offset[1] >= self._window_size[1]:
            self._offset = self._offset[0], self._offset[1] - self._window_size[1]
