import pygame as pg

from sys import path
from sys import exit
import os
os.chdir('attachments')

#my_path = os.path.dirname(os.path.realpath('attachments'))
#os.chdir(my_path)
#path.append(my_path)

pg.init()
screen = pg.display.set_mode((800,500)) #set your window size, (x,y)
pg.display.set_caption("Game title/Name")
clock = pg.time.Clock()
surface1 = pg.image.load('ThePit.jpg')
music = pg.mixer.music.load('Mortal.mp3')
pg.mixer.music.play(1)

white = (255,255,255)
green = (0,255,0)
black = (0,0,0)
health1 = pg.Rect(50,470,200,25)
health2 = pg.Rect(450,470,200,25)

calibri = pg.font.SysFont('calibri', 25) #fontType, size

def printToScreen(x,y,text,colour):
    text = str(text)
    label = calibri.render(text, False, colour)
    screen.blit(label,(x,y))

class cage():

    def __init__(self):

        self.frame = 0
        self.speed_x = 0
        self.framek = 0
        self.kicking = 0
        self.framep = 0
        self.punching = 0

        self.hitbox = pg.Rect(250,300,50,50)

        self.run_R = []
        self.run_R.append(pg.image.load('91.png'))
        self.run_R.append(pg.image.load('92.png'))
        self.run_R.append(pg.image.load('93.png'))
        self.run_R.append(pg.image.load('94.png'))
        self.run_R.append(pg.image.load('95.png'))
        self.run_R.append(pg.image.load('96.png'))
        self.run_R.append(pg.image.load('97.png'))
        self.run_R.append(pg.image.load('98.png'))

        self.run_L = []
        for i in self.run_R:
            self.run_L.append(pg.transform.flip(i,1,0))

        self.kick = []
        self.kick.append(pg.image.load('30.png'))
        self.kick.append(pg.image.load('31.png'))
        self.kick.append(pg.image.load('32.png'))
        self.kick.append(pg.image.load('33.png'))
        self.kick.append(pg.image.load('34.png'))
        self.kick.append(pg.image.load('35.png'))
        self.kick.append(pg.image.load('36.png'))
        self.kick.append(pg.image.load('37.png'))

        self.punch = []
        self.punch.append(pg.image.load('20.png'))
        self.punch.append(pg.image.load('21.png'))
        self.punch.append(pg.image.load('22.png'))
        self.punch.append(pg.image.load('23.png'))
        self.punch.append(pg.image.load('24.png'))
        self.punch.append(pg.image.load('25.png'))
        self.punch.append(pg.image.load('26.png'))

        self.stand = pg.image.load('90.png')

        self.dead = []
        self.dead.append(pg.image.load('60.png'))
        self.dead.append(pg.image.load('61.png'))
        self.dead.append(pg.image.load('62.png'))
        self.dead.append(pg.image.load('63.png'))
        self.dead.append(pg.image.load('64.png'))
        self.dead.append(pg.image.load('65.png'))
        self.dead.append(pg.image.load('66.png'))


        xD = len(self.dead)
        for i in range(xD):
            self.dead[i] = (pg.transform.scale2x(self.dead[i]))
        xP = len(self.punch)
        for i in range(xP):
            self.punch[i] = (pg.transform.scale2x(self.punch[i]))
        xK = len(self.kick)
        for i in range(xK):
            self.kick[i] = (pg.transform.scale2x(self.kick[i]))
        xR = len(self.run_R)
        for i in range(xR):
            self.run_R[i] = (pg.transform.scale2x(self.run_R[i]))
        xL = len(self.run_L)
        for i in range(xL):
            self.run_L[i] = (pg.transform.scale2x(self.run_L[i]))
        self.stand = (pg.transform.scale2x(self.stand))

    def draw(self):
        if self.speed_x == 0 and self.kicking == 0 and self.punching == 0:
            screen.blit(self.stand, (self.hitbox[0],self.hitbox[1]))
            self.hitbox[2] = self.stand.get_width()
            self.hitbox[3] = self.stand.get_height()
        if self.speed_x > 0:
            screen.blit(self.run_R[self.frame], (self.hitbox[0],self.hitbox[1]))
        if self.speed_x < 0:
            screen.blit(self.run_L[self.frame], (self.hitbox[0],self.hitbox[1]))
        if self.speed_x == 0 and self.kicking == 1:
            screen.blit(self.kick[self.framek], (self.hitbox[0],self.hitbox[1]))
        if self.speed_x == 0 and self.punching == 1:
            screen.blit(self.punch[self.framep], (self.hitbox[0],self.hitbox[1]))

    def update(self):
        self.hitbox[0] += self.speed_x

        if self.speed_x != 0:
            self.frame += 1

        if self.frame > 7:
            self.frame = 1

        if self.speed_x == 0 and self.kicking == 1:
            self.framek += 1

        if self.framek > 7:
            self.framek = 0
            self.kicking = 0

        if self.speed_x == 0 and self.punching == 1:
            self.framep += 1

        if self.framep > 6:
            self.framep = 0
            self.punching = 0

