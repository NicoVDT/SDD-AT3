import pygame
import random
import time
# Initialize Pygame
pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the game
pygame.display.set_caption("Dodging Game")
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
white = (255, 255, 255)

# Set the clock
clock = pygame.time.Clock()

# Load the images
control_button_hover = pygame.image.load(
    "Menu Buttons/Large Buttons/Large Buttons/Controls Button  Hover.png")
start_game_hover = pygame.image.load(
    "Menu Buttons/Large Buttons/Large Buttons/StartButtonhover.png")
exit_button_hover = pygame.image.load(
    "Menu Buttons/Large Buttons/Large Buttons/Exit Button Hover.png")
back_button_hover = pygame.image.load(
    "Menu Buttons/Square Buttons/Square Buttons/Return Square Button hover.png")
help_button_hover = pygame.image.load(
    "Menu Buttons/Square Buttons/Square Buttons/Questionmark Square Button hover.png")
mute_button_hover = pygame.image.load(
    "Menu Buttons/Square Buttons/Square Buttons/Audio Square Button hover.png")
music_button_hover = pygame.image.load(
    "Menu Buttons/Square Buttons/Square Buttons/Music Square Button hover.png")

mute_button_image = pygame.image.load(
    "Menu Buttons/Square Buttons/Square Buttons/Audio Square Button.png")
muted_button_image = pygame.image.load(
    "Menu Buttons/Square Buttons/Square Buttons/Audio Square Button muted.png")
control_button_image = pygame.image.load(
    "Menu Buttons/Large Buttons/Large Buttons/Controls Button.png")
exit_button_image = pygame.image.load(
    "Menu Buttons/Large Buttons/Large Buttons/Exit Button.png")
help_button_image = pygame.image.load(
    "Menu Buttons/Square Buttons/Square Buttons/Questionmark Square Button.png")
start_game_button_image = pygame.image.load(
    "Menu Buttons/Large Buttons/Large Buttons/Start Button.png")
back_button_image = pygame.image.load(
    "Menu Buttons/Square Buttons/Square Buttons/Return Square Button.png")
music_button_image = pygame.image.load(
    "Menu Buttons/Square Buttons/Square Buttons/Music Square Button.png")

music_mute_button_image = pygame.image.load(
    "Menu Buttons/Square Buttons/Square Buttons/Music Square Button muted.png")

background_image = pygame.image.load("Background.png")

up_image = pygame.image.load(
    r"Menu Buttons/Square Buttons/Square Buttons/Up Square Button.png")
down_image = pygame.image.load(
    "Menu Buttons/Square Buttons/Square Buttons/Down Square Button.png")
left_image = pygame.image.load(
    "Menu Buttons/Square Buttons/Square Buttons/Back Square Button.png")
right_image = pygame.image.load(
    r"Menu Buttons/Square Buttons/Square Buttons/Next Square Button.png")


car_image = pygame.image.load("car.png")
car_width, car_height = car_image.get_rect().size
carbomb_image = pygame.image.load("bomb.png")
# car_width, car_height = carbomb_image.get_rect().size
object_image = pygame.image.load("object.png")
object_width, object_height = object_image.get_rect().size
object_image2 = pygame.image.load("object.png")
object_width, object_height = object_image.get_rect().size
# background = pygame.image.load("background.png").convert()
# screen.blit(background, (100, 100))


kane_image = pygame.image.load("kane.png")
object_width, object_height = object_image.get_rect().size


# Set the font
font = pygame.font.Font(None, 36)


currentscreen: str
music_on = True


def menu():
    screen.blit(background_image, (105, 35))
    if start_button.draw():
        global start_game
        start_game = True

    if exit_button.draw():
        exit()

    if help_button.draw():
        print("help")

    if control_button.draw():
        global currentscreen
        currentscreen = "controls"

    if mute_button.draw():

        mute_button.toggled = not mute_button.toggled

        if mute_button.toggled:
            mute_button.image = mute_button_image
            print("audio is unmuted")
        else:
            mute_button.image = muted_button_image
            print("audio is muted")

    if music_button.draw():

        music_button.toggled = not music_button.toggled

        if music_button.toggled:
            music_button.image = music_button_image
            print("music is unmuted")
        else:
            music_button.image = music_mute_button_image
            print("music is muted")

    start_game_font = pygame.font.Font(None, 65)
    titletext = start_game_font.render(
        "WELCOME TO ROAD RAGE", True, (100, 150, 255))

    screen.blit(titletext, (105, 35))

    pygame.display.flip()


