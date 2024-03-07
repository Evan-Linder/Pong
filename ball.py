import pygame
import constants, paddles

# create the ball.
ball = pygame.Rect(0,0, constants.BALL_SIZE, constants.BALL_SIZE)
ball.center = ((constants.WINDOW_WIDTH * 0.5, constants.WINDOW_HEIGHT * 0.5))


# movement of the ball.
ball_direction_x = constants.BALL_SPEED
ball_direction_y = constants.BALL_SPEED

# make the ball bounce only off the paddles and top and bottom edge.
def ball_movement():
    #avoid errors, cannot change global variables within functions.
    global ball_direction_x, ball_direction_y

    ball.x += ball_direction_x
    ball.y += ball_direction_y
    
    #paddles (reverses x direction using colliderect only if it hits the paddle).
    if ball.colliderect(paddles.paddle_a) or ball.colliderect(paddles.paddle_b):
        ball_direction_x *= -1


    
    #top and bottom (reverses y direction)
    if ball.top < 0:
        ball.top = 0
        ball_direction_y *= -1

    elif ball.bottom > constants.WINDOW_HEIGHT:
        ball.bottom = constants.WINDOW_HEIGHT
        ball_direction_y *= -1
