import pygame
import sys

# Initialize pygame and General Setup
pygame.init()
clock = pygame.time.Clock()

# Settting
screen_width = 1280
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))
caption = pygame.display.set_caption("11:11  PM ❤️🍭")




# Player, Rectangle and Ball
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height - 150, 10, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)
background_color = pygame.Color(139,0,139)
light_grey = (200, 200, 200)


# Ball Speed
ball_speed_x = 7
ball_speed_y = 7

while True:
    # Handling Input 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    # Ball Movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    # Ball Collisions to the Wall
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1
        
    # Visuals
    screen.fill(background_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height))
    # Updating the window
    pygame.display.flip()
    clock.tick(60)