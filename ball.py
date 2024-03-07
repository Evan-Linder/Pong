import pygame
import constants

#create the ball.
ball = pygame.Rect(0,0, constants.BALL_SIZE, constants.BALL_SIZE)
ball.center = ((constants.WINDOW_WIDTH * 0.5, constants.WINDOW_HEIGHT * 0.5))
