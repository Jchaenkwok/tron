import pygame

# Initialize pygame
pygame.init()

# Create Tron map
screen = pygame.display.set_mode((900, 600))

# Game title
pygame.display.set_caption("Tron")

# Game icon
icon = pygame.image.load('identity_disc.png')
pygame.display.set_icon(icon)

# Blue cycle
blue_bike = pygame.image.load('bluebike.png')
blue_color = (0, 220, 253)
blue_new_bike = blue_bike
blue_angle = 0
blue_bike_x = 217
blue_bike_y = 296

# Starting blue cycle direction and movement
blue_bike_x_change = 0.2
blue_bike_y_change = 0
blue_direction = "East"

# Orange cycle
orange_bike = pygame.image.load('orangebike.png')
orange_color = (253, 133, 0)
orange_new_bike = orange_bike
orange_angle = 0
orange_bike_x = 667
orange_bike_y = 296

# Starting orange cycle direction and movement
orange_bike_x_change = -0.2
orange_bike_y_change = 0
orange_direction = "West"


def build_blue(x, y):
    screen.blit(blue_bike, (x, y))


def build_new_blue(x, y):
    screen.blit(blue_new_bike, (x, y))


def build_new_orange(x, y):
    screen.blit(orange_new_bike, (x, y))


def build_orange(x, y):
    screen.blit(orange_bike, (x, y))


blue_x_initial = 217
blue_y_initial = 296
orange_x_initial = 667
orange_y_initial = 296


# Game
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Direction control
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                blue_bike_y_change = 0.2
                blue_bike_x_change = 0
                blue_angle = 90
                blue_new_bike = pygame.transform.rotate(blue_bike, blue_angle)

            if event.key == pygame.K_s:
                blue_bike_y_change = -0.2
                blue_bike_x_change = 0
                blue_angle = 270
                blue_new_bike = pygame.transform.rotate(blue_bike, blue_angle)

            if event.key == pygame.K_a:
                blue_bike_x_change = -0.2
                blue_bike_y_change = 0
                blue_angle = 180
                blue_new_bike = pygame.transform.rotate(blue_bike, blue_angle)

            if event.key == pygame.K_d:
                blue_bike_x_change = 0.2
                blue_bike_y_change = 0
                blue_angle = 0
                blue_new_bike = pygame.transform.rotate(blue_bike, blue_angle)

            if event.key == pygame.K_UP:
                orange_bike_y_change = +0.2
                orange_bike_x_change = 0
                orange_angle = 90
                orange_new_bike = pygame.transform.rotate(orange_bike, orange_angle)

            if event.key == pygame.K_DOWN:
                orange_bike_y_change = -0.2
                orange_bike_x_change = 0
                orange_angle = 270
                orange_new_bike = pygame.transform.rotate(orange_bike, orange_angle)

            if event.key == pygame.K_LEFT:
                orange_bike_x_change = -0.2
                orange_bike_y_change = 0
                orange_angle = 180
                orange_new_bike = pygame.transform.rotate(orange_bike, orange_angle)

            if event.key == pygame.K_RIGHT:
                orange_bike_x_change = 0.2
                orange_bike_y_change = 0
                orange_angle = 0
                orange_new_bike = pygame.transform.rotate(orange_bike, orange_angle)

    # Background color
    screen.fill((0, 0, 0))

    # Change direction
    blue_bike_x += blue_bike_x_change
    blue_bike_y -= blue_bike_y_change

    orange_bike_x += orange_bike_x_change
    orange_bike_y -= orange_bike_y_change

    # Create light cycles
    build_new_blue(blue_bike_x, blue_bike_y)
    build_new_orange(orange_bike_x, orange_bike_y)


    # set var for initial position and replace in draw rect set width to current x or heigh to current y. when change dir change initial pos
    blue_trail = pygame.Rect(blue_x_initial, blue_y_initial + 2, blue_x_initial + blue_bike_x, 2)
    orange_trail = pygame.Rect(orange_bike_x + 16, orange_y_initial + 2, orange_x_initial - orange_bike_x, 2)

    pygame.draw.rect(screen, orange_color, orange_trail, 0)
    pygame.draw.rect(screen, blue_color, blue_trail, 0)

    pygame.display.update()
