# Menu template with button class and basic menu navigation
# Adapted from http://www.dreamincode.net/forums/topic/401541-buttons-and-sliders-in-pygame/

import pygame, sys
pygame.init()
title = " "
#J = "Zombie Parashooter"
background = pygame.image.load("zombie.jpg")
# Define some colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (177, 227, 102)
BRIGHT_GREEN = (205, 237, 157)
RED = (234, 53, 70)
BRIGHT_RED = (241,126,137)
BRIGHT_Blue = (135,212,223)
Blue = (67,188,205)

SCREENWIDTH = 740
SCREENHEIGHT = 521
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)



pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
pygame.mixer.music.load('A Walk in the Forest - Relax Music and Nature Sounds.mp3')
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
def stop_music():
    pygame.mixer.music.pause()

level = 1
title = "Zombie Parashooter"
titlesize = 30

carryOn = True
clock = pygame.time.Clock()

#create button objects
fontTitle = pygame.font.Font('freesansbold.ttf', titlesize)
textSurfaceTitle = fontTitle.render(title, True, BLACK) 
textRectTitle = textSurfaceTitle.get_rect()
textRectTitle.center = (370,50)  



button_HELLO = Button("PLAY", (SCREENWIDTH/2, SCREENHEIGHT/4), my_hello, bg=RED)
button_Previous = Button("PREVIOUS", (SCREENWIDTH/2, SCREENHEIGHT/4), my_previous_function,bg=RED)
button_SETTINGS = Button("SETTINGS", (SCREENWIDTH/2, SCREENHEIGHT*2/4),my_next_function, bg=GREEN)
button_QUIT = Button("QUIT", (SCREENWIDTH/2, SCREENHEIGHT*3/4), my_quit_function, bg=Blue)
button_Sound = Button("SOUND", (SCREENWIDTH/2, SCREENHEIGHT*1/4),my_next_function, bg=GREEN)
button_ON = Button("ON", (SCREENWIDTH/2, SCREENHEIGHT/4), play_music,bg=GREEN)
button_OFF= Button("OFF", (SCREENWIDTH/2, SCREENHEIGHT*2/4),stop_music, bg=GREEN)
button_Previous2 = Button("PREVIOUS", (SCREENWIDTH/2, SCREENHEIGHT*3/4), my_previous_function,bg=RED)
button_Previous3 = Button("PREVIOUS", (100, 481), my_previous_function2,bg=RED)
button_INSTRUCTIONS = Button("INSTRUCTIONS", (SCREENWIDTH/2, SCREENHEIGHT*2/4),my_instunction_function, bg=GREEN)

#arrange button groups depending on level
level1_buttons = [button_HELLO,button_SETTINGS, button_QUIT]
level2_buttons = [button_Previous2,button_Sound]
level3_buttons = [button_ON,button_OFF,button_Previous2]
level4_buttons = [button_Previous3, button_INSTRUCTIONS]
level5_buttons = [button_Previous2]
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

    # --- Draw code goes here
    screen.fill(WHITE)
    screen.blit(background, (0, 0))
    screen.blit(textSurfaceTitle,textRectTitle)

    # Clear the screen to white
    

    # Draw buttons
    if level == 1:
        title = "Zombie Parashooter"
        for button in level1_buttons:
            button.draw()
    elif level == 2:
        title = "Settings"
        for button in level2_buttons:
            button.draw()
    elif level == 3:
        title = "Sound"
        for button in level3_buttons:
            button.draw()
    elif level == 4:
        for button in level4_buttons:
            button.draw()
    elif level == 5:
        title = "'A' to move left"
        titlesize = 10
        for button in level5_buttons:
            button.draw()

    # Add title
    
    textSurfaceTitle = fontTitle.render(title, True, BLACK) 
    textRectTitle = textSurfaceTitle.get_rect()
    textRectTitle.center = (370,50)

    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()
