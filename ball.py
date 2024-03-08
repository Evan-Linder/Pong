import pygame, constants, paddles, random



# allignment of the ball
ball = pygame.Rect(0,0, constants.BALL_SIZE, constants.BALL_SIZE)
ball.center = ((constants.WINDOW_WIDTH * 0.5, constants.WINDOW_HEIGHT * 0.5))


# movement of the ball.
ball_direction_x = constants.BALL_SPEED
ball_direction_y = constants.BALL_SPEED


# reset the ball to the center.
def reset_ball():

    global ball_direction_x, ball_direction_y
    
    ball.center = ((constants.WINDOW_WIDTH * 0.5, constants.WINDOW_HEIGHT * 0.5))
    ball_direction_x = random.choice([-1,1]) * constants.BALL_SIZE
    ball_direction_y = random.choice([-1,1]) * constants.BALL_SIZE



# make the ball bounce only off the paddles and  the top/bottom edge.
def ball_movement():
    global ball_direction_x, ball_direction_y

    ball.x += ball_direction_x
    ball.y += ball_direction_y


    # Paddles (reverses x axis direction using colliderect only if it hits the paddle).
    if ball.colliderect(paddles.paddle_a) or ball.colliderect(paddles.paddle_b):
        ball_direction_x *= -1
    

    # Top and bottom (reverses y axis direction)
    if ball.top < 0:
        ball.top = 0
        ball_direction_y *= -1
    elif ball.bottom > constants.WINDOW_HEIGHT:
        ball.bottom = constants.WINDOW_HEIGHT
        ball_direction_y *= -1


    # Check if ball has gone out of bounds add a point and reset if necessary.
    if ball.right > constants.WINDOW_WIDTH:
         paddles.player_a_score += 1
         reset_ball()
    elif ball.left < 0: 
         paddles.player_b_score += 1 
         reset_ball()
    
    
