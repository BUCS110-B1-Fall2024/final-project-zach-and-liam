# Added Some Basic Functions Mentioned In Milestone 2, Will Add More Later
import pygame
from model_a import Snake, Eatable_Object

class Controller:
  
  def __init__(self):
    #setup pygame data
    
  def mainloop(self):
   while(True):
   
    #select state loop
    
  
  ### below are some sample loop states ###

  def menuloop(self):
    
      #event loop

      #update data

      #redraw
      
  def gameloop(self):
      pygame.display.flip()
      
      #event loop

      #update data

      #redraw
    
  def gameoverloop(self):
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
         pygame.quit() 
         exit()
      
      
      #event loop

      #update data

      #redraw
