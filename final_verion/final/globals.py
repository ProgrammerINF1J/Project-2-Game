import pygame, time
pygame.init()

# Globals
width = 1024
height = 600
size = width, height #defines the height and width of the game window
display = pygame.display.set_mode(size) #defines the screen

#image library, place all images here
logo = pygame.image.load("pictures/skyline.png")
rulesImg = pygame.image.load('pictures/Knipsel1.png')
rulesImg1 = pygame.image.load('pictures/Knipsel2.png')
dice1Img = pygame.image.load('pictures/Dobbel1.png')
dice2Img = pygame.image.load('pictures/Dobbel2.png')
dice3Img = pygame.image.load('pictures/Dobbel3.png')
dice4Img = pygame.image.load('pictures/Dobbel4.png')
dice5Img = pygame.image.load('pictures/Dobbel5.png')
dice6Img = pygame.image.load('pictures/Dobbel6.png')
background = pygame.image.load('pictures/background.png')
coffeeImg = pygame.image.load("pictures/coffee.png")
effect = pygame.mixer.Sound('sounds/coffee.wav') 
ball = pygame.image.load("pictures/stuiter.png")
houtImg = pygame.image.load("pictures/PlakjeHout.png")

#color library
white = 255, 255, 255 
black = 0, 0, 0
green = 0, 255, 0
light_green = 107, 255, 129
red = 255, 0, 0
light_red = 255, 112, 131
blue = 0, 0, 255
light_blue = 60, 130, 240
orange = 230, 100, 20
light_orange = 230, 120, 60
turquise = 75, 220, 230
yellow = 225, 200, 10
light_yellow = 255, 255, 153
kind_of_brown = 210, 200,110
x_set = 150
y_set = 400

# fonts
font = pygame.font.Font(None, 30)#Grote text, wordt gebruikt voor de buttons
font2 = pygame.font.Font(None, 20)#Kleine text, wordt gebruikt voor het input scherm
font3 = pygame.font.Font(None, 70)
krist = pygame.font.Font("fonts/ITCKRIST.TTF", 30)

clock = pygame.time.Clock()
closed = False