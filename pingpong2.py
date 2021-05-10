from pygame import *
from random import randint
from time import time as timer
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,w,h,player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(w,h))
        self.speed = player_speed
        self.rect=self.image.get_rect()
        self.rect.x=player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))

class Player1(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y>0:
            self.rect.y-=self.speed
        if key_pressed[K_s] and self.rect.y<450:
            self.rect.y+=self.speed
class Player2(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y>0:
            self.rect.y-=self.speed
        if key_pressed[K_DOWN] and self.rect.y<450:
            self.rect.y+=self.speed





ball = 'mayot.png'
racket = 'rocket.png' 
finish = False
run=True
clock = time.Clock()
white = (255,255,255)





racket1 = Player1(racket,40,150,10,250,5)
racket2 = Player2(racket,40,150,1160,250,5)

window = display.set_mode((1200, 600))
display.set_caption('PingPong')
window.fill(white)


##font.init()
##lose = font.SysFont('Arial',70).render("ti vsral", 1,(255,0,0))
##win = font.SysFont('Arial',70).render("krasaychik", 1,(0,255,0))


while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not(finish):
        window.fill(white)
        racket1.update()
        racket2.update()
        racket1.reset()
        racket2.reset()
    display.update()            
    clock.tick(80)

