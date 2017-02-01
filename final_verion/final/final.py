#--Copyright all rights reserved, this game is created by Steven Koert, Sem Jansen and Vincent de Heer

from database import *
from globals import *
import random, pygame, time
pygame.init()

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

class Node():
    def __init__(self, value, tail):
        """value: unkown type, tail: reference next value or empty"""
        self.Value = value
        self.Tail = tail
        self.IsEmpty = False
    def __str__(self):
        return str(self.Value) + "\n" + str(self.Tail)
    def fold(self, function, predicate): # The predicate can be True, False, 0, 1 , integer , float, string
        """Returns a function uses a lambda as input"""
        return function(self.Value, self.Tail.fold(function, predicate))
    def length(self):
        """Returns the lenght of the list, this function uses fold"""
        return self.fold(lambda x, y: y +1,0)
    def print_pygame(self, x, y, n): 
        """displays the list on the pygame window"""
        if (str(n) == "1"):
            p1 = Player(self.Value, 0, x, y)
            text = font.render(str(n) + ": " + p1.Name,1, black)
        elif (str(n) == "2"):
            p2 = Player(self.Value, 0, x, y)
            text = font.render(str(n) + ": " + p2.Name,1, black)
        elif (str(n) == "3"):
            p3 = Player(self.Value, 0, x, y)
            text = font.render(str(n) + ": " + p3.Name,1, black)
        elif (str(n) == "4"):
            p4 = Player(self.Value, 0, x, y)
            text = font.render(str(n) + ": " + p4.Name,1, black)
        display.blit(text, (x, y))
        return self.Tail.print_pygame(x, y + 30, n+1)
    def select(self, index): 
        """selects an item from a list with the matching index start with 0"""
        for i in range(index):
            self = self.Tail
        return self.Value
    
