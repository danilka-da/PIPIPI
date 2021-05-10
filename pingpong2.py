from pygame import *
from random import randint
from time import time as timer
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,w,h,player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(w,h))
        self.speed = player_speed
        self.rect=self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_LEFT] and self.rect.x>5:
            self.rect.x-=self.speed
        if key_pressed[K_RIGHT] and self.rect.x<715:
            self.rect.x+=self.speed
    def fire(self):
        bullet = Bullet("bullet.png",20,15,self.rect.centerx,self.rect.top,10)
        bullets.add(bullet)
        shot.play()
window = display.set_mode((800, 600))
display.set_caption('ксг')
bg = transform.scale(image.load('fff.jpg'),(800, 600))




Finish = False
run=False
clock = time.Clock()





space_ship = Player("rocket.png",80,100,380,495,5)


mixer.init()
mixer.music.load('d.ogg.ogg')
mixer.music.play()
shot = mixer.Sound('d.ogg.ogg')
##font.init()
##lose = font.SysFont('Arial',70).render("ti vsral", 1,(255,0,0))
##win = font.SysFont('Arial',70).render("krasaychik", 1,(0,255,0))


game = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not(finish):
     
        
    display.update()            
    clock.tick(60)

