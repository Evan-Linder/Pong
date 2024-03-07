import pygame
import constants, paddles, fpsController, ball


#Initalize pygame: this is required.
pygame.init()



# setup the window: make it a tuple so it is unmutable and avoid errors.
window = pygame.display.set_mode((constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT))
pygame.display.set_caption(f"Evan's Pong Game")

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

            # if w is pressed move paddle A up on the y axis.
            if event.key == pygame.K_w: 
                 paddles.paddle_direction_a -= constants.PADDLE_SPEED
            # if s is pressed move paddle A down on the y axis.
            if event.key == pygame.K_s: 
                 paddles.paddle_direction_a += constants.PADDLE_SPEED 

        # stop paddle when key is unpressed (inverse math operations).
        elif event.type == pygame.KEYUP:
             if event.key == pygame.K_w:
                  paddles.paddle_direction_a += constants.PADDLE_SPEED 
             if event.key == pygame.K_s:
                 paddles.paddle_direction_a -= constants.PADDLE_SPEED 


  
    #call the function from paddles to clean up code.
    paddles.paddle_a_movement()
    ball.ball_movement()
    

    #set background to red.
    window.fill(constants.RED)

    #draw paddles and the ball.
    pygame.draw.rect(window, constants.WHITE, paddles.paddle_a)
    pygame.draw.rect(window, constants.WHITE, paddles.paddle_b)
    pygame.draw.rect(window, constants.WHITE, ball.ball)



    pygame.display.flip()

    #set the fps controller tick (60 Fps).
    fpsController.fps_controller.tick(constants.FPS)










