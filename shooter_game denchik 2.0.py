#Создай собственный Шутер!
from pygame import *
from random import *
numb = 0
font.init()
font1 = font.SysFont("Arial",36)
wind = display.set_mode((1000,700))
display.set_caption("")
back = transform.scale(image.load("snowblack.jpg"), (1000,700))
clock = time.Clock()
bulets = sprite.Group()
score = 0
trash = True
trash1 = True
trash2 = True
trash3 = True
trash4 = True
class GameSprite(sprite.Sprite):
    def __init__(self,plyer_image,player_x,player_y, size_x, size_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(plyer_image),(size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def showhero(self):
        wind.blit(self.image,(self.rect.x,self.rect.y))
    def uprawlen(self):
        keys = key.get_pressed()
        if keys[K_a]:
            self.rect.x -= self.speed
        if keys[K_d]:
            self.rect.x += self.speed
    def update(self):
        global numb 
        self.rect.y += self.speed
        if self.rect.y > 740 :
            self.rect.y = -20
            self.rect.x = randint(40,960)
            self.speed = randint(3,4)
            numb += 1
    def fire(self):
        bullet = Bullet("sus.png", self.rect.x, self.rect.y,50,50,15 )
        bulets.add(bullet)

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 5:
            self.kill()
FPS = 60
game = True
game1 = False
game2 = False
game3 = False
game4 = False
sprite1 = GameSprite("lisa.png",50,600,100,100,15)
monsters = sprite.Group()
for i in range (25):
    monster = GameSprite("polise.png", randint(40,960), -20,100,100, randint(2,2))
    monsters.add(monster)

while game:
    wind.blit(back,(0,0))
    sprite1.showhero()
    monsters.draw(wind)
    bulets.draw(wind)
    sprite1.uprawlen()
    monsters.update()
    bulets.update()
    clock.tick(FPS)
    text_lose = font1.render("вас поймали "+str(numb)+" полицаев",1,(255,255,255))
    wind.blit(text_lose,(10,20))
    if sprite.groupcollide(monsters, bulets, True, True):
            score += 1
            monster = GameSprite("polise.png", randint(40,960), -20,100,100, randint(2,2))
            monsters.add(monster)
    text_score = font1.render(str(score)+" полицаев вкинулось",1,(255,255,255))
    wind.blit(text_score,(10,50))
    kp = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            game = False
        
        if kp[K_SPACE]:
            sprite1.fire()
    if trash != False:
        if score >= 100 :
            back = transform.scale(image.load("vostan1.jpg"), (1000,700))
            trash = False
            for i in range (50):
                monster = GameSprite("polise.png", randint(40,960), -20,100,100, randint(2,2))
                monsters.add(monster)
            game = False
            game1 = True
    if numb >= 100:
        back = transform.scale(image.load("sneg.jpg"), (1000,700))
    if numb >= 200:
        back = transform.scale(image.load("failniga.jpg"), (1000,700))
        text_def = font1.render("ВЫ ПРОИГРАЛИ",50,(255,255,255))
        wind.blit(text_def,(100,100))
        game = False        
    display.update()

while game1:
    wind.blit(back,(0,0))
    sprite1.showhero()
    monsters.draw(wind)
    bulets.draw(wind)
    sprite1.uprawlen()
    monsters.update()
    bulets.update()
    clock.tick(FPS)
    text_lose = font1.render("вас поймали "+str(numb)+" полицаев",1,(255,255,255))
    wind.blit(text_lose,(10,20))
    if sprite.groupcollide(monsters, bulets, True, True):
            score += 1
            monster = GameSprite("polise.png", randint(40,960), -20,100,100, randint(2,2))
            monsters.add(monster)
    text_score = font1.render(str(score)+" полицаев вкинулось",1,(255,255,255))
    wind.blit(text_score,(10,50))
    kp = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            game1 = False
        if kp[K_SPACE]:
            sprite1.fire()
    if trash1 != False:
        if score >= 250 :
            back = transform.scale(image.load("vostan1.jpg"), (1000,700))
            trash1 = False
            for i in range (75):
                monster = GameSprite("polise.png", randint(40,960), -20,100,100, randint(2,2))
                monsters.add(monster)
            game1 = False
            game2 = True
    if numb >= 100:
        back = transform.scale(image.load("sneg.jpg"), (1000,700))
    if numb >= 200:
        back = transform.scale(image.load("failniga.jpg"), (1000,700))
        text_def = font1.render("ВЫ ПРОИГРАЛИ",50,(255,255,255))
        wind.blit(text_def,(100,100))
        game1 = False        
    display.update()

while game2:
    wind.blit(back,(0,0))
    sprite1.showhero()
    monsters.draw(wind)
    bulets.draw(wind)
    sprite1.uprawlen()
    monsters.update()
    bulets.update()
    clock.tick(FPS)
    text_lose = font1.render("вас поймали "+str(numb)+" полицаев",1,(255,255,255))
    wind.blit(text_lose,(10,20))
    if sprite.groupcollide(monsters, bulets, True, True):
            score += 1
            monster = GameSprite("polise.png", randint(40,960), -20,100,100, randint(2,2))
            monsters.add(monster)
    text_score = font1.render(str(score)+" полицаев вкинулось",1,(255,255,255))
    wind.blit(text_score,(10,50))
    kp = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            game2 = False
                
        if kp[K_SPACE]:
            sprite1.fire()
    if trash2 != False:
        if score >= 500 :
            back = transform.scale(image.load("vostan1.jpg"), (1000,700))
            trash1 = False
            for i in range (100):
                monster = GameSprite("polise.png", randint(40,960), -20,100,100, randint(2,2))
                monsters.add(monster)
            game2 = False
            game3 = True
    if numb >= 100:
        back = transform.scale(image.load("sneg.jpg"), (1000,700))
    if numb >= 200:
        back = transform.scale(image.load("failniga.jpg"), (1000,700))
        text_def = font1.render("ВЫ ПРОИГРАЛИ",50,(255,255,255))
        wind.blit(text_def,(100,100))
        game2 = False    
    display.update()

while game3:
    wind.blit(back,(0,0))
    sprite1.showhero()
    monsters.draw(wind)
    bulets.draw(wind)
    sprite1.uprawlen()
    monsters.update()
    bulets.update()
    clock.tick(FPS)
    text_lose = font1.render("вас поймали "+str(numb)+" полицаев",1,(255,255,255))
    wind.blit(text_lose,(10,20))
    if sprite.groupcollide(monsters, bulets, True, True):
            score += 1
            monster = GameSprite("polise.png", randint(40,960), -20,100,100, randint(2,2))
            monsters.add(monster)
    text_score = font1.render(str(score)+" полицаев вкинулось",1,(255,255,255))
    wind.blit(text_score,(10,50))
    kp = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            game3 = False        
        if kp[K_SPACE]:
            sprite1.fire()
    if trash3 != False:
        if score >= 750 :
            back = transform.scale(image.load("vostan1.jpg"), (1000,700))
            trash1 = False
            for i in range (125):
                monster = GameSprite("polise.png", randint(40,960), -20,100,100, randint(2,2))
                monsters.add(monster)
            game3 = False
            game4 = True
    if numb >= 100:
        back = transform.scale(image.load("sneg.jpg"), (1000,700))
    if numb >= 200:
        back = transform.scale(image.load("failniga.jpg"), (1000,700))
        text_def = font1.render("ВЫ ПРОИГРАЛИ",50,(255,255,255))
        wind.blit(text_def,(100,100))
        game3 = False
    display.update()

while game4:
    wind.blit(back,(0,0))
    sprite1.showhero()
    monsters.draw(wind)
    bulets.draw(wind)
    sprite1.uprawlen()
    monsters.update()
    bulets.update()
    clock.tick(FPS)
    text_lose = font1.render("вас поймали "+str(numb)+" полицаев",1,(255,255,255))
    wind.blit(text_lose,(10,20))
    if sprite.groupcollide(monsters, bulets, True, True):
            score += 1
            monster = GameSprite("polise.png", randint(40,960), -20,100,100, randint(2,2))
            monsters.add(monster)
    text_score = font1.render(str(score)+" полицаев вкинулось",1,(255,255,255))
    wind.blit(text_score,(10,50))
    kp = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            game4 = False
               
        if kp[K_SPACE]:
            sprite1.fire()
    if trash4 != False:
        if score >= 1000 :
            back = transform.scale(image.load("win.jpg"), (1000,700))
            trash4 = False
            
            text_win = font1.render("ВЫ ПРИНЯТЫ В КОМАНДУ!!!",50,(255,255,255))
            wind.blit(text_win,(100,100))
            game4 = False
    if numb >= 100:
        back = transform.scale(image.load("sneg.jpg"), (1000,700))
    if numb >= 200:
        back = transform.scale(image.load("failniga.jpg"), (1000,700))
        text_def = font1.render("ВЫ ПРОИГРАЛИ",50,(255,255,255))
        wind.blit(text_def,(100,100))
        game4 = False
    display.update()        