import pygame
import constants


# paddle A: aligns paddle in the middle of the screen, 20 pixels off the edge.
paddle_a = pygame.Rect(0, 0, constants.PADDLE_WIDTH, constants.PADDLE_HEIGHT)
paddle_a.centery = constants.WINDOW_HEIGHT * 0.5
paddle_a.left = constants.PADDLE_OFFSET_X
paddle_direction_a = 0

# paddle B: aligns paddle in the middle of the screen, 20 pixels off the edge.
paddle_b = pygame.Rect(0, 0, constants.PADDLE_WIDTH, constants.PADDLE_HEIGHT)
paddle_b.centery = constants.WINDOW_HEIGHT * 0.5
paddle_b.right = constants.WINDOW_WIDTH - constants.PADDLE_OFFSET_X
paddle_direction_b = 0

#movement of paddle A.
def paddle_a_movement():
     
    paddle_a.y += paddle_direction_a  

    if paddle_a.top < 0:
         paddle_a.top = 0
    elif paddle_a.bottom > constants.WINDOW_HEIGHT:
         paddle_a.bottom = constants.WINDOW_HEIGHT

# Define AI movement for paddle B
def paddle_b_movement(ball):

    # Get the vertical position of the ball
    ball_center_y = ball.ball.centery

    # Adjust paddle B towards the vertical position of the ball
    if paddle_b.centery < ball_center_y:
        paddle_b.y += constants.PADDLE_SPEED
    elif paddle_b.centery > ball_center_y:
        paddle_b.y -= constants.PADDLE_SPEED

    # Ensure paddle B stays within the game boundaries
    if paddle_b.top < 0:
        paddle_b.top = 0
    elif paddle_b.bottom > constants.WINDOW_HEIGHT:
        paddle_b.bottom = constants.WINDOW_HEIGHT
     

    