class frozen():

    def __init__(self):

        self.frame = 0
        self.speed_x = 0
        self.framep = 0
        self.punching = 0
        self.framek = 0
        self.kicking = 0
        self.framed = 0

        self.hitbox = pg.Rect(450,300,50,50)

        self.run_R = []
        self.run_R.append(pg.image.load('41.png'))
        self.run_R.append(pg.image.load('42.png'))
        self.run_R.append(pg.image.load('43.png'))
        self.run_R.append(pg.image.load('44.png'))
        self.run_R.append(pg.image.load('45.png'))
        self.run_R.append(pg.image.load('46.png'))
        self.run_R.append(pg.image.load('47.png'))
        self.run_R.append(pg.image.load('48.png'))

        self.run_L = []
        for i in self.run_R:
            self.run_L.append(pg.transform.flip(i,1,0))

        self.punch = []
        self.punch.append(pg.image.load('80.png'))
        self.punch.append(pg.image.load('81.png'))
        self.punch.append(pg.image.load('82.png'))
        self.punch.append(pg.image.load('83.png'))

        self.punch_L = []
        for i in self.punch:
            self.punch_L.append(pg.transform.flip(i,1,0))

        self.kick = []
        self.kick.append(pg.image.load("50.png"))
        self.kick.append(pg.image.load("51.png"))
        self.kick.append(pg.image.load("52.png"))
        self.kick.append(pg.image.load("53.png"))
        self.kick.append(pg.image.load("54.png"))
        self.kick.append(pg.image.load("55.png"))

        self.kick_L = []
        for i in self.kick:
            self.kick_L.append(pg.transform.flip(i,1,0))

        self.stand1 = pg.image.load('40.png')
        self.stand = (pg.transform.flip(self.stand1,1,0))

        self.dead = []
        self.dead.append(pg.image.load('0.png'))
        self.dead.append(pg.image.load('1.png'))
        self.dead.append(pg.image.load('2.png'))
        self.dead.append(pg.image.load('3.png'))
        self.dead.append(pg.image.load('4.png'))
        self.dead.append(pg.image.load('5.png'))

        self.dead_L = []
        for i in self.dead:
            self.dead_L.append(pg.transform.flip(i,1,0))

        xD = len(self.dead)
        for i in range(xD):
            self.dead_L[i] = (pg.transform.scale(self.dead_L[i], (50, 120)))
        xP = len(self.punch)
        for i in range(xP):
            self.punch_L[i] = (pg.transform.scale(self.punch_L[i], (60, 120)))
        xK = len(self.kick)
        for i in range(xK):
            self.kick_L[i] = (pg.transform.scale(self.kick_L[i], (58, 120)))
        xR = len(self.run_R)
        for i in range(xR):
            self.run_R[i] = (pg.transform.scale(self.run_R[i], (50, 120)))
        xL = len(self.run_L)
        for i in range(xL):
            self.run_L[i] = (pg.transform.scale(self.run_L[i], (50, 120)))
        self.stand = (pg.transform.scale(self.stand, (50, 120)))

    def draw(self):
        if health2[3] > 5:
            if self.speed_x == 0 and self.punching == 0 and self.kicking == 0:
                screen.blit(self.stand,(self.hitbox[0],self.hitbox[1]))
                self.hitbox[2] = self.stand.get_width()
                self.hitbox[3] = self.stand.get_height()
            if self.speed_x > 0:
                screen.blit(self.run_R[self.frame], (self.hitbox[0],self.hitbox[1]))
            if self.speed_x < 0:
                screen.blit(self.run_L[self.frame], (self.hitbox[0],self.hitbox[1]))
            if self.speed_x == 0 and self.punching == 1:
                screen.blit(self.punch_L[self.framep], (self.hitbox[0],self.hitbox[1]))
            if self.speed_x == 0 and self.kicking == 1:
                screen.blit(self.kick_L[self.framek], (self.hitbox[0],self.hitbox[1]))
        if health2[3] <= 5:
                screen.blit(self.dead_L[self.frame], (self.hitbox[0],self.hitbox[1]))

    def update(self):
        self.hitbox[0] += self.speed_x

        if self.speed_x != 0:
            self.frame += 1

        if self.frame > 7:
            self.frame = 1

        if self.speed_x == 0 and self.punching == 1:
            self.framep += 1

        if self.framep > 3:
            self.framep = 0
            self.punching = 0

        if self.speed_x == 0 and self.kicking == 1:
            self.framek += 1

        if self.framek > 5:
            self.framek = 0
            self.kicking = 0

        if self.framed > 5:
            self.framed == 5

John = cage()
Scor = frozen()

while True:
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] == 1:
        John.speed_x = -20
    elif keys[pg.K_RIGHT] == 1:
        John.speed_x = 20
    else:
        John.speed_x = 0
    if keys[pg.K_o] == 1 and John.kicking == 0:
        John.kicking = 1
    if keys[pg.K_p] == 1 and John.punching == 0:
        John.punching = 1
    if keys[pg.K_a] == 1:
        Scor.speed_x = -20
    elif keys[pg.K_d] == 1:
        Scor.speed_x = 20
    else:
        Scor.speed_x = 0
    if keys[pg.K_r] == 1 and Scor.punching == 0:
        Scor.punching = 1
    if keys[pg.K_f] == 1 and Scor.kicking == 0:
        Scor.kicking = 1
    if (John.punching == 1 or John.kicking == 1) and John.hitbox.colliderect(Scor.hitbox) == 1:
        health2[2] += -2
    if (Scor.punching == 1 or Scor.kicking == 1) and Scor.hitbox.colliderect(John.hitbox) == 1:
        health1[2] += -2

    Scor.update()
    John.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    screen.fill(black)
    screen.blit(surface1, (0,0))
    pg.draw.rect(screen, green, health1)
    pg.draw.rect(screen, green, health2)
    printToScreen(450,450,"Scorpion",white)
    printToScreen(50,450,"Johnny Cage",white)
    if health2[2] <= 0:
        break
    if health1[2] <= 0:
        break
    John.draw()
    Scor.draw()
    pg.display.flip()
    clock.tick(10)

if health2[2] <= 0:
    printToScreen(450,200,"Johnny Cage Wins",white)
if health1[2] <= 0:
    printToScreen(450,200,"Scorpion Wins",white)
pg.display.flip()