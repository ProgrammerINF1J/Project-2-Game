import pygame


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

font = pygame.font.Font(None, 30)
font2 = pygame.font.Font(None, 20)

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
        self.Value = value
        self.Tail = tail
        self.IsEmpty = False
    def __str__(self):
        return str(self.Value) + "\n" + str(self.Tail)

class Empty():
    def __init__(self):
        self.IsEmpty = True
    def __str__(self):
        return ""

empty = Empty()
"""
class Text_Box():
    def __init__(self, message ,x, y,height, width, color):
        self.Message = message
        self.X = x
        self.Y = y
        self.Height = height
        self.Width = width
        self.Color = color
    def draw(self, surface):
        pygame.draw.rect(surface, self.Color, (self.X , self.Y, self.Width, self.Height))
        pygame.draw.rect(surface, white, (self.X + self.Width//14, self.Y + self.Height//3, self.Width - 40, self.Height //2))
        if len(self.Message) > 0:
            text = font.render(self.Message, 1, black)
            surface.blit(text, (self.X + self.Width // 14, self.Y + self.Height //2))
    def ask(self):
        name = []
        while 1:
             key = get_key()
             if key == pygame.K_BACKSPACE:
                  name = name[0:-1]
             elif key == pygame.K_RETURN:
                  break
             elif key == pygame.K_MINUS:
                  name.append("_") 
             elif key <= 127:
                  name.append(chr(key))


def get_key():
    while 1:
       event = pygame.event.poll()
       if event.type == pygame.KEYDOWN: 
          return event.key
       else:
           pass

"""#Oude code text_field

class TextBox():
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
        

def ask(screen, question):
  "ask(screen, question: string) -> answer"
  name = []
  text_box = TextBox(question + str(print_list(name)), 100, 100, 600, 100, (red))
  text_box.draw(screen)
  while True:
    key = get_key()
    if key == pygame.K_BACKSPACE:
      name = name[0:-1] 
    elif key == pygame.K_RETURN:
      return name
    elif key <= 127:
        if key == pygame.K_RSHIFT:
            key = ord(key) - 32
        name.append(chr(key))
    text_box = TextBox(question + str(print_list(name)), 100, 100, 600, 100, (red))
    text_box.draw(screen)
    
def print_list(list):
    """This function does not print the node/empty data structure list but a list in the shape of an array"""
    tmp_list = ""
    for i in range(len(list)):
        tmp_list = tmp_list + list[i]
    return tmp_list


def game(color, width, height):

   
    
    while not process_events():
        display.fill(color)
        n = 1
        while n < 5:
            name = ask(display, "what is your name player " + str(n) + "?:  ")
            print(print_list(name))
            n += 1

        pygame.display.update()


game(green, width ,height)




