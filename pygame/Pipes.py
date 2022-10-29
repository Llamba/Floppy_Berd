import pygame


class Pipes(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("img/pipes.png"), (600, 600))
        self.rect = self.image.get_rect()
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y]
        if position == -1:
            self.rect.topleft = [x, y]

    def update(self):
        self.rect.x -= 4
