import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, width, height, speed, damage):

        super().__init__()

        self.image = pygame.image.load("bullet.png")
        self.image = pygame.transform.scale(self.image,(width, height))

        self.width = width
        self.height = height
        self.speed = speed
        self.damage = damage

        self.rect = self.image.get_rect()

        speed = 20000

    
    def goRight(self, speed):
        self.rect.x += self.speed

    def goLeft(self, speed):
        self.rect.x -= self.speed

    def setSpeed(self, speed):
        self.speed = speed

    def shootBulletUp(self, speed):
        self.rect.y -= self.speed
