import pygame


class Bird(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range(1, 4):
            img = pygame.image.load(f"img/Berd{num}.png")
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.vel = 0
        self.clicked = False
        self.jumpforce = 10
        self.start = False
        self.gameover = False

    def update(self):

        #  gravity
        if not self.gameover:
            if pygame.mouse.get_pressed()[0] == 1:
                self.start = True
            if self.start:
                self.vel += 0.5
                if self.vel >= 15:
                    self.vel = 15
                self.rect.y += self.vel
                if self.rect.y >= 900:
                    self.gameover = True

            #  Jump
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                if self.vel >= -15:
                    if self.vel > 0:
                        self.vel = 0
                        self.vel -= 10
                    elif self.vel <= 0:
                        self.vel -= 10
                elif self.vel < 15:
                    self.vel = -15
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

            # animation
            self.counter += 1
            flap_cooldown = 5
            if self.counter > flap_cooldown:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0

        #  Rotation
        if not self.gameover:
            self.image = pygame.transform.rotate(self.images[self.index], self.vel * -1)
        if self.gameover:
            self.image = pygame.transform.rotate(pygame.image.load("img/deadbird.png"), 90)
