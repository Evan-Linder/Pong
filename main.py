'''
Evan Linder
Pong Game
Start date: 3/7/23
End date: 
'''


import pygame
import constants, paddles, ball


# Initalize pygame: this is required.
pygame.init()



# setup the window: make it a tuple so it is unmutable and avoid errors.
window = pygame.display.set_mode((constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT))
pygame.display.set_caption(f"Pong Game")

# create the main game loop.
loop_active = True
                                
while loop_active:
    for event in pygame.event.get():
        
        # quit the game
        if event.type == pygame.QUIT:
             loop_active == False
             pygame.quit()
        
        # check if the W or S key is pressed.
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_w: 
                 paddles.paddle_direction_a -= constants.PADDLE_SPEED
            if event.key == pygame.K_s: 
                 paddles.paddle_direction_a += constants.PADDLE_SPEED 


        # stop paddle when key is unpressed (inverse math operations).
        elif event.type == pygame.KEYUP:
             if event.key == pygame.K_w:
                  paddles.paddle_direction_a += constants.PADDLE_SPEED 
             if event.key == pygame.K_s:
                 paddles.paddle_direction_a -= constants.PADDLE_SPEED 


  
    # call the functions from paddles and ball to clean up the code.
    paddles.paddle_a_movement()
    paddles.paddle_b_movement(ball)
    ball.ball_movement()
    

    # set background to red.
    window.fill(constants.RED)
    

    # draw the paddles and ball.
    pygame.draw.rect(window, constants.WHITE, paddles.paddle_a)
    pygame.draw.rect(window, constants.WHITE, paddles.paddle_b)
    pygame.draw.rect(window, constants.WHITE, ball.ball)

    # draw scoring system

    # create a fps controller to avoid lag and screen tearing on low end pc's, set the fps controller tick to 60 Fps.
    fps_controller = pygame.time.Clock()
    fps_controller.tick(constants.FPS)


    # tell the window to update every itteration of the loop. 
    pygame.display.flip()








