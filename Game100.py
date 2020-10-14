import pygame,sys,numpy
from pygame import *
from random import randint
import time
carImg = pygame.image.load('car.png')
carImgT = pygame.image.load('car.png')
pygame.font.init()
basicfont = pygame.font.SysFont(None, 48)
class Player:
    def init(self,pos,lives):
        self.pos = pos
        self.x = 400
        self.y = 450
        self.lives = lives
    def locate(self):
        if(self.pos == 0):
            self.x = 400 - ((self.y-100)/2)
        elif(self.pos == 2):
            self.x = 400 + ((self.y-100)/2)
        else:
            self.x = 400
    def posm(self):
        if(self.pos >= 1):
            self.pos -= 1
    def posp(self):
        if(self.pos <= 1):
            self.pos += 1
    def draw(self,window):
        window.blit(carImg, (self.x - 50,self.y - 50))
    def collide(self,pos):
        if(self.pos == pos):
            self.lives -= 1
            if(self.lives == 0):
                pygame.quit()
            return True
    def getLives(self):
        return self.lives
class Enemy:
    def init(self,pos):
        self.y = 100 
        self.pos = pos
        self.x = 400
    def reset(self):
        self.y = 100
        self.pos = randint(0,2)
    def move(self):
        self.y += (self.y/100)**3
        if(self.pos == 0):
            self.x = 400 - ((self.y-85)/2)- 50*(numpy.log(self.y -99)/6)
        elif(self.pos == 2):
            self.x = 400 + ((self.y-85)/2)- 50*(numpy.log(self.y -99)/6)
        else:
            self.x = 400 - 50*(200/(600-self.y))
    def draw(self,window):
        carImgT = pygame.transform.rotozoom(carImg,0,numpy.log(self.y -99)/6)
        window.blit(carImgT,(self.x - int(numpy.log(self.y -99)/6) , self.y - int(numpy.log(self.y -99)/6)))
    def getPos(self):
        return self.pos
    def getY(self):
        return self.y
player = Player()
player.init(1,3)
car1 = Enemy()
car1.init(0)
car2 = Enemy()
car2.init(2)
pygame.init()
screen = pygame.display.set_mode((800,600),pygame.NOFRAME)
while True:
    screen.fill((1,1,200))
    pygame.draw.rect(screen, (0,175,0),(0,100,800,500))
    pygame.draw.polygon(screen,(150,150,150),[(100,600),(700,600),(405,100),(395,100)])
    y1 = car1.getY()
    y2 = car2.getY()
    if(y1 > 500):
        car1.reset()
    if(y2 > 500):
        car2.reset()
    car1.move()
    car2.move()
    car1.draw(screen)
    car2.draw(screen)
    for event in pygame.event.get():
            if event.type==KEYDOWN:
                if event.key==K_LEFT:
                    player.posm()
                if event.key==K_RIGHT:
                    player.posp()
    player.locate()
    player.draw(screen)
    if(y1 > 400 and y1 < 500):
        if(player.collide(car1.getPos()) == True):
            car1.reset()
    if(y2 > 400 and y2 < 500):
        if(player.collide(car2.getPos()) == True):
            car2.reset()
    screen.blit(basicfont.render('Lives: ' + str(player.getLives()), False, (255, 255, 255)),(0,0))
    pygame.display.update()
    time.sleep(1/60)


