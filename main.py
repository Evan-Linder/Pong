'''
Evan Linder
Pong Game
Start date: 3/7/23
End date: 
'''


import pygame
import constants
import ball
import paddles

# Initialize pygame: this is required.
pygame.init()

# Setup the window: make it a tuple so it is unmutable and avoid errors.
window = pygame.display.set_mode((constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT))
pygame.display.set_caption("Pong Game")

score_font = pygame.font.SysFont(None, 36)

# Create the main game loop.
loop_active = True
game_started = False

while loop_active:
    for event in pygame.event.get():
        # Quit the game
        if event.type == pygame.QUIT:
            loop_active = False
            pygame.quit()

        # Check if the user clicks the screen to start the game
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_started:
            game_started = True

    # If game has started, execute game logic
    if game_started:
        
        # check if w or s is pressed.
        for event in pygame.event.get(): 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    paddles.paddle_direction_a -= constants.PADDLE_SPEED
                if event.key == pygame.K_s:
                    paddles.paddle_direction_a += constants.PADDLE_SPEED
            # check when the key is released.
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    paddles.paddle_direction_a += constants.PADDLE_SPEED
                if event.key == pygame.K_s:
                    paddles.paddle_direction_a -= constants.PADDLE_SPEED
        
        # call the functions from other documents to simplify the code.
        paddles.paddle_a_movement()
        paddles.paddle_b_movement(ball)
        ball.ball_movement()
        
        window.fill(constants.RED)

        pygame.draw.rect(window, constants.WHITE, paddles.paddle_a)
        pygame.draw.rect(window, constants.WHITE, paddles.paddle_b)
        pygame.draw.rect(window, constants.WHITE, ball.ball)

        # Draw scoring system
        paddle_a_score_image = score_font.render(f'Player 1: {paddles.player_a_score}', True, constants.WHITE)
        window.blit(paddle_a_score_image, (30, 20))
        paddle_b_score_image = score_font.render(f'Player 2: {paddles.player_b_score}', True, constants.WHITE)
        window.blit(paddle_b_score_image, (650, 20))

        # Create a FPS controller to avoid lag and screen tearing on low-end PCs, set the FPS controller tick to 60 FPS.
        fps_controller = pygame.time.Clock()
        fps_controller.tick(constants.FPS)

        # Tell the window to update every iteration of the loop.
        pygame.display.flip()
    else:
        # Display a message to prompt the user to start the game by clicking the screen.
        window.fill(constants.RED)
        start_message = score_font.render("Click anywhere to start the game", True, constants.WHITE)
        window.blit(start_message, (200, constants.WINDOW_HEIGHT * 0.5))
      

        # Update the display.
        pygame.display.flip()
             










