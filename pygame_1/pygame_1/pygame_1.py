import math
import pygame
from database import *

#screen size
width = 800
height = 400

class Player:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.score = player1_score
        self.name = player1_name

    def update(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            self.x -= 1
        elif keys[pygame.K_RIGHT]:
            self.x += 1

        if keys[pygame.K_UP]:
            self.y -= 1
        elif keys[pygame.K_DOWN]:
            self.y += 1

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 255, 0),
                           (int(self.x), int(self.y)), int(self.r))

class Enemy:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.health = 255

    def update(self, player, player_addscore):
        # If this enemy is colliding with the player
        if math.sqrt((player.x - self.x) ** 2 +
                     (player.y - self.y) ** 2) < self.r + player.r:
            self.health -= 1
            if self.health == 0:
                self.health = 255
                player.score += player_addscore
                player.x = width * 0.2
                player.y = height * 0.5
                update_score(player.name, player.score)

    def draw(self, screen):
        pygame.draw.circle(screen, (self.health, 0, 0),
                           (int(self.x), int(self.y)), int(self.r))

# Handle pygame events
def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Give the signal to quit
            return True
    return False

# Main program logic
def program():
    size = (width, height)
    
    # Start PyGame
    pygame.init()
    
    # Set the resolution
    screen = pygame.display.set_mode(size)
    
    # Set up the default font
    font = pygame.font.Font(None, 30)
    
    # Create an enemy
    enemy = Enemy(width * 0.8, height * 0.5, width * 0.1)
    
    # Create the player
    player = Player(width * 0.2, height * 0.5, width * 0.1)

    while not process_events():
        # Update entities
        player.update()
        enemy.update(player, 10)
        
        # Clear the screen
        screen.fill((0, 0, 0))
        
        # Draw the entities
        enemy.draw(screen)
        player.draw(screen)
        
        # Draw the score text
        score_text = font.render(str(player.score), 1, (255, 255, 255))
        screen.blit(score_text, (16, 16))
        
        # Flip the screen
        pygame.display.flip()
        
# Start the program
program()

# close the cursor object
cc.close ()

# close the connection
conn.close ()