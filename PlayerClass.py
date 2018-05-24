import pygame
WHITE = (255, 255, 255)

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

        self.life = 10

    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def changeSpeed(self, speed):
        self.speed = speed

    def moveForward(self, speed):
        self.rect.y += self.speed * speed / 20


        
