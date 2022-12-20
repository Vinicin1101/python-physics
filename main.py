import pygame
from pygame.locals import (QUIT, KEYDOWN, K_ESCAPE)
import pymunk
from pymunk.vec2d import Vec2d
import pymunk.pygame_util

import sys
import math

import rocket

# Variaveis Globais
GAME_TITLE = "não sei"
FPS = 60

# Tamanho da tela
SCREEN_WIDTH = 800
SCREEN_HEIGTH = 600


# pygame screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
pygame.display.set_caption(GAME_TITLE)
# pygame.display.set_icon(pygame.image.load('icon.png'))

clock = pygame.time.Clock()


# física com o pymunk
draw_options = pymunk.pygame_util.DrawOptions(screen)

space = pymunk.Space()
space.gravity = (0, 100)

# Chão
ground_body = pymunk.Body(body_type=pymunk.Body.STATIC)
ground_shape = pymunk.Segment(
    ground_body, (0, (SCREEN_HEIGTH/2)), (SCREEN_WIDTH, (SCREEN_HEIGTH/2)), 1.0)
ground_shape.color = (pygame.Color("white"))
space.add(ground_body, ground_shape)

# Foguetinho
rocket = rocket.Rocket((400, 100))

space.add(rocket.body, rocket.shape)

run = True
while run:

    # Taxa de atualização
    clock.tick(FPS)

    # close event
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
            sys.audit('quit')

        elif e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
            print("Left Click")

        # Reseta o impulso quando solta o espaço
        elif e.type == pygame.KEYUP:
            if e.key == pygame.K_SPACE:
                rocket.resetPropultion()

    keys = pygame.key.get_pressed()  # Ouve a tecla pressionada
    # Movimentação

    if keys[pygame.K_LEFT]:
        rocket.angle -= 5
        rocket.change_direction(0)
    elif keys[pygame.K_RIGHT]:
        rocket.angle += 5
        rocket.change_direction(1)

    # if keys[pygame.K_UP]:

    # if keys[pygame.K_DOWN]:

    # Faz o foguetinho subir
    if keys[pygame.K_SPACE]:
        print("YOU PRESS SPACE!")
        rocket.impulse()

    # Desenha conforme o pymunk
    screen.fill(pygame.Color("black"))
    space.debug_draw(draw_options)

    # Update
    dt = 1.0 / FPS
    space.step(dt)

    pygame.display.update()


pygame.quit()
