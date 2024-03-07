import pygame
import constants, paddles

#Initalize pygame: this is required
pygame.init()



#setup the window: make it a tuple so it is unmutable
window = pygame.display.set_mode((constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT))
pygame.display.set_caption(f"Evan's Pong Game")

#create the main game loop
loop_active = True
                                
while loop_active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             #quit the game
             loop_active == False
             pygame.quit()
                
    
    #set background to red
    window.fill(constants.RED)

    #draw paddle A
    pygame.draw.rect(window, constants.WHITE, paddles.paddle_a)


    pygame.display.flip()







