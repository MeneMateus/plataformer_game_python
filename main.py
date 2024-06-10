import os
import random
import math
import pygame

from player import Player
from os import listdir
from os.path import isfile, join
print("Inicializando Pygame...")
pygame.init()
print("Configurando a tela...")
pygame.display.set_caption("Plataforma")

BG_COLOR = (255, 255, 255)
WIDTH, HEIGHT = 1000, 800
FPS = 60
PLAYER_VEL = 5

window = pygame.display.set_mode((WIDTH, HEIGHT))



def load_image(dir,name):
    image = pygame.image.load(join("assets", dir, name))
    return image

def get_background(name):
    image = load_image("Background",name)
    _,_, width, heigth = image.get_rect() # x, y estão como "_" pois não é preciso mexer neles.
    tiles = []
    
    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // heigth + 1):
            pos = [i * width, j * heigth]
            tiles.append(pos)

    return tiles, image

def draw(window, background, bg_image, player):
    for tile in background:
        window.blit(bg_image, tile)

    player.draw(window)

    pygame.display.update()

def handle_move(player):
    keys = pygame.key.get_pressed()

    player.x_vel = 0
    if keys[pygame.K_LEFT]:
        player.move_left(PLAYER_VEL)
    
    if keys[pygame.K_RIGHT]:
        player.move_rigth(PLAYER_VEL)

def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Blue.png")
    print("Carregando o jogador...")
    player = Player(100, 100, 50, 50)

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        player.loop(FPS)
        handle_move(player)
        draw(window, background, bg_image, player)
    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)