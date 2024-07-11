import pygame
import sys

pygame.init()

pygame.display.set_caption("Fadi's Game :)")

width = 550
height = 500

red = (255, 165, 0) # Characters color

x = 50 # Characters location
y = 50 # Characters location

movement_speed = 50

screen = pygame.display.set_mode((width, height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]: 
            x -= movement_speed
        if keys[pygame.K_RIGHT]:
            x += movement_speed
        if keys[pygame.K_UP]:
            y -= movement_speed
        if keys[pygame.K_DOWN]:
            y += movement_speed

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, red, (x, y, 40, 60))
    pygame.display.update()

       

