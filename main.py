import pygame
from menu import Menu, GameOver
from game import Game

class Main:

    def __init__(self, sizex, sizey, title):
        pygame.init()
        
        pygame.mixer.init()
        pygame.mixer.music.load("assets/sounds/bg.ogg")
        pygame.mixer.music.play(-1)
        
        self.window = pygame.display.set_mode([sizex, sizey])
        self.title = pygame.display.set_caption(title)

        self.menu = Menu("assets/start.png")
        self.game = Game()
        self.gameover = GameOver("assets/gameover.png")
        
        self.loop = True

        self.fps = pygame.time.Clock()
    

    def draw(self):
        if self.menu.change_scene == False:
            self.menu.draw(self.window)
        elif not self.game.change_scene:
            self.game.draw(self.window)
            self.game.update()
        elif not self.gameover.change_scene:
            self.gameover.draw(self.window)
        else:
            self.menu.change_scene = False
            self.game.change_scene = False
            self.gameover.change_scene = False
            self.game.abelha.life = 3
            self.game.abelha.pts = 0

    def events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT: 
                self.loop = False
            if self.menu.change_scene == False:    
                self.menu.events(events)
            elif not self.game.change_scene:
                 self.game.abelha.move_abelha(events)
            else: self.gameover.events(events)
            
    def update(self):
        while self.loop:
            self.fps.tick(30) 
            self.draw()
            self.events()
            pygame.display.update()

pygame.font.init()
game = Main(360, 640, "BeeHoney")
game.update()
