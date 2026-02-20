import pygame
pygame.init()

#screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

#player
player_size = 40
player_speed = 20
player_x = screen_width / 2 - player_size / 2
player_y = screen_height / 2 - player_size / 2
player_rect = pygame.Rect(player_x, player_y, player_size, player_size)

def player_movment(player_speed, player_rect):

    direction_x = None
    direction_y = None

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        direction_y = "UP"
    if keys[pygame.K_s]:
        direction_y = "DOWN"
    if keys[pygame.K_a]:
        direction_x = "LEFT"
    if keys[pygame.K_d]:
        direction_x = "RIGHT"

    dy = 0
    dx = 0
    if direction_y == "UP" and direction_x == "LEFT":
        dy -= player_speed / 1.5
        dx -= player_speed / 1.5
    elif direction_y == "UP" and direction_x == "RIGHT":
        dy -= player_speed / 1.5
        dx += player_speed / 1.5
    elif direction_y == "DOWN" and direction_x == "LEFT":
        dy += player_speed / 1.5
        dx -= player_speed / 1.5
    elif direction_y == "DOWN" and direction_x == "RIGHT":
        dy += player_speed / 1.5
        dx += player_speed / 1.5
    elif direction_x == "LEFT":
        dx -= player_speed
    elif direction_x == "RIGHT":
        dx += player_speed
    elif direction_y == "UP":
        dy -= player_speed
    elif direction_y == "DOWN":
        dy += player_speed
    player_rect.y += dy
    player_rect.x += dx
    return player_speed, player_rect
