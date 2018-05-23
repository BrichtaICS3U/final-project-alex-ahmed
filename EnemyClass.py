#Attraction code adapted from: https://stackoverflow.com/questions/20044791/how-to-make-an-enemy-follow-the-player-in-pygame
from PlayerClass import Player
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

    def move_towards_player(self, player, speed):
        # find normalized direction vector (dx, dy) between enemy and player
        dx, dy = self.rect.x - playerMain.rect.x, self.rect.y - playerMain.rect.y
        dist = math.hypot(dx, dy)
        dx, dy = dx / dist, dy / dist
        # move along this normalized vector towards the player at current speed
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed
