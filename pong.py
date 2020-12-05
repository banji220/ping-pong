import pygame
import sys

# Initialize pygame and General Setup
pygame.init()
clock = pygame.time.Clock()

# Settting
screen_width = 1280
screen_height = 900
screen_setup = pygame.display.set_mode((screen_width, screen_height))
caption = pygame.display.set_caption("Banji-Pong")




# Player, Rectangle and Ball

while True:
    # Handling Input 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    
    # Updating the window
    pygame.display.flip()
    clock.tick(60)