import pgzrun
import math


# Set screen width and height.
WIDTH = 600
HEIGHT = 400

# Define colours.
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Speed of the player.
PLAYER_SPEED = 5

# Distance along a 45 degree diagonal vector.
DIAGONAL_DISTANCE = math.hypot(1,1)


# Player entity.
player = Rect((WIDTH / 2, HEIGHT / 2), (16, 16))


def normalise_diagonal(vec):
    """ Normalise a vector along the diagonal. """
    return (vec[0] / DIAGONAL_DISTANCE, vec[1] / DIAGONAL_DISTANCE)


def draw():
    screen.clear()
    screen.fill(BLUE)
    screen.draw.filled_rect(player, YELLOW)
    screen.draw.text("- Untitled -", (0, 0))


def update():
    player_dx = 0
    player_dy = 0

    if keyboard.left:
        player_dx -= 1
    
    if keyboard.right:
        player_dx += 1
    
    if keyboard.up:
        player_dy -= 1
    
    if keyboard.down:
        player_dy += 1

    player_dx, player_dy = normalise_diagonal((player_dx, player_dy))
    player.move_ip(player_dx * PLAYER_SPEED, player_dy * PLAYER_SPEED)


pgzrun.go()