class Empty():
    """Returns IsEmpty = False, if the list is empty"""
    def __init__(self):
        self.IsEmpty = True
    def __str__(self): #Return an empty string
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
        surface.blit(font2.render("Max. 14 characters----------------------------press return to submit",1,black),(self.X + self.Width//6, self.Y + self.Height//2 +30))
        if len(self.Message) != 0:
            text = font2.render(self.Message, 1, black) 
            surface.blit(text,((self.X+self.Width//80) , (self.Y+self.Height//4)))
        pygame.display.update()

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
                click = pygame.mixer.Sound('sounds/click.wav') 
                click.play()
                self.Pressed = True

#question library: multiple choice
question1 = Node("Is this a question?" ,Node("Yes", Node("No" , Node("Maybe" , Node("Can't tell", Node("Yes", empty))))))
question2 = Node("Who sang the Rotterdam hit you never walk alone?", Node("Frank Sinatra", Node("Lee Towers" , Node("Bruce Lee", Node("Frans Bauer", Node("Lee Towers", empty))))))
question3 = Node("Who is the congressman of Rotterdam?", Node("Barack Obama", Node("Donald Trump", Node("Mark Rutte", Node("Mohammed Abboutaleb", Node("Mohammed Abboutaleb", empty))))))
question4 = Node("How many people live in Rotterdam?" , Node("2000.000", Node("7000.000.000", Node("4", Node("600.000", Node("600.000", empty))))))
question5 = Node("Who won 35th marathon of Rotterdam?", Node("Usain Bolt", Node("Abera Kuma", Node("Jurandy Martina", Node("A random guy", Node("Abera Kuma", empty))))))
question6 = Node("Who does NOT live in Rotterdam?", Node("Martin van Waardenburg", Node("Jandino Asporaat", Node("Thea Beckman", Node("Freek Vonk", Node("Freek Vonk", empty))))))
question7 = Node("Who did NOT develop this game?" ,Node("Steven Koerts", Node("Daniel Brandwijk", Node("Vincent de Heer", Node("Sem Jansen", Node("Daniel Brandwijk", empty))))))
question8 = Node("Which river belongs to Rotterdam?" ,Node("The Rijn", Node("The Maas" , Node("The Thames", Node("The Seine", Node("The Maas", empty))))))
question9 = Node("Where is the museum of Rotterdam?", Node("In Amsterdam", Node("In Schiedam", Node("In Rotterdam", Node("In Groningen", Node("In Rotterdam", empty))))))
question10 = Node("Where is the Rotterdamsedijk?", Node("Rotterdam", Node("Schiedam", Node("Maastricht", Node("Rotterdam and Schiedam" , Node("Rotterdam and Schiedam", empty))))))
question11 = Node("Wich is the tallest buiding in the list?", Node("Euromast", Node("WTC Building", Node("The Markthal", Node("Wijhaven 117", Node("Euromast", empty))))))
question12 = Node("When was Rotterdam bombed?", Node("1941", Node("1940", Node("1943", Node("1942", Node("1940", empty))))))
question13 = Node("When was the dam over the Rotte build?", Node("1170", Node("1270", Node("1370", Node("1470", Node("1270", empty))))))
question14 = Node("Where was Desiderius Erasmus born?", Node("Rotterdam", Node("Trier", Node("Maassluis", Node("Berlin", Node("Rotterdam", empty))))))
question15 = Node("When was Desiderius Erasmus born?", Node("12 july 1536", Node("24 augustus 1455", Node("13 april 1562", Node("4 septembre 1423", Node("12 july 1536", empty))))))
question16 = Node("Is Rotterdam the gateway to Europe?", Node("Yes", Node("No", Node("Probebly", Node("That's a lie!!", Node("Probebly", empty))))))
question17 = Node("How many seats has the Kuip?", Node("132.320", Node("51.480", Node("42.120", Node("45.560", Node("51.480", empty))))))
question18 = Node("What is the answer to THIS question?", Node("This One", Node("this ONE", Node("THIS one", Node("This one", Node("THIS one", empty))))))
question19 = Node("What are geograthical coordinates of Rotterdam?", Node("32 N , 17 E", Node("74 N , 42 E", Node("52 N , 4 E", Node("78 N , 38 E", Node("52 N , 4 E", empty))))))
question20 = Node("What are the colors of the Rotterdam flag?", Node("Yellow and Black", Node("Red, Yellow, Blue", Node("Green and White", Node("Red, White, Blue", Node("Green and White", empty))))))
question21 = Node("What is 454 times 15?", Node("4.930", Node("6.810", Node("5.320", Node("2.234", Node("6.810", empty))))))
question22 = Node("What is the oldest football club of Rotterdam?", Node("Excelcior", Node("Feynoord", Node("Ajax", Node("Sparta", Node("Feynoord", empty))))))
question23 = Node("America has the Trump Towers, what has Rotterdam?", Node("the Eifel Towers", Node("Lee Towers", Node("The Euro Towers", Node("The Towers of Pisa", Node("Lee Towers", empty))))))
question24 = Node("How much degrees is 2pi radians?", Node("180 degrees", Node("360 degrees Celcius", Node("360 degrees", Node("90 degrees", Node("360 degrees", empty))))))
question25 = Node("What is on top of the markthal?", Node("Air", Node("Nothing", Node("Shopping centre", Node("Luxery appartements", Node("Luxery appartements", empty))))))
question26 = Node("What is the name of the Rotterdam boattour company?", Node("Speedo", Node("Spido", Node("Spiedo", Node("Speedy", Node("Spido", empty))))))
question27 = Node("What is 0,5 divided by 0,25?", Node("0,5 * 0,25^-1", Node("4", Node("2^-1 + 4^-1", Node("2,5", Node("0,5 * 0,25^-1", empty))))))
question28 = Node("What are the first 10 digits of pi?", Node("3,141592653", Node("3,141592654", Node("3,14158293", Node("8,919289182", Node("3,141592653", empty))))))
question29 = Node("Is Rotterdam the capital of the Netherlands?", Node("Yes!!!!", Node("No, offcourse not!!!", Node("No, but it should be!!!", Node("Maybe!!!", Node("No, but it should be!!!", empty))))))
question30 = Node("Wich website said: The port of Rotterdam is the largest port of Europe?", Node("wwww.eu.eu", Node("www.holland.be", Node("www.portofrotterdam.com", Node("www.github.com", Node("www.portofrotterdam.com", empty))))))
question31 = Node("Finish the sentence: Komen wij uit Rotterdam..............", Node("Nee hoor!!", Node("Kun je dat horen dan!!!", Node("Ken je dat niet horen dan!!!", Node("Kon je dat niet horen dan!!!", Node("Ken je dat niet horen dan!!!", empty))))))
question32 = Node("Can you answer this question wrong?", Node("No", Node("No", Node("No", Node("No", Node("No", empty))))))
question33 = Node("Can you answer THIS question wrong?", Node("Yes", Node("Yes", Node("Yes", Node("Yes", Node("No", empty))))))
question34 = Node("Can you answer this question right?", Node("Yes", Node("Yes", Node("Yes", Node("Yes", Node("Yes", empty))))))
question35 = Node("Can you answer THIS question right?", Node("No", Node("Offcourse not", Node("Absolutly not", Node("No way", Node("yes", empty))))))
question36 = Node("What is the quadratic formula?", Node("(-b+-(D^0,5)/2a)", Node("sin(x^2)/5", Node("2pi*r^2", Node("a^2 + b^2 = c^2", Node("(-b+-(D^0,5)/2a)", empty))))))
question37 = Node("dh3uh838hdnxmnxmsnmsnmndmsnwdn383#Ed3d#$#%^$(*^$...?", Node("#DRD#r3w2@@w", Node("D#DW@SWSSDSDdw", Node("3$Ddwdsdd3@2dd", Node("ddjskjd9du83ud", Node("3$Ddwdsdd3@2dd", empty))))))
question38 = Node("What is the house number of the Hogeschool Rotterdam?", Node("232", Node("117", Node("234", Node("-32", Node("117", empty))))))
question39 = Node("What is the name of this game?", Node("Rotterdam: The game", Node("GTA 5", Node("CSGO", Node("Euromast: The game", Node("Euromast: The game", empty))))))
question40 = Node("How high is the Euromast?", Node("High", Node("Verry high", Node("Tremendous", Node("Not so high", Node("Tremendous", empty))))))
question41 = Node("How many stepps does the stair of the euromast have?", Node("732", Node("123", Node("589", Node("892", Node("589", empty))))))
question42 = Node("How high is the Euromast for real?", Node("300 meter", Node("0,185 kilometer", Node("930 meter", Node("493 meter", Node("0,185 kilometer", empty))))))
question43 = Node("Who designed the Euromast?", Node("Bert Rijnoever", Node("Frank Scheldewater", Node("Sjaak Trekhaak", Node("Huig Maaskant", Node("Huig Maaskant", empty))))))
question44 = Node("How do you say Rotterdam in slang?", Node("Rotta", Node("Rodda", Node("Roffa", Node("Rovva", Node("Roffa", empty))))))
question45 = Node("What is squarroot of 5", Node("2,23", Node("2,24", Node("2,22", Node("2,25", Node("2,24", empty))))))
question46 = Node("On wich day has the question been written?", Node("19:23 18-1-2017", Node("13:28 1-2-2017", Node("00:00 3-5-1956", Node("12:35 28-1-2017", Node("13:28 1-2-2017", empty))))))
question47 = Node("Would you recommend this game to others?", Node("Yes, offcourse", Node("Yes, It's the best game ever", Node("No, why should I", Node("No, No and no!!", Node("Yes, It's the best game ever", empty))))))
question48 = Node("Wich button is the B button?", Node("A", Node("C", Node("B", Node("D", Node("C", empty))))))
question49 = Node("?", Node("!", Node("@", Node("#", Node("$", Node("#", empty))))))
question50 = Node("What was Wim Alders his job?", Node("Painter", Node("Baker", Node("Comedian", Node("Politician", Node("Politician", empty))))))
# Node("", Node("", Node("", Node("", Node("", Node("", empty)))))) standard question = [Q, A, B, C, D, answer, empty]

#Put al questions in a list, this is where the computer selects the question from
q_list = Node(question1, Node(question2, Node(question3, Node(question4, Node(question5, Node(question6, Node(question7, Node(question8, Node(question9, Node(question10, Node(question11, Node(question12, Node(question13, Node(question14, Node(question15, Node(question16, Node(question17, Node(question18, Node(question19, Node(question20, Node(question21, Node(question22, Node(question23,Node(question24, Node(question25, Node(question26, Node(question27, Node(question28, Node(question29, Node(question30, Node(question31, Node(question32, Node(question33, Node(question34, Node(question35, Node(question36, Node(question37, Node(question38,  Node(question39,  Node(question40,  Node(question41,  Node(question42,  Node(question43,  Node(question44,  Node(question45,  Node(question46,  Node(question47,  Node(question48,  Node(question49,  Node(question50, empty))))))))))))))))))))))))))))))))))))))))))))))))))

#Dice
dice = Node(dice1Img, Node(dice2Img, Node(dice3Img, Node(dice4Img, Node(dice5Img, Node(dice6Img, empty))))))

def roll_dice(x, y):
        index = random.randint(0,5)
        #display.blit(dice.select(index),(x,y))
        return index

class McQuestion():
    def __init__(self, question, option_a, option_b, option_c, option_d, correct):
        """defines a multiple choice question, question, options(a,b,c,d), correct answere"""
        self.Question = question
        self.Option_A = option_a
        self.Option_B = option_b
        self.Option_C = option_c
        self.Option_D = option_d
        self.Answered = False
        self.Correct = correct
    def draw(self, surface):
        """Draws the body of the ask question box"""
        pygame.draw.rect(surface,turquise, (width//10, height//4, 680, 200))
        pygame.draw.rect(surface, yellow ,(width//10, height//4, 680, 50))
        question = font2.render(self.Question, 1, black)
        surface.blit(question, (width//10 + 10, height//4 + 20))
    def answer(self, surface):
        height_btn = 50
        width_btn = 300
        a = Button(120, 220, height_btn, width_btn, orange)
        a.draw(surface)
        a_text = font2.render(self.Option_A, 1, black)
        surface.blit(a_text, (140, 240))
        a.mouse_event(surface, red)

        b = Button(120, 290, height_btn, width_btn, orange)
        b.draw(surface)
        b_text = font2.render(self.Option_B, 1, black)
        surface.blit(b_text, (140, 310))
        b.mouse_event(surface, red)

        c = Button(450, 220, height_btn, width_btn, orange)
        c.draw(surface)
        c_text = font2.render(self.Option_C, 1, black)
        surface.blit(c_text, (470, 240))
        c.mouse_event(surface, red)

        d = Button(450, 290, height_btn, width_btn, orange)
        d.draw(surface)
        d_text = font2.render(self.Option_D, 1, black)
        surface.blit(d_text, (470, 310))
        d.mouse_event(surface, red)

        if a.Pressed:
            if self.Option_A == self.Correct:
                pygame.draw.rect(surface, green, (width//4, height//4, 400, 180))
            else:
                 pygame.draw.rect(surface, red, (width//4, height//4, 400, 180))
            self.Answered = True
            return self.Option_A
        if b.Pressed:
            if self.Option_B == self.Correct:
                pygame.draw.rect(surface, green, (width//4, height//4, 400, 180))
            else:
                 pygame.draw.rect(surface, red, (width//4, height//4, 400, 180))
            self.Answered = True
            return self.Option_B            
        if c.Pressed:
            if self.Option_C == self.Correct:
                pygame.draw.rect(surface, green, (width//4, height//4, 400, 180))
            else:
                 pygame.draw.rect(surface, red, (width//4, height//4, 400, 180))
            self.Answered = True
            return self.Option_C          
        if d.Pressed:
            if self.Option_D == self.Correct:
                pygame.draw.rect(surface, green, (width//4, height//4, 400, 180))
            else:
                 pygame.draw.rect(surface, red, (width//4, height//4, 400, 180))
            self.Answered = True
            return self.Option_D

class Player():
    def __init__(self, name, score, x, y):
        self.Name = name
        self.Score = score
        self.X = x
        self.Y = y
    def draw(self, surface, color):
        pygame.draw.circle(surface, color, (self.X, self.Y), 20)
    def update(self, amount, stepps):
        return Player(self.Name, self.Score + amount, self.X, self.Y - (stepps*10))
    def __str__(self):
        return str(self.Name)
    def reset_score(self):
        return Player(self.Name, 0 , self.X, self.Y)
    def reset_pos(self):
        return Player(self.Name, self.Score, self.X, y_set)
            
class MessageBox():
    def __init__(self, height, width , x, y, color):
        self.Height = height
        self.Width = width
        self.X = x
        self.Y = y
        self.Color = color
    def draw(self, surface, message):
        pygame.draw.rect(surface, self.Color, (self.X, self.Y, self.Width, self.Height))
        surface.blit(font.render(message, 1 , black), (self.X + self.Width//4, self.Y + self.Height//8))

def create_question(index):
    question = q_list.select(index)
    return McQuestion(question.select(0),question.select(1), question.select(2), question.select(3), question.select(4), question.select(5))

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
  if len(name) > 14:
      return name[0:13]
  else:
      return name
    
def print_list(list):
    """This function does not print the node/empty data structure list but a list in the shape of an array"""
    tmp_list = ""
    for i in range(len(list)):
        tmp_list = tmp_list + list[i]
    return tmp_list

def rules(x,y):
    display.blit(rulesImg, (x,y))

def rules1(x,y):
    display.blit(rulesImg1, (x,y))

def player_list(amount_players):
    """Returns a list of all players, including names starts with 1 and ends with 4"""
    if amount_players < 5: 
         player = print_list(ask_name(display, "Player " + str(amount_players) + " enter your name: "))
         return Node(player, player_list(amount_players + 1))
    else:
         return empty        
   
def coffeebreak(x, y):
    display.blit(coffeeImg, (0, 0))
    effect.play()

class Ball():
     def __init__(self, x, y, xspeed, yspeed):
         self.X = x
         self.Y = y   
         self.SpeedX = xspeed
         self.SpeedY = yspeed
     def draw(self, surface):
         #pygame.draw.circle(surface, blue, (self.X, self.Y), self.R)
         display.blit(ball, (self.X, self.Y))
     def move(self):
         if 0 < self.X < 1024:
                self.X = self.X + self.SpeedX 
         if 0 < self.Y < 600:
             self.Y = self.Y +self.SpeedY
         if self.X == 5 or self.X == 810:      
             self.SpeedX = self.SpeedX *-1
         if self.Y == 5 or self.Y == 410:
             self.SpeedY = self.SpeedY *-1 

def game(color, width, height):
    """Defines the entire game, put the display functions inside the while loop """
    def start():
        return True

    def end():
        return False

    def display_menu():
        """Displays the menu on the screen"""
        display.blit(logo, (0 ,0))

        ball.draw(display)
        ball.move()

        start_button.draw(display)
        start_button.mouse_event(display, light_green)
        start_button.draw_text("Start" , display)

        exit_button.draw(display)
        exit_button.mouse_event(display, light_red)
        exit_button.draw_text("Exit" , display)

        rules_button.draw(display)
        rules_button.mouse_event(display, light_blue)
        rules_button.draw_text("Rules", display)

        highscore_button.draw(display)
        highscore_button.mouse_event(display, light_yellow)
        highscore_button.draw_text("Highscore", display)

    def back():
        """Defines a back button"""
        back_button.draw(display)
        back_button.mouse_event(display,light_red)
        back_button.draw_text("Back", display)

    def press_all():
        start_button.Pressed = True
        rules_button.Pressed = True
        rules_button2.Pressed = True
        highscore_button.Pressed = True

    def unpress_all():
        """This function unpresses all buttons visual in the menu, it just sets all button.pressed value to False, exept exit"""
        start_button.Pressed = False
        rules_button.Pressed = False
        rules_button2.Pressed = False
        highscore_button.Pressed = False
        
    def check_button(): #Contains all buttons from the menu
        """"This function returns True if all menu buttons are pressed and false if not pressed"""
        if start_button.Pressed or rules_button.Pressed or rules_button2.Pressed or highscore_button.Pressed:
            return True
        else:
            return False

    #button library
    ball = Ball(50, 50, 5, 5)
    start_button = Button(width//8, height//2, 50, 100, green)#x, y, H, W
    exit_button = Button(width//2, height//2, 50, 100, red)
    rules_button = Button((5*width)//16, height//2, 50, 100, blue)
    back_button = Button(width -150, 50, 50,100, red)
    rules_button2 = Button(width - 150, 515, 50, 100, blue)
    highscore_button = Button(675, height//2, 50, 180, yellow)
    players = Node(empty , empty) #Sets the list players to empty
    select_question = False
    key = pygame.key.get_pressed()
    stepps = random.randint(0,5)
    player_turn = 0
    coffee = False
    win_screen =  MessageBox(400, 800, 100, 50, blue)
    win_back_button = Button(600, 100, 50, 300, red)
    mute = False
    
    highscore = True

    pygame.display.set_caption("Euromast: The Game") #Defines the title of the game
    
    #the game loop
    while not process_events():
          key = pygame.key.get_pressed()
          display.fill(color)
          if player_turn >3:
              player_turn = 0

          if check_button() == False:#The menu will only apear when nothing is pressed
                display_menu() #When you press a button the menu will disappear

          if highscore_button.Pressed:
              display.blit(houtImg, (0,0))
              back()
              if highscore == True:
                  highscore_all = select_screen_highscore()
                  titel = krist.render("Highscore top 5", 1, black)
                  display.blit(titel,(400, 55))
                  score1 = krist.render("Number 1, name: "+highscore_all[0][1]+" score: "+str(highscore_all[0][2]), 1, black)
                  display.blit(score1,(300, 120))
                  score2 = krist.render("Number 2, name: "+highscore_all[1][1]+" score: "+str(highscore_all[1][2]), 1, black)
                  display.blit(score2,(300, 183))
                  score3 = krist.render("Number 3, name: "+highscore_all[2][1]+" score: "+str(highscore_all[2][2]), 1, black)
                  display.blit(score3,(300, 245))
                  score4 = krist.render("Number 4, name: "+highscore_all[3][1]+" score: "+str(highscore_all[3][2]), 1, black)
                  display.blit(score4,(300, 309))
                  score5 = krist.render("Number 5, name: "+highscore_all[4][1]+" score: "+str(highscore_all[4][2]), 1, black)
                  display.blit(score5,(300, 365))

          if win_back_button.Pressed:
            # player 1
            if (check_name(player1.Name) == 0):
                print("doesn't exists")
                insert_player(player1.Name, player1.Score)
                id = select_player_id(player1.Name)
                insert_highscore(id, player1.Name, player1.Score)
                print("score and highscore ge-update van id:", id)
            elif (check_name(player1.Name) == 1):
                print("does exists")
                id = select_player_id(player1.Name)
                if (player1.Score < select_highscore(player1.Name) or player1.Score == select_highscore(player1.Name)):
                    update_score(player1.Score, id)
                    print("p1 score ge-update")
                if (player1.Score > select_highscore(player1.Name)):
                    update_score(player1.Score, id)
                    update_highscore(player1.Score, id)
                    print("p1 highscore ge-update")
            # player 2
            if (check_name(player2.Name) == 0):
                print("doesn't exists")
                insert_player(player2.Name, player2.Score)
                id = select_player_id(player2.Name)
                insert_highscore(id, player2.Name, player2.Score)
                print("score and highscore ge-update van id:", id)
            elif (check_name(player2.Name) == 1):
                print("does exists")
                id = select_player_id(player2.Name)
                if (player2.Score < select_highscore(player2.Name) or player2.Score == select_highscore(player2.Name)):
                    update_score(player2.Score, id)
                    print("p2 score ge-update")
                if (player2.Score > select_highscore(player2.Name)):
                    update_score(player2.Score, id)
                    update_highscore(player2.Score, id)
                    print("p2 highscore ge-update")
            # player 3
            if (check_name(player3.Name) == 0):
                print("doesn't exists")
                insert_player(player3.Name, player3.Score)
                id = select_player_id(player3.Name)
                insert_highscore(id, player3.Name, player3.Score)
                print("score and highscore ge-update van id:", id)
            elif (check_name(player3.Name) == 1):
                print("does exists")
                id = select_player_id(player3.Name)
                if (player3.Score < select_highscore(player3.Name) or player3.Score == select_highscore(player3.Name)):
                    update_score(player3.Score, id)
                    print("p3 score ge-update")
                if (player3.Score > select_highscore(player3.Name)):
                    update_score(player3.Score, id)
                    update_highscore(player3.Score, id)
                    print("p3 highscore ge-update")
            # player 4
            if (check_name(player4.Name) == 0):
                print("doesn't exists")
                insert_player(player4.Name, player4.Score)
                id = select_player_id(player4.Name)
                insert_highscore(id, player4.Name, player4.Score)
                print("score and highscore ge-update van id:", id)
            elif (check_name(player4.Name) == 1):
                print("does exists")
                id = select_player_id(player4.Name)
                if (player4.Score < select_highscore(player4.Name) or player4.Score == select_highscore(player4.Name)):
                    update_score(player4.Score, id)
                    print("p4 score ge-update")
                if (player4.Score > select_highscore(player4.Name)):
                    update_score(player4.Score, id)
                    update_highscore(player4.Score, id)
                    print("p4 highscore ge-update")
            unpress_all() #reset all buttons
            players = Node(empty, empty) #clears the player list
            player_turn = 0 #Set the turn to the first player
            select_question = False # You won't be able to get a question after the winscreen
            win_back_button.Pressed = False #sets itself back to false otherwise you wont be able to click it again
            pygame.mixer.stop() #stops all sound effects
            pygame.mixer.music.stop() #stops all music

          if start_button.Pressed and players.length() < 4: #Game set up
             players = player_list(1) #Creates a list of all players including all names
             player1 = Player(players.select(0), 0, x_set,y_set) #Creates the different claasses for players
             player2 = Player(players.select(1), 0, x_set+180,y_set)#And places the on the start position
             player3 = Player(players.select(2), 0, x_set+360,y_set)
             player4 = Player(players.select(3), 0, x_set+540,y_set)
             startup = pygame.mixer.Sound('sounds/startup.wav') #Plays the opening tune
             startup.play() 
          
          if start_button.Pressed:#If only start button pressed, and the startup is done
              display.blit(background,(0,0)) #Draws the background
              back() 
              display.blit(dice.select(stepps), (870, 130)) #displays the dice
              players.print_pygame(width - 200, height - 200, 1)    #print the players on the screen
              #Put the name and the score under the pawns  
              display.blit(font.render(str(player1.Name) +" "+ str(player1.Score), 1, black), (player1.X -len(player1.Name), player1.Y + 20))
              display.blit(font.render(str(player2.Name) +" "+ str(player2.Score), 1, black), (player2.X -len(player2.Name), player2.Y + 20))
              display.blit(font.render(str(player3.Name) +" "+ str(player3.Score), 1, black), (player3.X -len(player3.Name), player3.Y + 20))
              display.blit(font.render(str(player4.Name) +" "+ str(player4.Score), 1, black), (player4.X- len(player4.Name), player4.Y + 20))
              #Draws the pawns, on their current position
              player1.draw(display, turquise)
              player2.draw(display, green)       
              player3.draw(display, red)
              player4.draw(display, yellow)
              #displays the current turn
              turn = font3.render(players.select(player_turn) + " its your turn", 1, blue)
              display.blit(turn, (200, 450))
              display.blit(font2.render("-Press space to role the dice-", 1, black), (800, 270))   
              
              if player1.Y < 20 or player2.Y < 20 or player3.Y < 20 or player4.Y < 20:#Check if a player reaches the finish
                  win = pygame.mixer.Sound('sounds/winning.wav') 
                  win.play()#Play winning music
                  select_question = False #To make sure you can't pick a question in the win screen
                  #Draws the win screen
                  win_screen.draw(display, "You won!!!!")
                  win_back_button.draw(display)
                  win_back_button.mouse_event(display, light_red)
                  win_back_button.draw_text("Back To Menu", display)
                  #There are outcomes the game can end: Player 1, 2,3, or 4 can win, this code checks who reached the top
                  if player1.Y < 20:
                      display.blit(font.render(player1.Name + " Your score is: " + str(player1.Score), 1, black), (300, 150))
                      display.blit(font.render("And these are the losers: " + player2.Name + ", " + player3.Name + " and " + player4.Name, 1, black), (200, 250))
                  if player2.Y < 20:
                      display.blit(font.render(player2.Name + " Your score is: " + str(player2.Score), 1, black), (300, 150))
                      display.blit(font.render("And these are the losers: " +player1.Name + ", "+ player3.Name + " and "+ player4.Name, 1, black), (200, 250))
                  if player3.Y < 20:
                      display.blit(font.render(player3.Name + " Your score is: " + str(player3.Score), 1, black), (300, 150))
                      display.blit(font.render("And these are the losers: " +player2.Name + ", " + player1.Name + " and " + player4.Name, 1, black), (200, 250))
                  if player4.Y < 20:
                     display.blit(font.render(player4.Name + " Your score is: " + str(player4.Score), 1, black), (300, 150))
                     display.blit(font.render("And these are the losers: " +player2.Name + ", " + player3.Name + " and "+ player1.Name, 1, black), (200, 250))         
             
          if back_button.Pressed: #The back button resets all buttons and clears the player list and stops all sound and music
              unpress_all()
              players = Node(empty, empty)
              player_turn = 0
              select_question = False
              back_button.Pressed = False
              coffee = False
              pygame.mixer.stop()
              pygame.mixer.music.stop()

          if rules_button.Pressed:
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

          if exit_button.Pressed:#if the exit button is pressed the pygame window closes
              sys.exit() #exits the interperter
              #The build in function break does do the same thing, only the function exits the endless while loop
              #break

             #Only when the game has started, no question is selected and space is pressed you can role the dice
          if start_button.Pressed and key[pygame.K_SPACE] and select_question == False:
             stepps = random.randint(0,5) #changes the stepps variable and the index of the dice list
             select_question = True
             time_left = 50000
             #Picks a random question from the list, from index: 0 to length.list
             pick_question = random.randint(0, q_list.length() - 1)
             question = create_question(pick_question)
             pygame.mixer.music.load('sounds/thinking.mp3')
             pygame.mixer.music.play()

          #Only displays the chosen question if space not pressed, game not on pause and select_question = True
          if select_question == True and not key[pygame.K_SPACE] and coffee == False:
             #displays the timer
             time_text = str(time_left // 1000)
             pygame.draw.circle(display, kind_of_brown, (950, 350), 50)
             display.blit(font.render(time_text, 1,black), (940, 340))
             #Draws the question box
             question.draw(display)
             choice = question.answer(display) #Safes the users answer in a variable
             answered = False
             #The total points are the time_left in secconds + the dice result * 10
             #So the maximum score is 50 + 6*10 = 110
             points = round((time_left//1000) + (10 *stepps))

             #check if the question is correct
             if question.Correct == choice: #If question is correct
                 good = pygame.mixer.Sound('sounds/good.wav') 
                 good.play()
                 if player_turn == 0:
                     player1 = player1.update(points, stepps)
                     print("p1:",player1.Score)
                 if player_turn == 1:
                     player2 = player2.update(points, stepps)
                     print("p2:",player2.Score)
                 if player_turn == 2:
                     player3 = player3.update(points, stepps)
                     print("p3:",player3.Score)
                 if player_turn == 3:
                     player4 = player4.update(points, stepps)
                     print("p4:",player4.Score)
                 pygame.mixer.music.stop()
                 player_turn +=1
                 select_question = False
             if choice != question.Correct and question.Answered or time_left == 0:#If answer is wrong
                 fault = pygame.mixer.Sound('sounds/fault.wav') 
                 fault.play()
                 if player_turn == 0:
                     player1 = player1.update(-points, -stepps)#Decrease the stepps and the score
                     #If score or Y is negative set the value back to zero
                     if player1.Score < 0:
                         player1 = player1.reset_score()
                     if player1.Y > y_set:
                         player1 = player1.reset_pos()
                 if player_turn == 1:
                     player2 = player2.update(-points, -stepps)
                     if player2.Score < 0:
                         player2 = player2.reset_score()
                     if player2.Y > y_set:
                         player2 = player2.reset_pos()
                 if player_turn == 2:
                     player3 = player3.update(-points, -stepps)
                     if player3.Score < 0:
                         player3 = player3.reset_score()
                     if player3.Y > y_set:
                         player3 = player3.reset_pos()
                 if player_turn == 3:
                     player4 = player4.update(-points, -stepps)
                     if player4.Score < 0:
                         player4 = player4.reset_score()
                     if player4.Y > y_set:
                         player4 = player4.reset_pos()
                 pygame.mixer.music.stop()
                 player_turn += 1
                 select_question = False 
             time_left -= 50 #Decrease the timer by 50(aproximatly 1 sec.)

          #During a question you can pause the game
          if select_question == True:
                 if key[pygame.K_p]:#by pressing k
                     coffee = True
                     pygame.time.wait = 10

          if coffee == False and select_question == True:
                 display.blit(font.render("-Press P to get a coffee-", 1, black), (700, 550))

          if coffee == True:
                  coffeebreak(10, 10)
                  display.blit(font.render("-Press O to drink your coffee-", 1, black), (700, 550))
                  
                  if key[pygame.K_o]:#Press o unpauses the game
                      effect.stop()
                      coffee = False

          if key[pygame.K_m]:
             mute = True

          if mute == True:
            pygame.mixer.stop()

          if key[pygame.K_n]:
             mute = False

          if key[pygame.K_c]:
             player1.Y = 20

          pygame.display.update() #This line updates the screen

game(white, width, height)

#Closes the pygame window
pygame.quit()
quit()

#--Copyright al rights reserved, this game is created by Steven Koert, Sem Jansen en Vincent de Heer