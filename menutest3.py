# Menu template with button class and basic menu navigation
# Adapted from http://www.dreamincode.net/forums/topic/401541-buttons-and-sliders-in-pygame/

import pygame, sys, random
pygame.init()
from PlayerClass import Player
from EnemyClass import Enemy
from BulletClass import Bullet

bulletGain = 1
speedBullets = 10

title = " "
title2 = " "
title3 = " "
title4 = " "
title5 = " "
title6 = " "
title7 = " "
#speed = 1
#J = "Zombie Parashooter"
#speed = 4
speed = 20000
damage = 5
background = pygame.image.load("bg.jpg")
# Define some colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (177, 227, 102)
BRIGHT_GREEN = (205, 237, 157)
RED = (234, 53, 70)
BRIGHT_RED = (241,126,137)
BOLD_RED = (226,0,0)
BRIGHT_Blue = (135,212,223)
Blue = (67,188,205)

PURE_GREEN = (0, 255, 0)
PURE_BLUE = (0, 0, 255)
LIGHT_BLUE = (0, 232, 224)

SCREENWIDTH = 800
SCREENHEIGHT = 600
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)

pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
pygame.mixer.music.load('Call of Duty - Black Ops - Nazi Zombie - Damned.mp3')
pygame.mixer.music.play(-1)


