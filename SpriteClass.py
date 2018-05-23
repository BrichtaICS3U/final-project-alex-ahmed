#Attraction code adapted from: https://stackoverflow.com/questions/20044791/how-to-make-an-enemy-follow-the-player-in-pygame
import pygame
import math
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Enemy(pygame.sprite.Sprite):

    def __init__(self, width2, height2, speed2):

        super().__init__()

        self.image = pygame.image.load("zombie.png").convert()
        self.image.set_colorkey(WHITE)
        self.image = pygame.transform.scale(self.image,(width2, height2))

        self.width2 = width2
        self.height2 = height2
        self.speed = speed2
        #self.attack = attack

        self.rect = self.image.get_rect()

    def moveRight2(self, pixels):
        self.rect.x += pixels

    def moveLeft2(self, pixels):
        self.rect.x -= pixels

    def changeSpeed2(self, speed):
        self.speed = speed

    def moveForward2(self, speed):
        self.rect.y += self.speed * speed / 20

    def changeSpeed(self, speed):
        self.speed = speed

    def moveHorizontal(self, speed) :
        self.rect.x += self.speed * speed / 20

    

class Player(pygame.sprite.Sprite):

    def __init__(self, width, height, speed):

        super().__init__()

        #self.image = pygame.Surface([width, height])
        self.image = pygame.image.load("army.gif").convert()
        #self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        self.image = pygame.transform.scale(self.image,(width, height))
        

        #self.color = color
        self.width = width
        self.height = height
        self.speed = speed
        #self.attack = attack


        #pygame.draw.rect(self.image,[0 , 0, self.width, self.height])

        self.rect = self.image.get_rect()
        

    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def changeSpeed(self, speed):
        self.speed = speed

    def moveForward(self, speed):
        self.rect.y += self.speed * speed / 20

