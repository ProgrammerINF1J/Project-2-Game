#--Copyright all rights reserved, this game is created by Steven Koert, Sem Jansen en Vincent de Heer

import sys, pygame, time, random
pygame.init()

#Globals
width = 1024
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
turquise = 75, 220, 230
yellow = 225, 200, 10
kind_of_brown = 210, 200,110
x_set = 150
y_set = 400

font = pygame.font.Font(None, 30)#Grote text, wordt gebruikt voor de buttons
font2 = pygame.font.Font(None, 20)#Kleine text, wordt gebruikt voor het input scherm
font3 = pygame.font.Font(None, 70)

#image library, place all images here
logo = pygame.image.load("skyline.png")
rulesImg = pygame.image.load('Knipsel1.png')
rulesImg1 = pygame.image.load('Knipsel2.png')
dice1Img = pygame.image.load('Dobbel1.png')
dice2Img = pygame.image.load('Dobbel2.png')
dice3Img = pygame.image.load('Dobbel3.png')
dice4Img = pygame.image.load('Dobbel4.png')
dice5Img = pygame.image.load('Dobbel5.png')
dice6Img = pygame.image.load('Dobbel6.png')
background = pygame.image.load('background.png')
coffeeImg = pygame.image.load("coffee.png")
 



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
    def fold(self, function, predicate):
        return function(self.Value, self.Tail.fold(function, predicate))
    def length(self):
        return self.fold(lambda x, y: y +1,0)
    def print_pygame(self, x, y, n): 
        """displays the list on the pygame window"""
        text = font.render(str(n) + ": " + self.Value,1, black)
        display.blit(text, (x, y))
        return self.Tail.print_pygame(x, y + 30, n+1)
    def select(self, index): 
        """selects an item from a list with the matching index start with 0"""
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
                click = pygame.mixer.Sound('click.wav') 
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
# Node("", Node("", Node("", Node("", Node("", Node("", empty)))))) standard question = [Q, A, B, C, D, answer, empty]