class Button():
    """This is a class for a generic button.
    
       txt = text on the button
       location = (x,y) coordinates of the button's centre
       action = name of function to run when button is pressed
       bg = background colour (default is white)
       fg = text colour (default is black)
       size = (width, height) of button
       font_name = name of font
       font_size = size of font
    """
    def __init__(self, txt, location, action, bg=WHITE, fg=BLACK, size=(100, 40), font_name="Segoe Print", font_size=16):
        self.color = bg  # the static (normal) color
        self.bg = bg  # actual background color, can change on mouseover
        self.fg = fg  # text color
        self.size = size

        self.font = pygame.font.SysFont(font_name, font_size)
        self.txt = txt
        self.txt_surf = self.font.render(self.txt, 1, self.fg)
        self.txt_rect = self.txt_surf.get_rect(center=[s//2 for s in self.size])

        self.surface = pygame.surface.Surface(size)
        self.rect = self.surface.get_rect(center=location)

        self.call_back_ = action

    def draw(self):
        self.mouseover()

        self.surface.fill(self.bg)
        self.surface.blit(self.txt_surf, self.txt_rect)
        screen.blit(self.surface, self.rect)

    def mouseover(self):
        """Checks if mouse is over button using rect collision"""
        self.bg = self.color
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.bg = BRIGHT_RED  # mouseover color

    def call_back(self):
        """Runs a function when clicked"""
        self.call_back_()
        
def my_hello():

    
    print('')

    global level
    level = 4

def my_shell_function():
    """A generic function that prints something in the shell"""
    print('Fire the nukes!')

def my_next_function():
    """A function that advances to the next level"""
    global level
    level += 1
    
def my_previous_function():
    """A function that retreats to the previous level"""
    bg = RED
    global level
    level -= 1

def my_previous_function2():
    """A function that retreats to the previous level"""
    bg = RED
    global level
    level = 1

def my_quit_function():
    """A function that will quit the game and close the pygame window"""
    pygame.quit()
    sys.exit()

def my_instunction_function():
    """A function that will instruct the player on how to play the game"""
    global level
    bg = GREEN
    level = 5 
    

def mousebuttondown(level):
    """A function that checks which button was pressed"""
    pos = pygame.mouse.get_pos()
    if level == 1:
        for button in level1_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()
    elif level == 2:
        for button in level2_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()
    elif level == 3:
        for button in level3_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()
    elif level == 4:
        for button in level4_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()
    elif level == 5:
        for button in level5_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()

                
def play_music():
    pygame.mixer.music.unpause()
    background = pygame.image.load("bg.jpg")
def stop_music():
    pygame.mixer.music.pause()

level = 1
title = "Zombie Parashooter"
title2 = "'D' to move right"
titlesize = 30
titlex = 400

carryOn = True
clock = pygame.time.Clock()

#create button objects

fontTitle = pygame.font.Font('freesansbold.ttf', titlesize)
textSurfaceTitle = fontTitle.render(title, True, BLACK) 
textRectTitle = textSurfaceTitle.get_rect()
textRectTitle.center = (400,50)  

fontTitle2 = pygame.font.Font('freesansbold.ttf', titlesize)
textSurfaceTitle2 = fontTitle2.render(title2, True, BLACK) 
textRectTitle2 = textSurfaceTitle2.get_rect()
textRectTitle2.center = (400,80)


button_HELLO = Button("PLAY", (SCREENWIDTH/2, SCREENHEIGHT/4), my_hello, bg=RED)
button_Previous = Button("PREVIOUS", (SCREENWIDTH/2, SCREENHEIGHT/4), my_previous_function,bg=RED)
button_SETTINGS = Button("SETTINGS", (SCREENWIDTH/2, SCREENHEIGHT*2/4),my_next_function, bg=GREEN)
button_QUIT = Button("QUIT", (SCREENWIDTH/2, SCREENHEIGHT*3/4), my_quit_function, bg=Blue)
button_Sound = Button("SOUND", (SCREENWIDTH/2, SCREENHEIGHT*1/4),my_next_function, bg=GREEN)
button_ON = Button("ON", (SCREENWIDTH/2, SCREENHEIGHT/4), play_music,bg=GREEN)
button_OFF= Button("OFF", (SCREENWIDTH/2, SCREENHEIGHT*2/4),stop_music, bg=GREEN)
button_Previous2 = Button("PREVIOUS", (SCREENWIDTH/2, SCREENHEIGHT*3/4), my_previous_function,bg=RED)
button_Previous3 = Button("PREVIOUS",(SCREENWIDTH*0.5/4, SCREENHEIGHT*3.7/4) , my_previous_function2,bg=RED)
button_Previous4 = Button("PREVIOUS",(SCREENWIDTH*0.5/4, SCREENHEIGHT*3.7/4) , my_previous_function2,bg=RED)

button_CONTINUE = Button("CONTINUE", (SCREENWIDTH*3.5/4, SCREENHEIGHT*3.7/4),my_next_function, bg=GREEN)

#arrange button groups depending on level
level1_buttons = [button_HELLO,button_SETTINGS, button_QUIT]
level2_buttons = [button_Previous2,button_Sound,]
level3_buttons = [button_ON,button_OFF,button_Previous2]
level4_buttons = [button_Previous3, button_CONTINUE]
level5_buttons = [button_Previous4]

#create groups for sprites
all_sprites_list = pygame.sprite.Group()
all_enemies_list = pygame.sprite.Group()

#create player
playerMain = Player(80, 80, 20, 1)
playerMain.rect.x = SCREENWIDTH/2
playerMain.rect.y = SCREENHEIGHT - 120

all_sprites_list.add(playerMain)


#create bullets
for j in range (8):
    bullets = Bullet(10, 10, speedBullets, 5)
    all_sprites_list.add(bullets)
    bullets.rect.x = playerMain.rect.x + 20
    bullets.rect.y = playerMain.rect.y + 20



#create zombies
for i in range(7): # make 5 zombies for now
   zombie = Enemy(80, 80, 4) #make enemies the same size as the player
   zombie.rect.x = random.randint(0, SCREENWIDTH-80)
   zombie.rect.y = random.randint(-400, -200)
   all_sprites_list.add(zombie)
   all_enemies_list.add(zombie)

   
#---------Main Program Loop----------
screen.blit(background, (0, 0))
while carryOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False
        elif event.type == pygame.MOUSEBUTTONDOWN: # Player clicked the mouse
            mousebuttondown(level)


    # --- Game logic goes here
    if playerMain.rect.x > 720:
        playerMain.rect.x = 720
    elif playerMain.rect.x < 0:
        playerMain.rect.x = 0

    if bullets.rect.x > 820:
        damage == 0
        bullets.rect.x = playerMain.rect.x + 20
        bullets.rect.y = playerMain.rect.y + 20
    elif bullets.rect.y > 620:
        j -= 1
        damage == 0
        bullets.rect.x = playerMain.rect.x + 20
        bullets.rect.y = playerMain.rect.y + 20

    
    # --- Draw code goes here
    screen.fill(WHITE)
    screen.blit(background, (0, 0))
    

    # Clear the screen to white
    

    # Draw buttons
    if level == 1:
        colour = BLACK
        title = "Zombie Parashooter"
        for button in level1_buttons:
            button.draw()
    elif level == 2:
        colour = BLACK
        title = "Settings"
        for button in level2_buttons:
            button.draw()
    elif level == 3:
        colour = BLACK
        title = "Sound"

        for button in level3_buttons:
            button.draw()
    elif level == 4:
        colour = BLACK
        title = "Game Instructions"
        title2 = "'D' to move right"
        title3 = "'A' to move left"
        title4 = "Use Mouse to aim"
        title5 = "Click Left Mouse Button to Shoot"
        title6 = "Objective: Eliminate all Zombies. Good Luck."
        for button in level4_buttons:
            button.draw()
    elif level == 5:
        title7 = "Bullets Remaining: " + str(j) +  " " + str(bulletGain)
        title = " "
        keys = pygame.key.get_pressed()
       

        if keys[pygame.K_LEFT]:
            playerMain.moveLeft(10)
            bullets.goLeft(10)
        if keys[pygame.K_RIGHT]:
            playerMain.moveRight(10)
            bullets.goRight(20)
        if keys[pygame.K_UP]:
            bullets.shootBulletUp(speed)
        for button in level5_buttons:
            button.draw()

        for zombie in all_enemies_list:
            #zombie.moveForward(speed)
            #if zombie.rect.y  == SCREENHEIGHT - 120:
            zombie.move_towards_player(playerMain)

        #very simple hit mechanic
        #zombieHitByPlayer = pygame.sprite.spritecollide(bullets, all_enemies_list, False)
        playerHitByZombie = pygame.sprite.spritecollide(playerMain, all_enemies_list, False)
        for hitZombie in playerHitByZombie:
            playerMain.life -= 1
            print(playerMain.life)

        #for hitPlayer in zombieHitByPlayer:
            #zombie.life -= 5
            #print(zombie.life)

            #recycle zombies that have hit the player
            hitZombie.rect.x = random.randint(0, SCREENWIDTH-80)
            hitZombie.rect.y = random.randint(-400, -200)

        if playerMain.life < 1: #player is dead
            print('you died')
            carryOn = False

        zombieHitByPlayer = pygame.sprite.spritecollide(bullets, all_enemies_list, False)
        for hitPlayer in zombieHitByPlayer:
            zombie.life -= 5
            bulletGain = random.randint (1, 5)
            if  bulletGain == 5:   
                j += 1
            else:
                j -= 1
            print(zombie.life)

            #recycle zombies that have hit the player
            hitPlayer.rect.x = random.randint(0, SCREENWIDTH-80)
            hitPlayer.rect.y = random.randint(-400, -200)
            bullets.rect.x = playerMain.rect.x + 20
            bullets.rect.y = playerMain.rect.y + 20
        

        if zombie.life < 1: #player is dead
            print('one zombie dead')
            zombie.rect.x = random.randint(0, SCREENWIDTH-80)
            zombie.rect.y = random.randint(-400, -200)
            zombie.life == 10
            
        
            
        all_sprites_list.update()
        all_sprites_list.draw(screen)
    

    # Add title

    fontTitle = pygame.font.Font('freesansbold.ttf', titlesize)
    textSurfaceTitle = fontTitle.render(title, True, BLACK) 
    
    textSurfaceTitle = fontTitle.render(title, True, colour) 
    textRectTitle = textSurfaceTitle.get_rect()
    textRectTitle.center = (400,50)

    screen.blit(textSurfaceTitle,textRectTitle)
    if level == 4:
        fontTitle2 = pygame.font.Font('freesansbold.ttf', 20)

        textSurfaceTitle2 = fontTitle2.render(title2, True, WHITE) 

        textSurfaceTitle2 = fontTitle2.render(title2, True, LIGHT_BLUE) 
        textRectTitle2 = textSurfaceTitle2.get_rect()
        textRectTitle2.center = (400,150)
        screen.blit(textSurfaceTitle2,textRectTitle2)

        fontTitle3 = pygame.font.Font('freesansbold.ttf', 20)

        textSurfaceTitle3 = fontTitle3.render(title3, True, WHITE) 

        textSurfaceTitle3 = fontTitle3.render(title3, True, LIGHT_BLUE) 

        textRectTitle3 = textSurfaceTitle3.get_rect()
        textRectTitle3.center = (400,210)
        screen.blit(textSurfaceTitle3,textRectTitle3)

        fontTitle4 = pygame.font.Font('freesansbold.ttf', 20)

        textSurfaceTitle4 = fontTitle4.render(title4, True, WHITE) 

        textSurfaceTitle4 = fontTitle4.render(title4, True, Blue) 

        textRectTitle4 = textSurfaceTitle4.get_rect()
        textRectTitle4.center = (400,270)
        screen.blit(textSurfaceTitle4,textRectTitle4)

        fontTitle5 = pygame.font.Font('freesansbold.ttf', 20)

        textSurfaceTitle5 = fontTitle5.render(title5, True, WHITE) 

        textSurfaceTitle5 = fontTitle5.render(title5, True, Blue) 

        textRectTitle5 = textSurfaceTitle5.get_rect()
        textRectTitle5.center = (400,330)
        screen.blit(textSurfaceTitle5,textRectTitle5)

        fontTitle6 = pygame.font.Font('freesansbold.ttf', 20)

        textSurfaceTitle6 = fontTitle6.render(title6, True, WHITE) 
        textRectTitle6 = textSurfaceTitle6.get_rect()
        textRectTitle6.center = (400,390)
        screen.blit(textSurfaceTitle6,textRectTitle6)


        textSurfaceTitle6 = fontTitle6.render(title6, True, Blue) 
        textRectTitle6 = textSurfaceTitle6.get_rect()
        textRectTitle6.center = (400,390)
        screen.blit(textSurfaceTitle6,textRectTitle6)
    
    fontTitle = pygame.font.Font('freesansbold.ttf', titlesize)

    fontTitle7 = pygame.font.Font('freesansbold.ttf', 10)

    textSurfaceTitle7 = fontTitle7.render(title7, True, Blue) 
    textRectTitle7 = textSurfaceTitle7.get_rect()
    textRectTitle7.center = (400,390)
    screen.blit(textSurfaceTitle7,textRectTitle7)

    fontTitle7 = pygame.font.Font('freesansbold.ttf', 10)


    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()

