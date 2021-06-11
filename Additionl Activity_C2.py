# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 18:52:07 2021

@author: dell
"""

import pygame,sys
from pygame.locals import *
 
# 2 - Initialize the game
pygame.init()
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
 
width, height = 64*10, 64*8
screen=pygame.display.set_mode((width, height))
player_x = 200
player_y = 200
keys = [False, False, False, False]
 
# 3 - Load images
player = pygame.image.load("enemy.png")
 
# 4 - keep looping through
while 1:
 
    # 5 - clear the screen before drawing it again
    screen.fill((255,255,255))
    # 6 - draw the screen elements
    screen.blit(player, (player_x, player_y))
 
    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit() 
            sys.exit(0) 
        if event.type == pygame.KEYDOWN:
                           
            if event.key==pygame.K_UP:
                keys[0]=True
            elif event.key==pygame.K_LEFT:
                keys[1]=True
            elif event.key==pygame.K_DOWN:
                keys[2]=True
            elif event.key==pygame.K_RIGHT:
                keys[3]=True
 
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_UP:
                keys[0]=False
            elif event.key==pygame.K_LEFT:
                keys[1]=False
            elif event.key==pygame.K_DOWN:
                keys[2]=False
            elif event.key==pygame.K_RIGHT:
                keys[3]=False
    # Update the y position
    # If the up button is pressed
    if keys [0]: 
         if player_y> 0:     # If the coordinate is greater than 0 (not outside the playing field)
             player_y  = player_y-15 # Change the y position by 15 pixels. The player moves upwards
    # If the down key is pressed
    elif keys [2]: 
         if player_y <height-64: # If the coordinate is less than the height of the playing field
             player_y  = player_y+15     # Change the y position by 15 pixels. The player goes down
    # Update x-position
    # If the left key is pressed
    if keys [1]: 
         if player_x> 0:      # If the player is inside the playing field
             player_x  = player_x-15  # Decrease x position. The player goes left
    # If the right key is pressed
    elif keys [3]: 
         if player_x <width-64: # If the player is inside the playing field
             player_x  = player_x+15    # Increase x position. The player goes right
