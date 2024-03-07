import pygame
import constants, paddles, fpsController

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
             pygame.QUIT()
        
        # check if the W or S key is pressed.
        elif event.type == pygame.KEYDOWN: 

            # if w is pressed move paddles up on the y axis.
            if event.key == pygame.K_w: 
                 paddles.paddle_a_velocity -= constants.PADDLE_SPEED
            # if s is pressed move paddles down on the y axis.
            if event.key == pygame.K_s: 
                 paddles.paddle_a_velocity += constants.PADDLE_SPEED 

        # stop paddle when key is unpressed (inverse math operations).
        elif event.type == pygame.KEYUP:
             if event.key == pygame.K_w:
                  paddles.paddle_a_velocity += constants.PADDLE_SPEED 
             if event.key == pygame.K_s:
                 paddles.paddle_a_velocity -= constants.PADDLE_SPEED 


  

    #movement of paddle A        
    paddles.paddle_a.y += paddles.paddle_a_velocity  

    if paddles.paddle_a.top < 0:
         paddles.paddle_a.top = 0
    elif paddles.paddle_a.bottom > constants.WINDOW_HEIGHT:
         paddles.paddle_a.bottom = constants.WINDOW_HEIGHT

    #set background to red.
    window.fill(constants.RED)

    #draw paddle A
    pygame.draw.rect(window, constants.WHITE, paddles.paddle_a)
    pygame.draw.rect(window, constants.WHITE, paddles.paddle_b)


    pygame.display.flip()

    #set the fps controller tick (60 Fps).
    fpsController.fps_controller.tick(constants.FPS)










