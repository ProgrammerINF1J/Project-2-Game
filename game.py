import sys, pygame
import time
pygame.init()


#Globals
width = 800
height = 600
size = width, height #defines the height and width of the game window
display = pygame.display.set_mode(size) #defines the screen

#color library
white = 255, 255, 255
black = 0, 0, 0
green = 0, 255, 0
light_green = 107, 255, 129
red = 255, 0, 0
light_red = 255, 112, 131
blue = 0, 0, 255
light_blue = 60, 130, 240

font = pygame.font.Font(None, 30)
logo = pygame.image.load("skyline.png")
rulesImg = pygame.image.load('Knipsel1.png')
rulesImg1 = pygame.image.load('Knipsel2.png')

clock = pygame.time.Clock()
closed = False

def process_events():
    """Checks if there are any active events it returns True or False"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Give the signal to quit
            return True
        
    return False



class Button():
    def __init__(self, x , y, height, width, color):
        self.X = x
        self.Y = y
        self. Height = height
        self.Width = width
        self.Color = color
        self.Pressed = False
    def draw(self, surface):
        pygame.draw.rect(surface, self.Color, (self.X, self.Y, self.Width, self.Height))
    def draw_text(self, text, surface):
        Text = font.render(text,1, black)
        surface.blit(Text, (self.X + self.Width//4, self.Y + self.Height//4 ))
    def mouse_event(self, surface, color):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        #mous[0] is the x coordinate of the mouse and mouse[1] is the y coordinate
        if self.X + self.Width > mouse[0] > self.X and self.Height + self.Y > mouse[1] > self.Y:
            pygame.draw.rect(surface, color, (self.X, self.Y, self.Width, self.Height))
            if click[0] == 1:
                self.Pressed = True
                if click[0] == 0:
                    self.Pressed = False
        
        
     
            
            
        
def rules(x,y):
    display.blit(rulesImg, (x *0,5,y*0,5))

def rules1(x,y):
    display.blit(rulesImg1, (x*0,5,y*0,5))





def game(color, width, height):

    def display_menu():
             display.blit(logo, (width//5 ,height//4))
             start_button.draw(display)
             start_button.draw_text("Start" , display)
             exit_button.draw(display)
             exit_button.draw_text("Exit" , display)
             rules_button.draw(display)
             rules_button.draw_text("Rules", display)

    def menu_event():
        start_button.mouse_event(display, light_green)
        exit_button.mouse_event(display, light_red)
        back_button.mouse_event(display, light_red)
        rules_button.mouse_event(display, blue)


    start_button = Button(150, 450, 50, 100, green)#x, y, H, W
    exit_button = Button(550, 450, 50, 100, red)
    rules_button = Button(270, 450, 50, 100, blue)
    back_button = Button(630, 50, 50,100, red)

    pygame.display.set_caption("Euromast: The Game") #Defines the title of the game
    
    #the game loop
    while not process_events():
        
        
        if not start_button.Pressed: 
            display.fill(color)
            display_menu()
            menu_event()
        else: 
            display.fill(red)
            text_start = font.render("Game has started",1,black)
            display.blit(text_start,(200, 150)) 
        
        if exit_button.Pressed:
            sys.exit()
       
       
        if rules_button.Pressed:
            rules(0,0)
            back_button.draw(display)
            back_button.mouse_event(display, light_red)
            back_button.draw_text("Back", display)
        if  back_button.Pressed:
               display.fill(white)
               display_menu()
               menu_event()
               
          
                
                
        
        pygame.display.update()


game(white, width, height)


