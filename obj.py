import pygame


class Obj:

    def __init__(self, image, x, y):

        self.group = pygame.sprite.Group()
        self.sprite = pygame.sprite.Sprite(self.group)

        self.sprite.image = pygame.image.load(image)
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect[0] = x
        self.sprite.rect[1] = y
        
        self.frame = 1
        self.tick = 0

    def drawing(self, window):
        self.group.draw(window)

    def anim(self, image, tick, frames):
        self.tick += 1
        if self.tick == tick:
            self.tick = 0
            self.frame += 1
        
        if self.frame == frames:
            self.frame = 1
            
        self.sprite.image = pygame.image.load("assets/"+ image + str(self.frame) + ".png")
        
class Abelha(Obj):
    
    def __init__(self, image, x, y):
        super().__init__(image, x, y)
        self.life = 3
        self.pts = 0
        
        pygame.mixer.init()
        self.som_pts = pygame.mixer.Sound("assets/sounds/score.ogg")
        self.som_dano = pygame.mixer.Sound("assets/sounds/bateu.ogg")
        
    def move_abelha(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.sprite.rect[0] = pygame.mouse.get_pos()[0] -32
            self.sprite.rect[1] = pygame.mouse.get_pos()[1] -32
            
    def colisao(self, group, name):
        
        name = name
        colison = pygame.sprite.spritecollide(self.sprite, group, True)
        
        if name == "Flower" and colison:
            self.pts += 1
            self.som_pts.play()
        elif name == "Spider" and colison:
            self.life -= 1
            self.som_dano.play()
class Text:
    
    def __init__ (self, size, text):
        
        self.font = pygame.font.SysFont("Aria bold", size, False, False)
        self.render = self.font.render(text, False, (255,255,255))
        
    def draw(self, window, x, y):
        window.blit(self.render, (x, y))
        
    def update_text(self, update):
        self.render = self.font.render(update, False, (255, 255, 255))