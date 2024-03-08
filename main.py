'''
Evan Linder
Pong Impossible
Start date: 3/7/23
End date: 
'''
import pygame, paddles, constants, ball

 # Initialize pygame: this is required. (made into a function so it can be called at the end.)
def run_game():
   
    pygame.init()

    # Setup the window: make it a tuple so it is unmutable and avoid errors.
    window = pygame.display.set_mode((constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT))
    pygame.display.set_caption("Pong Impossible")

    score_font = pygame.font.SysFont(None, 36)

    # Set initial game state
    loop_active = True
    game_started = False

    while loop_active:
        for event in pygame.event.get():
            # Quit the game
            if event.type == pygame.QUIT:
                loop_active = False
                pygame.quit()
                

            # Check if the W or S key is pressed.
            elif event.type == pygame.KEYDOWN and game_started:
                if event.key == pygame.K_w:
                    paddles.paddle_direction_a -= constants.PADDLE_SPEED
                elif event.key == pygame.K_s:
                    paddles.paddle_direction_a += constants.PADDLE_SPEED

            # Stop paddle when key is unpressed (inverse math operations).
            elif event.type == pygame.KEYUP and game_started:
                if event.key == pygame.K_w:
                    paddles.paddle_direction_a += constants.PADDLE_SPEED
                elif event.key == pygame.K_s:
                    paddles.paddle_direction_a -= constants.PADDLE_SPEED

            # Check if the user clicks the screen to start the game
            elif event.type == pygame.MOUSEBUTTONDOWN and not game_started:
                game_started = True

        # If game has started, execute game logic
        if game_started:
            paddles.paddle_a_movement()
            paddles.paddle_b_movement(ball)
            ball.ball_movement()

            window.fill(constants.RED)

            # draw game objects
            pygame.draw.rect(window, constants.WHITE, paddles.paddle_a)
            pygame.draw.rect(window, constants.WHITE, paddles.paddle_b)
            pygame.draw.rect(window, constants.WHITE, ball.ball)

            # Draw scoring system
            paddle_a_score_image = score_font.render(f'Player 1: {paddles.player_a_score}', True, constants.WHITE)
            window.blit(paddle_a_score_image, (30, 20))
            paddle_b_score_image = score_font.render(f'Player 2: {paddles.player_b_score}', True, constants.WHITE)
            window.blit(paddle_b_score_image, (650, 20))

            # check if player 1 or 2 has gotten to 5
            if paddles.player_a_score >= 5 or paddles.player_b_score >= 5:
                loop_active = False

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

    # After loop ends, display winner message
    window.fill(constants.RED)

    # Determine the winner
    if paddles.player_a_score >= 5:
        winner_message = score_font.render("You beat the impossible!", True, constants.WHITE)
    else:
        winner_message = score_font.render("You weren't good enough! ", True, constants.WHITE)

    # Display the winner message
    window.blit(winner_message, (200, constants.WINDOW_HEIGHT * 0.5))

    # Update the display.
    pygame.display.flip()

    # Wait for a click to restart the game
    waiting_for_click = True
    while waiting_for_click:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                waiting_for_click = False

    # Reset game scores and restart the game
    paddles.player_a_score = 0
    paddles.player_b_score = 0
    run_game()

# Run the game again
run_game()




            