q_list = Node(question1, Node(question2, Node(question3, Node(question4, Node(question5, Node(question6, Node(question7, Node(question8, Node(question9, Node(question10, Node(question11, Node(question12, Node(question13, Node(question14, Node(question15, Node(question16, Node(question17, Node(question18, Node(question19, Node(question20, Node(question21, Node(question22, empty))))))))))))))))))))))

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
        pygame.draw.rect(surface,turquise, (width//4, height//4, 400, 180))
        pygame.draw.rect(surface, yellow ,(width//4, height//4, 400, 50))
        question = font2.render(self.Question, 1, black)
        surface.blit(question, (width//4 + 10, height//4 + 20))
    def answer(self, surface):
        height_btn = 30
        width_btn = 150
        a = Button(280, 220, height_btn, width_btn, orange)
        a.draw(surface)
        a_text = font2.render(self.Option_A, 1, black)
        surface.blit(a_text, (280, 230))
        a.mouse_event(surface, red)

        b = Button(280, 260, height_btn, width_btn, orange)
        b.draw(surface)
        b_text = font2.render(self.Option_B, 1, black)
        surface.blit(b_text, (280, 270))
        b.mouse_event(surface, red)

        c = Button(470, 220, height_btn, width_btn, orange)
        c.draw(surface)
        c_text = font2.render(self.Option_C, 1, black)
        surface.blit(c_text, (470, 230))
        c.mouse_event(surface, red)

        d = Button(470, 260, height_btn, width_btn, orange)
        d.draw(surface)
        d_text = font2.render(self.Option_D, 1, black)
        surface.blit(d_text, (470, 270))
        d.mouse_event(surface, red)

        if a.Pressed:
            self.Answered = True
            return self.Option_A
        if b.Pressed:
            self.Answered = True
            return self.Option_B            
        if c.Pressed:
            self.Answered = True
            return self.Option_C          
        if d.Pressed:
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
    display.blit(rulesImg, (x *0,5,y*0,5))

def rules1(x,y):
    display.blit(rulesImg1, (x*0,5,y*0,5))

def coffeebreak():
        display.blit(coffeeImg, (0, 0))
        effect = pygame.mixer.Sound('coffee.wav') 
        effect.play()
       
       
        

def player_list(amount_players):
    """Returns a list of all players, including names starts with 1 and ends with 4"""
    if amount_players < 5: 
         player = print_list(ask_name(display, "Player " + str(amount_players) + " enter your name: "))
         return Node(player, player_list(amount_players + 1))
    else:
         return empty        
   
def game(color, width, height):
    """Defines the entire game, put the display functions inside the while loop """
    def start():
        
        return True

    def end():
        return False

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



    #button library
    start_button = Button(width//8, height//2, 50, 100, green)#x, y, H, W
    exit_button = Button(width//2, height//2, 50, 100, red)
    rules_button = Button((5*width)//16, height//2, 50, 100, blue)
    back_button = Button(width -150, 50, 50,100, red)
    rules_button2 = Button(width - 150, 500, 50, 100, blue)
    players = Node(empty , empty) #Sets the list players to empty
    select_question = False
    key = pygame.key.get_pressed()
    stepps = random.randint(0,5)
    player_turn = 0
    coffee = False
    mute = False

    pygame.display.set_caption("Euromast: The Game") #Defines the title of the game
    
    #the game loop
    while not process_events():
          key = pygame.key.get_pressed()
          display.fill(color)
          if player_turn >3:
              player_turn = 0

          if check_button() == False:#The menu will only apear when nothing is pressed
                display_menu() #When you press a button the menu will disappear
         
          if start_button.Pressed and players.length() < 4:
             players = player_list(1)
             player1 = Player(players.select(0), 0, x_set,y_set)
             player2 = Player(players.select(1), 0, x_set+180,y_set)
             player3 = Player(players.select(2), 0, x_set+360,y_set)
             player4 = Player(players.select(3), 0, x_set+540,y_set)
             startup = pygame.mixer.Sound('startup.wav') 
             startup.play()
             

          if start_button.Pressed:
              display.blit(background,(0,0))
              back() 
              display.blit(dice.select(stepps), (870, 130))
              players.print_pygame(width - 320, 50, 1)      
              display.blit(font.render(str(player1.Name) +" "+ str(player1.Score), 1, black), (player1.X -len(player1.Name), player1.Y + 20))
              display.blit(font.render(str(player2.Name) +" "+ str(player2.Score), 1, black), (player2.X -len(player2.Name), player2.Y + 20))
              display.blit(font.render(str(player3.Name) +" "+ str(player3.Score), 1, black), (player3.X -len(player3.Name), player3.Y + 20))
              display.blit(font.render(str(player4.Name) +" "+ str(player4.Score), 1, black), (player4.X- len(player4.Name), player4.Y + 20))
              player1.draw(display, turquise)
              player2.draw(display, green)       
              player3.draw(display, red)
              player4.draw(display, yellow)
              
              
              turn = font3.render(players.select(player_turn) + " its your turn", 1, blue)
              display.blit(turn, (200, 450))
              display.blit(font2.render("-Press space to role the dice-", 1, black), (800, 270))

             

          if back_button.Pressed: #The back button resets all buttons and clears the player list
              unpress_all()
              players = Node(empty, empty)
              select_question = False
              #pygame.time.wait(100)
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

          if start_button.Pressed and key[pygame.K_SPACE] and select_question == False:           
             stepps = random.randint(0,5)
             select_question = True
             time_left = 50000
             pick_question = random.randint(0, q_list.length() - 1)
             question = create_question(pick_question) 

          if select_question == True and not key[pygame.K_SPACE] and coffee == False:
             time_text = str(time_left // 1000)
             pygame.draw.circle(display, kind_of_brown, (950, 350), 50)
             display.blit(font.render(time_text, 1,black), (940, 340))
             question.draw(display)
             choice = question.answer(display)
             answered = False
             points = round((time_left//1000) + (10 *stepps))
             if question.Correct == choice:

                 good = pygame.mixer.Sound('good.wav') 
                 good.play()
                 #display.blit(font.render("'" + choice + "'" + " is correct!!!", 1, black), (400, 10))
                 if player_turn == 0:
                     player1 = player1.update(points, stepps)
                 if player_turn == 1:
                     player2 = player2.update(points, stepps)
                 if player_turn == 2:
                     player3 = player3.update(points, stepps)
                 if player_turn == 3:
                     player4 = player4.update(points, stepps) 
                 player_turn +=1
                 print("Question good")
                 #pygame.time.wait(500)
                 select_question = False
             if choice != question.Correct and question.Answered or time_left == 0:
                 fault = pygame.mixer.Sound('fault.wav') 
                 fault.play()
                 if player_turn == 0:
                     player1 = player1.update(-points, -stepps)
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
                 if player_turn == y_set:
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
                 player_turn += 1
                 print("Question wrong")
                 #pygame.time.wait(500)
                 select_question = False
             time_left -= 50

          if select_question == True:
            
            
            if key[pygame.K_p]:
              coffee = True
              
              pygame.time.wait = 10

          if coffee == False and select_question == True:
              display.blit(font.render("-Press P to get a coffee-", 1, white), (700, 550))

          if coffee == True:
              coffeebreak()
              display.blit(font.render("-Press O to drink your coffee-", 1, white), (700, 550))
              
              if key[pygame.K_o]:
                  coffee = False
                

          if key[pygame.K_m]:
             mute = True

          if mute == True:
            pygame.mixer.stop()

          if key[pygame.K_n]:
             mute = False
              
          
          
          
          #print(pygame.mouse.get_pos())

          pygame.display.update()

game(white, width, height)

#Closes the pygame window
pygame.quit()
quit()

#--Copyright all rights reserved, this game is created by Steven Koert, Sem Jansen en Vincent de Heer
