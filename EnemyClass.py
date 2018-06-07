#Attraction code adapted from: https://stackoverflow.com/questions/20044791/how-to-make-an-enemy-follow-the-player-in-pygame
from PlayerClass import Player
import pygame
import math
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Enemy(pygame.sprite.Sprite):

    def __init__(self, width, height, speed):

        super().__init__()

        self.image = pygame.image.load("zombiee.png").convert()
        self.image.set_colorkey(BLACK)
        self.image = pygame.transform.scale(self.image,(width, height))

        self.width = width
        self.height = height
        self.speed = speed
        #self.attack = attack

        self.life = 10

        

        self.rect = self.image.get_rect()

    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def changeSpeed(self, speed):
        self.speed = speed

    def moveForward(self, speed):
        self.rect.y += self.speed * speed / 20

    def changeSpeed(self, speed):
        self.speed = speed

    def moveHorizontal(self, speed) :
        self.rect.x += self.speed * speed / 20

    def move_towards_player(self, player):
        # find normalized direction vector (dx, dy) between enemy and player
        dx, dy =  player.rect.x - self.rect.x, player.rect.y - self.rect.y
        dist = math.hypot(dx, dy)
        dx, dy = dx / dist, dy / dist
        # move along this normalized vector towards the player at current speed
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed
