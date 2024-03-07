import pygame
import constants

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
            loop_active == False
    
    #set background to red
    window.fill(constants.RED)

    pygame.display.flip()

#quit the game
pygame.quit()





