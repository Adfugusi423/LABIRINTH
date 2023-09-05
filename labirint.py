import time
from  random import randint
from pygame import*
'''Переменные для картинок'''
img_back = 'wallpaperbetter.jpg'
img_hero = 'Skin.png'
img_enemy = 'enemy.png'
img_goal = 'goal.png'
img_bullet = 'bullet.png'
img_rock = 'bullet 2.png'
'''Музыка'''
mixer.init()
#mixer.music.load
#mixer.music.play()
#fire = mixer.Sound('.ogg')
'''Шрифт'''
font.init()
font = font.SysFont('Comic Sans MS',  50)
win = font.render('YOU WIN!!!', True,(255,255,0))
lose = font.render('YOU LOSE!!!', True, (255,255,255))
'''Классы'''
class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x, player_y, width, height, speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys [K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys [K_d] and self.rect.x <  win_width - 45: 
            self.rect.x += self.speed
        if keys [K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys [K_s] and self.rect.y < win_height - 45:
            self.rect.y += self.speed
    def fire(self):
        bullet = Bullet(img_bullet, self.rect.right, self.rect.centery,24,25,10)
        bullets.add(bullet)
    def fire2(self):
        bullet = Bullet(img_rock, self.rect.right, self.rect.centery, 24,25,10)
        bullets.add(bullet)

class Enemy(GameSprite):
    side = 'left'
    def update(self):
        if self.rect.x <= 470:
            self.side = 'right'
        if self.rect.x >= win_width - 85:
            self.side = 'left'
        if self.side == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Enemy2(GameSprite):
    side = 'left'
    def update(self):
        if self.rect.x <= 100:
            self.side = 'right'
        if self.rect.x >= win_width - 250:
            self.side = 'left'
        if self.side == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed


class Wall(sprite.Sprite):
    def __init__(self,red, green,blue,wall_x,wall_y, width, height):
        super().__init__()
        self.red = red
        self.green = green
        self.blue = blue
        self.w = width
        self.h = height
        self.image = Surface((self.w, self.h))
        self.image.fill((red,green,blue))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

class Bullet(GameSprite):
    def update(self):
        self.rect.x += self.speed
        if self.rect.x > win_width + 10:
            self.kill()
win_width = 700
win_height = 500
display.set_caption('лабиринт')
window = display.set_mode((win_width, win_height))
back = transform.scale(image.load(img_back),(win_width, win_height))
hero = Player(img_hero, 5, win_height - 80, 40, 40,10)
monster = Enemy(img_enemy, win_width - 80,280,65,65,2)
final = GameSprite(img_goal, win_width - 120, win_height - 80,65,65,0)
monster2 = Enemy2(img_enemy, win_width - 600,60,65,65,2)

w1 = Wall(154,205,50,100,20,450,10)
w2 = Wall(154,205,50,100,480,350,10)
w3 = Wall(154,205,50,100,20,10,380)
w4 = Wall(154,205,50,200,130,10,200)
w8 = Wall(154,205,50,300,130,10,200)
w9 = Wall(154,205,50,200,280,10,200)
w5 = Wall(154,205,50,450,130,10,360)
w6 = Wall(154,205,50,300,20,10,30)
w7 = Wall(154,205,50,390,120,130,10)

monsters = sprite.Group()
walls = sprite.Group()
bullets = sprite.Group()
monsters.add(monster)
monsters.add(monster2)
walls.add(w1)
walls.add(w2)
walls.add(w3)
walls.add(w4)
walls.add(w5)
walls.add(w6)
walls.add(w7)
walls.add(w8)
walls.add(w9)
points = 0
game = True
finish = False
clock = time.Clock()
FPS = 60
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                hero.fire()
            elif e.key == K_TAB:
                hero.fire2()
    if finish != True:
        window.blit(back,(0,0))
        walls.draw(window)
        monsters.update()
        monsters.draw(window)
        hero.reset()
        hero.update()
        final.reset()
        bullets.draw(window)
        bullets.update()
        sprite.groupcollide(bullets,walls, True,False)
        sprite.groupcollide(bullets,monsters, True,False)   


        if sprite.spritecollide (hero,walls,False):
            finish = True
            window.blit(lose,(200,200))
          
        if sprite.spritecollide (hero,monsters,False):
            finish = True
            window.blit(lose,(200,200))

        if sprite.collide_rect(hero,final):
            finish = True
            window.blit(win,(200,200))
        

    display.update()
    clock.tick(FPS)