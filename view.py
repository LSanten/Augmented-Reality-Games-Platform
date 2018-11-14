"""this file will contain all the views from all the different models
    We did this so we can easily switch between them"""

import pygame
class View():
    """this might have the views of all the different screens so we can make an overall UI"""
    def __init__(self,screenSize,model):
        self.screen_size = screenSize
        self.screen = pygame.display.set_mode(screenSize)
        self.model = model
        self.model.screen = self.screen
        pygame.display.set_caption = ("AR-Arcade")

    def draw(self):
        if self.model.organizer.state == "pong":
            #we will probably not use this
            pass
        if self.model.organizer.state == "spaceInvaders":
            #we will probably not use this
            pass

        if self.model.organizer.state == "homeScreen":
            #self.screen.fill(0,0,0)
            newSurface = pygame.surfarray.make_surface(self.model.cameraImage) # Reads the stored camera image and makes a surface out of it
            self.screen.blit(newSurface,(0,0)) # Make background of the sufrace (so it becomes live video)
            #draw squares for buttons for pong and spaceinvaders
            pygame.draw.rect(self.screen, (250,250,0), pygame.Rect(50, self.model.height/2-50, 200,200))
            pygame.draw.rect(self.screen, (250,250,0), pygame.Rect(300, self.model.height/2-50, 200,200))
            self.model.cursor.draw(self.screen)
            pygame.display.update()