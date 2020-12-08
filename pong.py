import pygame
import sys
import random


# Initialize pygame and General Setup
pygame.init()
clock = pygame.time.Clock()



# Ball Movement Function
def ball_animation():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    # Wall Collision
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_restart()
    # Player Collision
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1


def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))
# Player Movement
def player_movement():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

# Opponent Movement
def opponent_movement():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

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
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
# Player Speed
player_speed = 0
# Opponent Speed
opponent_speed = 7
while True:
    # Handling Input 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # KEYDOWN 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        # KEYUP   
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7
                
    # Ball Movement and Collision 
    ball_animation()
    
    # Player movement
    player_movement()
    
    # Opponent Movement
    opponent_movement()
    
    
    # Visuals
    screen.fill(background_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height))
    # Updating the window
    pygame.display.flip()
    clock.tick(60)