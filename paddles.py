import pygame
import constants, ball


# paddle A: aligns paddle in the middle of the screen, 20 pixels off the edge.
paddle_a = pygame.Rect(0, 0, constants.PADDLE_WIDTH, constants.PADDLE_HEIGHT)
paddle_a.centery = constants.WINDOW_HEIGHT * 0.5
paddle_a.left = constants.PADDLE_OFFSET_X
paddle_direction_a = 0
player_a_score = 0

# paddle B: aligns paddle in the middle of the screen, 20 pixels off the edge.
paddle_b = pygame.Rect(0, 0, constants.PADDLE_WIDTH, constants.PADDLE_HEIGHT)
paddle_b.centery = constants.WINDOW_HEIGHT * 0.5
paddle_b.right = constants.WINDOW_WIDTH - constants.PADDLE_OFFSET_X
paddle_direction_b = 0
player_b_score = 0

#movement of paddle A.
def paddle_a_movement():
     
    paddle_a.y += paddle_direction_a  

    if paddle_a.top < 0:
         paddle_a.top = 0
    elif paddle_a.bottom > constants.WINDOW_HEIGHT:
         paddle_a.bottom = constants.WINDOW_HEIGHT

# Define AI movement for paddle B
def paddle_b_movement(ball):
    global paddle_direction_b

    # Get the target range
    target_range_y = ball.ball.centery

    # Adjust paddle B towards the vertical position of the ball
    target_speed = (target_range_y - paddle_b.centery) * 0.2
    paddle_direction_b += (target_speed - paddle_direction_b) * 0.1
    paddle_b.y += paddle_direction_b
    

    # Ensure paddle B stays within the game boundaries
    if paddle_b.top < 0:
        paddle_b.top = 0
    elif paddle_b.bottom > constants.WINDOW_HEIGHT:
        paddle_b.bottom = constants.WINDOW_HEIGHT
     

    













