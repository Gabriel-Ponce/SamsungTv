import pygame
from samsungapi import SamsungAPI


class Controller():
    '''
    Class that creates the tv controller interface in pygame
    '''
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('TV Controller')
        
        self.samsung = SamsungAPI()

        self.resolution = (720, 720)
       
        self.isrunning = True

        self.screen = pygame.display.set_mode(self.resolution)
        self.screen.fill((255,255,255))

        self.method = ["", ""]
        self.buttons = [
            [(255,255,255), [250, 20], [65, 40], "power", "shortcuts"],
            [(0,0,255), [400, 20], [65, 40], "source", "shortcuts"],
            [(0,255,0), [255, 210], [65, 40], "volume_up", "shortcuts"],
            [(0,255,0), [255, 260], [65, 40], "volume_down", "shortcuts"],
            [(255,0,0), [400, 210], [65, 40], "volume_up", "shortcuts"],
            [(255,0,0), [400, 260], [65, 40], "volume_down", "shortcuts"],
            [(0,255,0), [335, 213], [55, 30], "mute", "shortcuts"],
            [(255,0,0), [255, 307], [55, 30], "menu", "shortcuts"],
            [(255,255,0), [335, 300], [55, 30], "home", "shortcuts"],
            [(255,0,0), [255, 347], [55, 30], "tools", "shortcuts"],
            [(255,0,0), [333, 347], [55, 30], "up", "shortcuts"],
            [(255,0,0), [255, 387], [65, 30], "left", "shortcuts"],
            [(255,0,0), [400, 387], [65, 30], "right", "shortcuts"],
            [(255,0,0), [333, 430], [55, 30], "down", "shortcuts"],
            [(255,0, 255), [333, 390], [55, 30], "enter", "shortcuts"],
            [(0,0,255), [255, 430], [65, 30], "back", "shortcuts"],
            [(0,0,255), [400, 430], [65, 30], "back", "shortcuts"],

        ]
        
        self.i_controller = pygame.image.load('TV_Remote.jpg')
        self.I_CONTROLLER = pygame.transform.scale(self.i_controller, (300,650))
        self.screen.blit(self.I_CONTROLLER, ((720/2)-(300/2),0))
      
        

    def execute(self):
        
            
        pygame.display.flip()
        
        self.mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            for color, coors, rect, shortcut, method in self.buttons:
                
                
                self.surface = pygame.Surface(rect)
                self.surface.fill(color)
                self.surface.set_alpha(0)
                self._rect = self.screen.blit(self.surface, coors)
                
                
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] and self._rect.collidepoint(self.mouse):
                    self.method = [shortcut, method]
                    self.samsung.commandShortcut(shortcut, method)
                    print(self.method)
                    self.method = ['', '']
            if event.type == pygame.QUIT:
                self.isrunning = False





        


