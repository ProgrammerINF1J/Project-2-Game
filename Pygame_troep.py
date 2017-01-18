import pygame
pygame.init()

#Steven
class Button():
    def __init__(self, x , y, height, width, color ):
        self.X = x
        self.Y = y
        self. Height = height
        self.Width = width
        self.Color = color
    def draw(self, surface):
        pygame.draw.rect(surface, self.Color, (self.X, self.Y, self.Width, self.Height))
    def draw_text(self, text, surface):
        Text = font.render(text,1, black)
        surface.blit(Text, (self.X + self.Width//4, self.Y + self.Height//4 ))

#Scherm
display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Rules')

#Kleurtjes
black = (0,0,0)
white = (255,255,255)
green = 0, 255, 0
font = pygame.font.Font(None, 30)


clock = pygame.time.Clock()
closed = False

#Plaatjes
rulesImg = pygame.image.load('Knipsel1.png')
rulesImg1 = pygame.image.load('Knipsel2.png')

def rules(x,y):
    gameDisplay.blit(rulesImg, (x,y))

def rules1(x,y):
    gameDisplay.blit(rulesImg1, (x,y))


x =  (display_width * 0,5)
y = (display_height * 0,5)


while not closed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            closed = True

    gameDisplay.fill(white)
    rules(x,y)
    

    
        
    pygame.display.update()
    clock.tick(60)


pygame.quit()
quit()