from obj import Obj, Abelha, Text
import random

class Game:
    
    def __init__(self):
        
        self.bg = Obj("assets/bg.png", 0, 0)
        self.bg2 = Obj("assets/bg.png", 0, -640)
        self.spider = Obj("assets/spider_0001.png", random.randrange(0,320), -70)
        self.flower = Obj("assets/florwer1.png", random.randrange(0,320), -70)
        self.abelha = Abelha("assets/bee01.png", 150, 550)
        
        self.change_scene = False
        
        self.velo_spider = 7
        
        self.score = Text(100, "0")
        self.lifes = Text(60, "3")
        
    def draw (self, window):
        self.bg.drawing(window)
        self.bg2.drawing(window)
        self.abelha.drawing(window)
        self.spider.drawing(window)
        self.flower.drawing(window)
        self.score.draw(window, 155, 20)
        self.lifes.draw(window, 20, 20)
        self.score.update_text(str(self.abelha.pts))
        self.lifes.update_text(str(self.abelha.life))
        
    def update(self):
        self.move_bg()
        self.spider.anim("spider_000", 2, 17)
        self.flower.anim("florwer", 8, 3)
        self.abelha.anim("bee0", 3, 7)
        self.abelha.colisao(self.spider.group, "Spider")
        self.abelha.colisao(self.flower.group, "Flower")
        self.move_spiders()
        self.move_flower()
        self.game_over()
    
    def move_bg(self):
        self.bg.sprite.rect[1] += 4
        self.bg2.sprite.rect[1] += 4
        
        if self.bg.sprite.rect[1] >= 640:
            self.bg.sprite.rect[1] = 0
            
        if self.bg2.sprite.rect[1] >= 0:
            self.bg2.sprite.rect[1] = -640
            
    def move_spiders(self):
        self.spider.sprite.rect[1]+= self.velo_spider
        
        if self.spider.sprite.rect[1] >= 700:
            self.spider.sprite.kill()
            self.spider = Obj ("assets/spider_0001.png",  random.randrange(0,320), -70)
            self.velo_spider += 1
            
    def move_flower(self):
        self.flower.sprite.rect[1]+= 5
        
        if self.flower.sprite.rect[1] >= 700:
            self.flower.sprite.kill()
            self.flower = Obj ("assets/florwer1.png",  random.randrange(0,320), -70)
            
    def game_over(self):
        if self.abelha.life <= 0:
            self.change_scene = True
            self.velo_spider = 7
            