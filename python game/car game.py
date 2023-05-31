import pygame
import random
import os
import math
import sys 
#from pygame_emojis import load_emoji

# Initialize Pygame
pygame.init()

screen_width = 800
screen_height = 600
screen: pygame.Surface = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the game
pygame.display.set_caption("Dodging Game")
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
white = (255, 255, 255)

# Set the clock
clock = pygame.time.Clock()


# Choose the size
size = (64, 64)

# Load the emoji as a pygame.Surface
#left = load_emoji('←', size)
#right = load_emoji('→', size)
#up = load_emoji('↑', size)
#down = load_emoji('↓', size)
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

original_background_image = pygame.image.load("Background.png")
background_image = pygame.transform.scale(
    original_background_image, (800, 600))

gamebackground = pygame.image.load("gamebackground.png")
gamebackgroundrect = gamebackground.get_rect()

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
gamebackground_height = gamebackground.get_height()
tiles = math.ceil(screen_height / gamebackground_height) + 1
print(tiles)
scroll = 0

kane_image = pygame.image.load("kane.png")
object_width, object_height = object_image.get_rect().size


# Set the font
font = pygame.font.Font(None, 36)


currentscreen: str
music_on = True


def menu():
    global Audio
    screen.blit(background_image, (0, 0))
    global currentscreen
    if start_button.draw():
        global start_game
        start_game = True

    if exit_button.draw():
        print("Thanks For Playing!!!")
        exit()

    if help_button.draw():
        currentscreen = "help"
        print("Help Menu")

    if control_button.draw():
        currentscreen = "controls"

    if mute_button.draw():

        mute_button.toggled = not mute_button.toggled

        if mute_button.toggled:
            mute_button.image = mute_button_image
            print("audio is unmuted")
            pygame.mixer.unpause()

        else:
            mute_button.image = muted_button_image
            print("audio is muted")
            Audio = False

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


leftconfig = False
rightconfig = False
downconfig = False
upconfig = False


def controls(upuni, downuni, leftuni, rightuni):
    start_game_font = pygame.font.Font(None, 65)
    mediumfont = pygame.font.Font(None, 40)
    screen.fill(white)
    up_arrow = start_game_font.render(upuni, True, (100, 200, 255))
    down_arrow = start_game_font.render(downuni, True, (100, 200, 255))
    left_arrow = start_game_font.render(leftuni, True, (100, 200, 255))
    right_arrow = start_game_font.render(rightuni, True, (100, 200, 255))

    controltext = mediumfont.render(
        "Your Current Controls", True, (100, 200, 255))

    control_title = start_game_font.render(
        "Choose your Controls", True, (100, 150, 255))
    if left_key.draw():
        global leftconfig
        leftconfig = True

    if right_key.draw():
        global rightconfig
        rightconfig = True

    if up_key.draw():
        global upconfig
        upconfig = True

    if down_key.draw():
        global downconfig
        downconfig = True

    if back_button.draw():
        global currentscreen
        currentscreen = "menu"
    screen.blit(up_arrow, (98, 260))
    screen.blit(down_arrow, (100, 300))
    screen.blit(right_arrow, (130, 300))
    screen.blit(left_arrow, (70, 300))
    screen.blit(control_title, (150, 35))
    screen.blit(controltext, (80, 140))

    pygame.display.flip()