def controls():
    screen.fill(white)
    start_game_font = pygame.font.Font(None, 65)
    control_title = start_game_font.render(
        "Choose your Controls", True, (100, 150, 255))
    if left_key.draw():
        pass
    if right_key.draw():
        pass
    if up_key.draw():
        pass
    if down_key.draw():
        pass

    if back_button.draw():
        global currentscreen
        currentscreen = "menu"
    screen.blit(control_title, (150, 35))
    pygame.display.flip()


def crashscreen(carbomb_image, car_x, car_y):
    global car_image
    car_image = carbomb_image
    pygame.display.flip()
    pygame.mixer.music.load("car_brake_crash.mp3")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play()
    # End game screen
    end_game_font = pygame.font.Font(None, 72)
    end_game_text = end_game_font.render("Game Over", True, (255, 0, 0))
    end_game_rect = end_game_text.get_rect()
    end_game_rect.center = (screen_width // 2, screen_height // 2)
    screen.blit(end_game_text, end_game_rect)
    screen.blit(car_image, (car_x - 16, car_y - 20))
    pygame.display.flip()
    pygame.time.wait(3000)


class Button():
    def __init__(self, x, y, image, scale, hoverimage=None):
        width = image.get_width()
        height = image.get_height()
        self.scale = scale
        self.hoverimage = hoverimage
        self.originalimage = image
        self._image = pygame.transform.scale(
            image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.toggled = False

    def image_set(self, image):
        width = image.get_width()
        height = image.get_height()
        self._image = pygame.transform.scale(
            image, (int(width * self.scale), int(height * self.scale)))

    def image_get(self):
        return self._image
    image = property(image_get, image_set)

    def draw(self):
        # draw button on screen
        action = False

        # get mouse postion
        pos = pygame.mouse.get_pos()
        # check mouse is over button and clicked

        if self.rect.collidepoint(pos):
            if self.hoverimage != None:
                self.image = self.hoverimage
            if pygame.mouse.get_pressed()[0] and self.clicked == False:
                self.clicked = True
                action = True
        else:

            if self.hoverimage != None:
                if self.toggled == False:
                    self.image = self.originalimage

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action


# Menu Screen
start_button = Button(265, 100, start_game_button_image,
                      0.4, hoverimage=start_game_hover)
help_button = Button(263, 278, help_button_image, 0.4,
                     hoverimage=help_button_hover)
control_button = Button(265, 188, control_button_image,
                        0.4, hoverimage=control_button_hover)
exit_button = Button(265, 365, exit_button_image, 0.4,
                     hoverimage=exit_button_hover)
mute_button = Button(344, 278, mute_button_image, 0.4)
# hoverimage=mute_button_hover)
back_button = Button(10, 10, back_button_image, 0.4,
                     hoverimage=back_button_hover)
music_button = Button(425, 278, music_button_image, 0.4)
# hoverimage=music_button_hover)

# Control screen
up_key = Button(550, 200, up_image, 0.4)
down_key = Button(550, 300, down_image, 0.4)
left_key = Button(450, 300, left_image, 0.4)
right_key = Button(650, 300, right_image, 0.4)


# Set the game loop
running = True
start_game = False


def startloop():
    global start_game
    start_game = False
    global currentscreen
    currentscreen = "menu"
    while not start_game:
        # Handle the events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            # if event.type == pygame.MOUSEBUTTONDOWN:
                # start_game = True

        # Draw the screen
        screen.fill(white)
        match currentscreen:
            case "menu":
                menu()
            case "controls":
                controls()


def gameloop():
    # Set the game loop
    global running, car_image
    car_image = pygame.image.load("car.png")

    # Set the position of the car
    car_x = (screen_width - car_width) // 2
    car_y = screen_height - car_height

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
    running = True
    while running:
        # Handle the events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

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
            crashscreen(carbomb_image, car_x, car_y)

        if score == 16:
            object_speed = 9

        if score == 22:
            object_speed = 11

        if score == 25:
            kane_objecty = -object_height
            object_speed = 12.5
        # Draw the screen

        # screen.blit(background, (100, 50))
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


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    startloop()
    gameloop()
