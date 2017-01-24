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
orange = 230, 100, 20
light_orange = 230, 120, 60

font = pygame.font.Font(None, 30)#Grote text, wordt gebruikt voor de buttons
font2 = pygame.font.Font(None, 20)#Kleine text, wordt gebruikt voor het input scherm

logo = pygame.image.load("skyline.png")
rulesImg = pygame.image.load('Knipsel1.png')
rulesImg1 = pygame.image.load('Knipsel2.png')

clock = pygame.time.Clock()
closed = False

def process_events():
    """Checks if there are any active events it returns True or False"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            closed = True
            # Give the signal to quit
            return True
        
    return False


class Button():
    """"Defines a button each button is build up with a position x and y, a height, a width and a color"""
    def __init__(self, x , y, height, width, color):
        self.X = x
        self.Y = y
        self. Height = height
        self.Width = width
        self.Color = color
        self.Pressed = None
    def draw(self, surface):
        """Draws the button on the screen"""
        pygame.draw.rect(surface, self.Color, (self.X, self.Y, self.Width, self.Height))
    def draw_text(self, text, surface):
        """"Draws text on the button make sure that draw text is AFTER draw"""
        Text = font.render(text,1, black)
        surface.blit(Text, (self.X + self.Width//4, self.Y + self.Height//4 ))
    def mouse_event(self, surface, color):
        """checks of the mouse is at the same position as the button and of it is pressed, put this between draw and draw_text"""
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        #mous[0] is the x coordinate of the mouse and mouse[1] is the y coordinate
        if self.X + self.Width > mouse[0] > self.X and self.Height + self.Y > mouse[1] > self.Y:
            pygame.draw.rect(surface, color, (self.X, self.Y, self.Width, self.Height))
            if click[0] == 1:
                self.Pressed = True
            

def rules(x,y):
    display.blit(rulesImg, (x *0,5,y*0,5))

def rules1(x,y):
    display.blit(rulesImg1, (x*0,5,y*0,5))


def game(color, width, height):
    """Defines the entire game, put the display functions inside the while loop """
    def display_menu():
             """Displays the menu on the screen"""
             display.blit(logo, (0 ,0))
             start_button.draw(display)
             start_button.mouse_event(display, light_green)
             start_button.draw_text("Start" , display)

             exit_button.draw(display)
             exit_button.mouse_event(display, light_red)
             exit_button.draw_text("Exit" , display)

             rules_button.draw(display)
             rules_button.mouse_event(display, light_blue)
             rules_button.draw_text("Rules", display)

    def back():
        """Defines a back button"""
        back_button.draw(display)
        back_button.mouse_event(display,light_red)
        back_button.draw_text("Back", display)

    def unpress_all():
        """This function unpresses all buttons visual in the menu, it just sets all button.pressed value to False, exept exit"""
        start_button.Pressed = False
        rules_button.Pressed = False
        rules_button2.Pressed = False

    def check_button():
        """"This function returns True if all menu buttons are pressed and false if not pressed"""
        if start_button.Pressed or rules_button.Pressed or rules_button2.Pressed:
            return True
        else:
            return False

    start_button = Button(150, height//2, 50, 100, green)#x, y, H, W
    exit_button = Button(550, height//2, 50, 100, red)
    rules_button = Button(270, height//2, 50, 100, blue)
    back_button = Button(630, 50, 50,100, red)
    rules_button2 = Button(630, 500, 50, 100, blue)
    

    pygame.display.set_caption("Euromast: The Game") #Defines the title of the game
    
    #the game loop
    while not process_events():

        if check_button() == False: #Only displays the menu if no button is pressed
            display.fill(color)
            display_menu()
            
        if start_button.Pressed: #Put a game function in here
            display.fill(green)
            text_start = font.render("Game has started",1,black)
            back()
            display.blit(text_start,(200, 150)) 
            
           
        if back_button.Pressed: #If the back button is pressed it resets all button.Pressed values to False, wich makes the unpressed
            unpress_all()
            pygame.time.wait(100)
            back_button.Pressed = False

        if rules_button.Pressed: #Shows the rules of the game including a next button
            display.fill(color)
            rules(0,0)
            rules_button2.draw(display)
            rules_button2.mouse_event(display, light_blue)
            rules_button2.draw_text("Next", display)
    
            if rules_button2.Pressed: #If the next button pressed show more rules and back button
                display.fill(color)
                rules1(0,0)
                back()
                
        if exit_button.Pressed: #Closes the program including the pygame window
            sys.exit()
        
        pygame.display.update()


game(white, width, height)

#Closes the pygame window
pygame.quit()
quit()
