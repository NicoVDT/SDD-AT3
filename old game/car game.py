import pygame
import random
import time
import sys
# Initialize Pygame
pygame.init()

# Set the screen size
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the game
pygame.display.set_caption("Dodging Game")
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define the game name font and size
game_name_font = pygame.font.SysFont("Arial", 64)
button_font = pygame.font.SysFont("Arial", 32)
# Set the clock
clock = pygame.time.Clock()

# Load the images
car_image = pygame.image.load("car.png")
car_width, car_height = car_image.get_rect().size
carbomb_image = pygame.image.load("carbomb.png")
#car_width, car_height = carbomb_image.get_rect().size
object_image = pygame.image.load("object.png")
object_width, object_height = object_image.get_rect().size
object_image2 = pygame.image.load("object.png")
object_width, object_height = object_image.get_rect().size
#background = pygame.image.load("background.png").convert()
#screen.blit(background, (100, 100))

kane_image = pygame.image.load("kane.png")
object_width, object_height = object_image.get_rect().size




# Set the position of the car
car_x = (screen_width - car_width) // 2
car_y = screen_height - car_height

# Set the position of the bullet 
bullet_x = (screen_width - car_width) // 2 
bullet_y = screen_height - car_height


# Set the speed of the car
car_speed = 5

# Set the position of the object
object_x = random.randint(0, screen_width - object_width)
object_y = -object_height

object_2x = random.randint(0, screen_width - object_width)
object_2y = -object_height

kane_objectx = random.randint(0, screen_width - object_width)
kane_objecty = -700

# Set the speed of the object
object_speed = 5


# Set the score
score = 0


# Set the font
font = pygame.font.Font(None, 36)

#Load the sounds 
def crashnoise(carbomb_image):
    global car_image
    car_image = carbomb_image
    pygame.display.flip()
    pygame.mixer.music.load("car_brake_crash.mp3")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play()
   
game_name_text = "Car Game"
# Set the game loop
colourcounter = 499
running = True
start_game = True
while start_game:
    # Handle the events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start_game = False
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            start_game = False

    # Draw the screen
    
    #background_colour = (200,50,50)
    #colourcounter += 1 
    #if colourcounter > 500:
        #colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        #colourcounter = 0 
        #screen.fill(colour)
    #button_colour = (50, 150 ,50)
    mouse = pygame.mouse.get_pos()
    #if 250 + 300 > mouse[0] > 250 and 255 + 80 > mouse[1] > 255:
        #pygame.draw.rect(screen, bright_green, pygame.Rect(250, 255, 300, 80))
    #else:
        #pygame.draw.rect(screen, green, pygame.Rect(250, 255, 300, 80))

          # Fill the screen with black
    screen.fill(BLACK)
    # Draw the game name text on the screen
    screen.blit(game_name_text, game_name_rect)
    # Draw the select car button on the screen
    draw_button(screen, select_car_text, select_car_rect, RED)
    # Draw the help button on the screen
    draw_button(screen, help_text, help_rect, BLUE)
    # Update the display
    pygame.display.flip()
    # Loop through the events in the event queue
    for event in pygame.event.get():
        # If the user clicks the close button, quit the game
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        # If the user clicks the mouse button
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse position
            mouse_pos = pygame.mouse.get_pos()
            # If the mouse position is inside the select car button rectangle
            if select_car_rect.collidepoint(mouse_pos):
                # TODO: Add code to go to the select car screen
                print("Select car button clicked")
            # If the mouse position is inside the help button rectangle
            if help_rect.collidepoint(mouse_pos):
                # TODO: Add code to go to the help screen
                print("Help button clicked")

        # Define the game name text and position
    game_name_text = game_name_font.render("Car Dodge Game", True, WHITE)
    game_name_rect = game_name_text.get_rect()
    game_name_rect.center = (screen_width // 2, screen_height // 4)

# Define the select car button text and position
    select_car_text = button_font.render("Select Car", True, WHITE)
    select_car_rect = select_car_text.get_rect()
    select_car_rect.center = (screen_width // 4, screen_height // 2)

# Define the help button text and position
    help_text = button_font.render("Help", True, WHITE)
    help_rect = help_text.get_rect()
    help_rect.center = (screen_width * 3 // 4, screen_height// 2)

    start_game_font = pygame.font.Font(None, 65)
    start_game_text = start_game_font.render("Click to Start", True, (255, 255, 255))
    
    start_game_rect = start_game_text.get_rect()
    start_game_rect.center = (screen_width // 2, screen_height // 2)
    screen.blit(start_game_text, start_game_rect)
    
    def draw_button(screen, text, rect, color):
    # Draw a rectangle with the given color
        pygame.draw.rect(screen, color, rect)
    # Draw the text on top of the rectangle
        screen.blit(text, rect)
    pygame.display.flip()
    

# Set the game loop
while running:
    # Handle the events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the car
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < screen_width - car_width:
        car_x += car_speed
    if keys[pygame.K_UP] and car_y > 0:
        car_y -= car_speed
    if keys[pygame.K_DOWN] and car_y < screen_height - car_height:
        car_y += car_speed

    # Move the object
    object_y += object_speed
    if object_y > screen_height:
        object_x = random.randint(0, screen_width - object_width)
        object_y = -object_height
        score += 1
    bullet = pygame.draw.rect(screen, bright_red, pygame.Rect(500, 350, 60, 60))
    if score >= 6:
        object_2y += object_speed
        if object_2y > screen_height:
            object_2x = random.randint(0, screen_width - object_width + 3)
            object_2y = -object_height
            score += 1

    if score >= 25:
        kane_objecty += object_speed
        if kane_objecty > screen_height:
            kane_objectx = random.randint(0, screen_width - object_width)
            kane_objecty = -object_height
            score += 1

    if score >= 40:
        pass
        
    # Check for collision
    if car_x < object_x + object_width and car_x + car_width > object_x and car_y < object_y + object_height and car_y + car_height > object_y:
        running = False
        crashnoise(carbomb_image)

    if score == 16:
        object_speed = 9
    
    if score == 22:
        object_speed = 11

    if score == 25:
        kane_objecty = -object_height
        object_speed = 12.5
    # Draw the screen
    
    #screen.blit(background, (100, 50))
  


    screen.fill((255, 255, 255))
    screen.blit(car_image, (car_x, car_y))
    screen.blit(object_image, (object_x, object_y))
    screen.blit(object_image2, (object_2x, object_2y))
    screen.blit(kane_image, (kane_objectx, kane_objecty))
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
   
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)

# End game screen
end_game_font = pygame.font.Font(None, 72)
end_game_text = end_game_font.render("Game Over", True, (255, 0, 0))
end_game_rect = end_game_text.get_rect()
end_game_rect.center = (screen_width // 2, screen_height // 2)
screen.blit(end_game_text, end_game_rect)
pygame.display.flip()

# Wait for 3 seconds
pygame.time.wait(3000)

# Quit Pygame
pygame.quit()