SIZE = WIDTH, HEIGHT = (1024, 720)
def blit_text(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += 25  # Start on new row.


text = "Game Name: Road Rage\nVersion: 1.0\nMade By: Nicholas Van Delft\nDate of release: 12/06/2023"
instructions_info = "How to Play:\nRoad Rage is a simple top-down 2D game\nYou shoot and try to doge obsticales coming towards you.\nAs you progress through the level doging more obsticales\nThe obsticals will start to multiply and speed up!\n\nIn the control menu you must click the keybind you want to change\nThen you must press the key down on your keyboard\nThe Visual represetation of your keybinds on the left will then change."



def help():
    screen.fill(white)
    start_game_font = pygame.font.Font(None, 65)
    abouttext_font = pygame.font.Font(None, 25)
    help_title = start_game_font.render(
        "Help Menu", True, (100, 150, 255))
    about_info = abouttext_font.render("Game Name: Road Rage\nVersion: 1.0\nMade By: Nicholas Van Delft\n Date of release: 12/06/2023", True, (100, 150, 255))
    if back_button.draw():
        global currentscreen
        currentscreen = "menu"
    
    blit_text(screen, text, (10, 500), font)
    blit_text(screen, instructions_info, (10,100 ), font)
    screen.blit(help_title, (270, 35))
    
    pygame.display.flip()


def crashscreen(carbomb_image: pygame.surface.Surface, car_x: int, car_y: int):
    global car_image
    car_image = carbomb_image  # type: ignore
    pygame.display.flip()
    pygame.mixer.music.load("car_brake_crash.mp3")
    pygame.mixer.music.set_volume(0.3)
    if Audio:
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


class Preferences():
    def __init__(self):
        self.up: int = pygame.K_UP
        self.down: int = pygame.K_DOWN
        self.left: int = pygame.K_LEFT
        self.right: int = pygame.K_RIGHT
        self.audioEnabled: bool = True
        self.soundsEnabled: bool = True


prefs = Preferences()


class Button():
    def __init__(self, x: int, y: int, image, scale: float | int, hoverimage: pygame.surface.Surface | None = None):
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

    def image_set(self, image: pygame.surface.Surface):
        width = image.get_width()
        height = image.get_height()
        self._image = pygame.transform.scale(
            image, (int(width * self.scale), int(height * self.scale)))

    def image_get(self) -> pygame.surface.Surface:
        return self._image
    image = property(image_get, image_set)

    def draw(self) -> bool:
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
    global upuni, downuni, leftuni, rightuni
    start_game = False
    upuni = "up"
    downuni = "down"
    leftuni = "left"
    rightuni = "right"

    global currentscreen
    currentscreen = "menu"
    global leftconfig, rightconfig, upconfig, downconfig
    while not start_game:
        # Handle the events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if leftconfig:
                if event.type == pygame.KEYDOWN:
                    print(event.dict['key'])
                    prefs.left = event.dict['key']
                    leftconfig = False
                    leftuni = event.dict["unicode"]
            elif rightconfig:
                if event.type == pygame.KEYDOWN:
                    print(event.dict['key'])
                    prefs.right = event.dict['key']
                    rightuni = event.dict["unicode"]
                    rightconfig = False
            elif downconfig:
                if event.type == pygame.KEYDOWN:
                    prefs.down = event.dict['key']
                    downuni = event.dict["unicode"]
                    downconfig = False
                    print(event.dict['key'])
            elif upconfig:
                if event.type == pygame.KEYDOWN:
                    print(event.dict['key'])
                    upuni = event.dict["unicode"]
                    prefs.up = event.dict['key']
                    print(event.dict["unicode"])
                    upconfig = False
            # if event.type == pygame.MOUSEBUTTONDOWN:
                # start_game = True

        # Draw the screen
        screen.fill(white)
        match currentscreen:
            case "menu":
                menu()
            case "controls":
                controls(upuni, downuni, leftuni, rightuni)
            case "help":
                help()


def gameloop(scroll):
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

        # Move the background

        # Move the car
        keys = pygame.key.get_pressed()
        if keys[prefs.left] and car_x > 0:
            car_x -= car_speed
        if keys[prefs.right] and car_x < screen_width - car_width:
            car_x += car_speed
        if keys[prefs.up] and car_y > 0:
            car_y -= car_speed
        # print(f"K_w {pygame.K_w}")
        # print(f"prefs up {prefs.up}")
        if keys[prefs.down] and car_y < screen_height - car_height:
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
        for i in range(0, tiles):
            screen.blit(gamebackground,
                        (0, -i * gamebackground_height + scroll))
            screen.blit(gamebackground,
                        (0, i * gamebackground_height + scroll))
            gamebackgroundrect.y = i * gamebackground_height + scroll
            # pygame.draw.rect(screen, (255, 0, 0), gamebackgroundrect, 1)

        # scroll speed
        scroll += 4

        # reset scroll

        if abs(scroll) > gamebackground_height:
            scroll = 0

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
    gameloop(scroll)
