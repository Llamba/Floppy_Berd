import pygame

pygame.init()

clock = pygame.time.Clock()
fps = 60
screenx = 1820
screeny = 980

screen = pygame.display.set_mode((screenx, screeny))
pygame.display.set_caption("Floppy Berd")

running = True

bg = pygame.image.load("img/plain blue.png")
trees_img = pygame.image.load("img/whatever these are.png")
# Game variables
ground_scroll = 0
scroll_speed = 2

from flappy_bird import Bird


berd_group = pygame.sprite.Group()

berd = Bird(100, screeny / 2)

berd_group.add(berd)

while running:

    clock.tick(fps)

    screen.blit(bg, (0, 0))
    screen.blit(trees_img, (ground_scroll, 584))
    berd_group.draw(screen)
    ground_scroll -= scroll_speed
    berd_group.update()
    if ground_scroll == -1920:
        ground_scroll = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
