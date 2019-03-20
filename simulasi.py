import pygame
import math
import numpy as np
import theta

pygame.init()

win = pygame.display.set_mode((1200, 480))

pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('Body5.png'), pygame.image.load('Body6.png'), pygame.image.load('Body7.png'),
             pygame.image.load('Body5.png'), pygame.image.load('Body6.png'), pygame.image.load('Body7.png'),
             pygame.image.load('Body5.png'), pygame.image.load('Body6.png'), pygame.image.load('Body7.png')]

walkLeft = [pygame.image.load('Body5.png'), pygame.image.load('Body6.png'), pygame.image.load('Body7.png'),
            pygame.image.load('Body5.png'), pygame.image.load('Body6.png'), pygame.image.load('Body7.png'),
            pygame.image.load('Body5.png'), pygame.image.load('Body6.png'), pygame.image.load('Body7.png')]

kelapa = pygame.image.load('_tree_03_70000.png')
bg = pygame.image.load('bg2.jpg')
char = pygame.image.load('Body5.png')
bola = pygame.image.load('bola1.png')

clock = pygame.time.Clock()

#var :
y0 = 0
t1 = 0.1
t2 = 0.2
g = 9.8
yt = 0
yt2 = 0
ytn = 0
vt = 0
t = 0
x = 0
peluru = 0
waktu = 0

bolax = 1110
bolay = 155

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.left:
            win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(char, (self.x, self.y))

class bolaaa(object):
    gerakan = [pygame.image.load('bola1.png'), pygame.image.load('bola1.png'), pygame.image.load('bola1.png'),
               pygame.image.load('bola1.png'), pygame.image.load('bola1.png'), pygame.image.load('bola1.png'),
               pygame.image.load('bola1.png'), pygame.image.load('bola1.png'), pygame.image.load('bola1.png'),
               pygame.image.load('bola1.png'), pygame.image.load('bola1.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [y, end]
        self.walkCount = 0
        self.vel = 2

    def draw(self, win):
        self.move()
        if self.walkCount + 1 >= 33:
            self.walkCount = 0

        if self.vel > 0:
            win.blit(self.gerakan[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.gerakan[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1

    def move(self):
        if man.x >= 1100:
            if self.vel > 0:
                if self.y < self.path[1] + self.vel:
                    self.y += self.vel
                else:
                    self.vel = self.vel * -1
                    self.y += self.vel
                    self.walkCount = 0



class enemy(object):
    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'),
                 pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'),
                 pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'),
                 pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'),
                pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'),
                pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'),
                pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 2

    def draw(self, win):
        self.move()
        if self.walkCount + 1 >= 33:
            self.walkCount = 0

        if self.vel > 0:
            win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1

    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0


def redrawGameWindow():
    win.blit(bg, (0, 0))
    win.blit(kelapa, (1000, 68))
    #win.blit(bola, (bolax, bolay))

    text = font.render('Yo: ' + str(y0), 1, (0, 0, 0))
    textg = font.render('g: ' + str(-g), 1, (0, 0, 0))
    textt1 = font.render('t1 : ' + str(t1), 1, (0, 0, 0))
    textt2 = font.render('waktu - numerik : ' + str(waktu), 1, (0, 0, 0))
    textt2n = font.render('waktu - analitik : ' + str(t), 1, (0, 0, 0))
    #textt = font.render('kecepatan pada detik : ' + str(vt), 1, (0, 0, 0))
    textyt1 = font.render('ketinggian objek(analitik) pada detik '+str(t1) + ': ' + str(yt), 1, (0, 0, 0))
    textyt2 = font.render('ketinggian objek(numerik) pada detik ' + str(t1) + ' : ' + str(ytn), 1, (0, 0, 0))



    win.blit(text, (700, 10))
    win.blit(textg, (700, 30))
    win.blit(textt1, (700, 50))
    win.blit(textt2, (770, 50))
    win.blit(textyt1, (700, 110))
    win.blit(textyt2, (700, 130))
    #win.blit(textt, (700, 70))
    win.blit(textt2n, (700, 90))


    man.draw(win)
    musuh.draw(win)
    bolaa.draw(win)
    pygame.display.update()


# mainloop
man = player(20, 290, 64, 64)
font = pygame.font.SysFont('comicsans', 20)
musuh = enemy(580, 410, 64, 64, 730)
bolaa = bolaaa(1110, 155, 20, 20, 320)
run = True
while run:
    clock.tick(15)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
    elif keys[pygame.K_RIGHT] and man.x < 1200 - man.width - man.vel:

        man.x += man.vel
        man.right = True
        man.left = False


    else:
        man.right = False
        man.left = False
        man.walkCount = 0

    if not (man.isJump):
        if man.x >= 580 and man.x <= 700:
            man.y = 410
        else:
            man.y = 290
        if keys[pygame.K_SPACE]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0

    else:


        #if man.y < 60:
            #y0 = man.y
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.6 * neg
            man.jumpCount -= 1

        else:

            man.isJump = False
            man.jumpCount = 10

    if man.x >= 1100:
        y0=155
        yt = (0.5 * -g * t1 * t1) + y0
        yt2 = (0.5 * -g * t2 * t2) + yt
        t = math.sqrt(y0 * 2 / 9.8)
#    peluru = 0.5 * -g * t1 * t1 + ((man.vel * np.sin(x)) * t1)

        v0 = 0
        vt = 0
        deltaT = 0.1

        if bolaa.y <= 318:
            ytn = 155
            vt = vt + (-g * deltaT)
            ytn = ytn + (vt * deltaT)
            waktu += deltaT
    redrawGameWindow()

pygame.quit()