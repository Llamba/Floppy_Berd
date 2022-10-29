import pygame
from flappy_bird import Bird
from Pipes import Pipes

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
flying = False
game_over = False
pipe_gap = 100
pipe_frequency = 1500  # miliseconds
lastpipe = pygame.time.get_ticks()

berd_group = pygame.sprite.Group()
berd = Bird(100, int(screeny) / 2)

berd_group.add(berd)

pipe_group = pygame.sprite.Group()

while running:

    clock.tick(fps)

    if berd.rect.y > 900:
        game_over = True

    if not game_over:
        time_now = pygame.time.get_ticks()
        if time_now >= 1500:
            btm_pipe = Pipes(screenx, int(screeny / 2) + pipe_gap / 2, -1)
            top_pipe = Pipes(screenx, int(screeny / 2) - pipe_gap / 2, 1)
            pipe_group.add(btm_pipe)
            pipe_group.add(top_pipe)
            time_now = 0

    screen.blit(bg, (0, 0))
    screen.blit(trees_img, (ground_scroll, 610))
    ground_scroll -= scroll_speed

    berd_group.draw(screen)
    pipe_group.draw(screen)

    berd_group.update()
    pipe_group.update()

    if ground_scroll == -1920:
        ground_scroll = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
