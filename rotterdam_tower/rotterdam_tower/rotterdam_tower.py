from database import *
from globals import *
import sys, random

def process_events():
    """Checks if there are any active events it returns True or False"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            closed = True
            # Give the signal to quit
            return True     
    return False

def get_key():
    """Gets the ASCII value from a key from the keyboard"""
    while True:
        event = pygame.event.poll()
        if event.type == pygame.KEYDOWN:
            return event.key
        else:
            pass

class Player():
    def __init__(self, name, score, x, y):
        self.Name = name
        self.Score = score
        self.X = x
        self.Y = y

class Node():
    def __init__(self, value, tail):
        self.Value = value
        self.Tail = tail
        self.IsEmpty = False
    def __str__(self):
        return str(self.Value) + "\n" + str(self.Tail)
    def fold(self, function, predicate):
        return function(self.Value, self.Tail.fold(function, predicate))
    def length(self):
        return self.fold(lambda x, y: y +1,0)
    def print_pygame(self, x, y, n): 
        """displays the list on the pygame window"""
        if (str(n) == "1"):
            player1 = Player(self.Value, 0, x, y)
            text = font.render("Player " + str(n) + ": " + player1.Name + " Score: " + str(player1.Score),1, black)
        elif (str(n) == "2"):
            player2 = Player(self.Value, 0, x, y)
            text = font.render("Player " + str(n) + ": " + player2.Name + " Score: " + str(player2.Score),1, black)
        elif (str(n) == "3"):
            player3 = Player(self.Value, 0, x, y)
            text = font.render("Player " + str(n) + ": " + player3.Name + " Score: " + str(player3.Score),1, black)
        elif (str(n) == "4"):
            player4 = Player(self.Value, 0, x, y)
            text = font.render("Player " + str(n) + ": " + player4.Name + " Score: " + str(player4.Score),1, black)
        display.blit(text, (x, y))
        return self.Tail.print_pygame(x, y + 30, n+1)
    def select(self, index): 
        for i in range(index): 
            self = self.Tail 
        return self.Value 

class Empty():
    def __init__(self):
        self.IsEmpty = True
    def __str__(self):
        return ""
    def fold(self, function, predicate):
        return predicate
    def print_pygame(self, x, y, n):
        return ""

empty = Empty()

class TextBox():
    """Defines an input screen, ist works the same as the buttons, but this one can ask a question. Use in combination with the ask() function"""
    def __init__(self, message, x, y , width, height, color):
        self.Message = message
        self.X = x
        self.Y = y
        self.Width = width
        self.Height = height
        self.Color = color
        
    def draw(self, surface):
        pygame.draw.rect(surface, self.Color, (self.X, self.Y , self.Width, self.Height))
        pygame.draw.rect(surface, white, ((self.X + self.Width//80, self.Y + self.Height//4,self.Width -20, self.Height// 4)))
        if len(self.Message) != 0:
            text = font2.render(self.Message, 1, black) 
            surface.blit(text,((self.X+self.Width//80) , (self.Y+self.Height//4)))
        pygame.display.update()

class Button():
    """"Defines a button each button is build up with a position x and y, a height, a width and a color"""
    def __init__(self, x , y, height, width, color):
        self.X = x
        self.Y = y
        self.Height = height
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
  
def ask_name(screen, question): 
    "ask(screen, question: string) -> answer"
    name = []
    text_box = TextBox(question + str(print_list(name)), width//4, height//4, 600, 100, (red))
    text_box.draw(screen)
    while 1:
        key = get_key()
        if key == pygame.K_BACKSPACE:
            name = name[0:-1] 
        elif key == pygame.K_RETURN:
            break
        elif key <= 127:
            if key == pygame.K_RSHIFT:
                key = ord(key) - 32
            name.append(chr(key))
        text_box = TextBox(question + str(print_list(name)), width//4, height//4, 600, 100, (red))
        text_box.draw(screen) #This function creates an text_box and asks for the users input
    return name
    

def print_list(list):
    """This function does not print the node/empty data structure list but a list in the shape of an array"""
    tmp_list = ""
    for i in range(len(list)):
        tmp_list = tmp_list + list[i]
    return tmp_list

def rules(x,y):
    display.blit(rulesImg, (x *0,5,y*0,5))

def rules1(x,y):
    display.blit(rulesImg1, (x*0,5,y*0,5))

def player_list(amount_players):
    """Returns a list of all players, including names starts with 1 and ends with 4"""
    if amount_players < 5: 
        player = print_list(ask_name(display, "Player " + str(amount_players) + " enter your name: "))
        return Node(player, player_list(amount_players + 1))
    else:
        return empty

    def next_player(list):
        if not list.IsEmpty: 
            return list.Tail 
        else:  
            return 0


def game(color, width, height):
    """Defines the entire game, put the display functions inside the while loop """
    def start():
        return True

    def end():
        return False

    def display_menu():
             """Displays the menu on the screen"""
             display.blit(logo, (width//16 ,0))
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

    def press_all():
        start_button.Pressed = True
        rules_button.Pressed = True
        rules_button2.Pressed = True

    def unpress_all():
        """This function unpresses all buttons visual in the menu, it just sets all button.pressed value to False, exept exit"""
        start_button.Pressed = False
        rules_button.Pressed = False
        rules_button2.Pressed = False
        
    def check_button(): #Contains all buttons from the menu
        """"This function returns True if all menu buttons are pressed and false if not pressed"""
        if start_button.Pressed or rules_button.Pressed or rules_button2.Pressed:
            return True
        else:
            return False

    start_button = Button(width//8, height//2, 50, 100, green)#x, y, H, W
    exit_button = Button(width//2, height//2, 50, 100, red)
    rules_button = Button((5*width)//16, height//2, 50, 100, blue)
    back_button = Button(width -150, 50, 50,100, red)
    rules_button2 = Button(width - 150, 500, 50, 100, blue)
    players = Node("" , empty)
    
    pygame.display.set_caption("Euromast: The Game") #Defines the title of the game
    
    #the game loop
    while not process_events():
        key = pygame.key.get_pressed()
        
        display.fill(color)
        if check_button() == False:#The menu will only apear when nothing is pressed
            display_menu() #When you press a button the menu will disappear
         
        if start_button.Pressed and players.length() < 4:
            players = player_list(1)
          
        if start_button.Pressed:
            back() 
            players.print_pygame(width - 400, 50, 1)
            x = random.randint(0,3)
            turn = font.render(players.select(x) + " its your turn", 1, orange)
            display.blit(turn, (400, 30))
            pygame.time.wait(100)
              
        if back_button.Pressed: #The back button resets all buttons and clears the player lsit
            unpress_all()
            players = Node("", empty)
            pygame.time.wait(100)
            back_button.Pressed = False

        if rules_button.Pressed:
            if rules_button.Pressed: #Shows the rules of the game including a next button
                display.fill(color)
                rules(width - 200,0)
                rules_button2.draw(display)
                rules_button2.mouse_event(display, light_blue)
                rules_button2.draw_text("Next", display)
                if rules_button2.Pressed: #If the next button pressed show more rules and back button
                        display.fill(color)
                        rules1(width-200,0)
                        back()

        if exit_button.Pressed:
            sys.exit()
              
        pygame.display.update()

game(white, width, height)

#Closes the pygame window
pygame.quit()
quit()