import pygame
import constants

#paddle A: aligns paddle in the middle of the screen and 20 pixels off the edge 
paddle_a = pygame.Rect(0, 0, constants.PADDLE_WIDTH, constants.PADDLE_HEIGHT)
paddle_a.centery = constants.WINDOW_HEIGHT * 0.5
paddle_a.left = constants.PADDLE_OFFSET_X

#paddle B: aligns paddle in the middle of the screen and 20 pixels off the edge the opposite side of A
paddle_b = pygame.Rect(0, 0, constants.PADDLE_WIDTH, constants.PADDLE_HEIGHT)
paddle_b.centery = constants.WINDOW_HEIGHT * 0.5
paddle_b.right = constants.WINDOW_WIDTH - constants.PADDLE_OFFSET_X












